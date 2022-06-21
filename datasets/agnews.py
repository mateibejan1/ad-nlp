from base.torchnlp_dataset import TorchnlpDataset
from torchnlp.datasets.dataset import Dataset
from torchnlp.encoders.text import SpacyEncoder
from torchnlp.utils import datasets_iterator
from torchnlp.encoders.text.default_reserved_tokens import DEFAULT_SOS_TOKEN
from torch.utils.data import Subset
from nltk.corpus import reuters
from nltk import word_tokenize
from utils.text_encoders import MyBertTokenizer
from utils.misc import clean_text
from .preprocessing import compute_tfidf_weights

import os
import torch
import nltk

class AGN_Dataset(TorchnlpDataset):

    def __init__(self, root: str, normal_class=0, tokenizer='spacy', use_tfidf_weights=False, append_sos=False,
                 append_eos=False, clean_txt=False):
        super().__init__(root)

        self.n_classes = 2
        classes = ['business', 'sci', 'sports', 'world']

        self.normal_classes = [classes[normal_class]]
        del classes[normal_class]
        self.outlier_class = classes

        self.train_set, self.test_set = agnews_dataset(directory='./data/ag_news/', train=True, test=True)

        # Pre-process
        self.train_set.columns.add('index')
        self.test_set.columns.add('index')
        self.train_set.columns.add('weight')
        self.test_set.columns.add('weight')

        train_idx_normal = []  # for subsetting train_set to normal class
        for i, row in enumerate(self.train_set):
            if row['label'] in self.normal_classes:
                train_idx_normal.append(i)
                row['label'] = torch.tensor(0)
            else:
                row['label'] = torch.tensor(1)
            row['text'] = row['text'].lower()

        for i, row in enumerate(self.test_set):
            row['label'] = torch.tensor(0) if row['label'] in self.normal_classes else torch.tensor(1)
            row['text'] = row['text'].lower()

        # Subset train_set to normal class
        self.train_set = Subset(self.train_set, train_idx_normal)
        print(len(self.train_set))

        # Make corpus and set encoder
        text_corpus = [row['text'] for row in datasets_iterator(self.train_set, self.test_set)]
        if tokenizer == 'spacy':
            self.encoder = SpacyEncoder(text_corpus, min_occurrences=3, append_eos=append_eos)
        if tokenizer == 'bert':
            self.encoder = MyBertTokenizer.from_pretrained('bert-base-uncased', cache_dir=root)

        # Encode
        for row in datasets_iterator(self.train_set, self.test_set):
            if append_sos:
                sos_id = self.encoder.stoi[DEFAULT_SOS_TOKEN]
                row['text'] = torch.cat((torch.tensor(sos_id).unsqueeze(0), self.encoder.encode(row['text'])))
            else:
                row['text'] = self.encoder.encode(row['text'])

        # Compute tf-idf weights
        if use_tfidf_weights:
            compute_tfidf_weights(self.train_set, self.test_set, vocab_size=self.encoder.vocab_size)
        else:
            for row in datasets_iterator(self.train_set, self.test_set):
                row['weight'] = torch.empty(0)

        # Get indices after pre-processing
        for i, row in enumerate(self.train_set):
            row['index'] = i
        for i, row in enumerate(self.test_set):
            row['index'] = i

def agnews_dataset(directory='./data/ag_news/', train=True, test=False):
    classes = ['business', 'sci', 'sports', 'world']
    ret = []
    splits = [split_set for (requested, split_set) in [(train, 'train'), (test, 'test')] if requested]

    for split_set in splits:

        path = os.path.join(directory, split_set)
        examples = []

        if split_set == 'train':
            for subset in classes:
                with open(f'{path}/{subset}.txt') as fp:
                # with open(f'{path}/{subset}.txt') as fp:
                    # from os import listdir
                    # from os.path import isfile, join
                    # onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
                    # print(onlyfiles)

                    print(f'{path}/{subset}.txt')
                    line = fp.readline()
                    while line:
                        if line != '\n':
                            examples.append({
                                'text': line[:-1],
                                'label': subset
                            })
                        line = fp.readline()
        else:
            for subset in classes:
                with open(f'{path}/{subset}.txt') as fp:

                    print(f'{path}/{subset}.txt')
                    line = fp.readline()
                    while line:
                        if line != '\n':
                            examples.append({
                                'text': line[:-1],
                                'label': subset
                            })
                        line = fp.readline()

        ret.append(Dataset(examples))

    if len(ret) == 1:
        return ret[0]
    else:
        return tuple(ret)

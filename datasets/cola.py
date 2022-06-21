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

import torch
import nltk

import glob
import pandas as pd
import math
from os import listdir
from os.path import isfile, join

class Cola_Dataset(TorchnlpDataset):

    def __init__(self, root: str, normal_class=0, tokenizer='spacy', use_tfidf_weights=False, append_sos=False,
                 append_eos=False, clean_txt=False):
        super().__init__(root)

        self.n_classes = 2  # 0: normal, 1: outlier
        files = [join(root, f) for f in listdir(join(root, 'train')) if isfile(join(root, 'train',f))]
        classes = [data_class.split('/')[-1].split('.')[0] for data_class in files]

        self.normal_classes = [classes[normal_class]]
        del classes[normal_class]
        self.outlier_class = classes

        self.train_set, self.test_set = cola_dataset(directory=root, train=True, test=True)

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

        self.train_set = Subset(self.train_set, train_idx_normal)

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

def cola_dataset(directory='./data/cola/raw/', train=True, test=False, clean_txt=False):

    files = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f))]
    classes = [data_class.split('/')[-1].split('.')[0] for data_class in files]
    data_dict_train, data_dict_test = {'label': None, 'text': None}, {'label': None, 'text': None}
    ret = []

    for file_name in glob.glob(join(directory, 'train', '*.txt')):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line != '\n':
                    if data_dict_train['label'] == None:
                        data_dict_train['label'] = [file_name.split('/')[-1].split('.')[0]]
                    else:
                        data_dict_train['label'].append(file_name.split('/')[-1].split('.')[0])
                    if data_dict_train['text'] == None:
                        data_dict_train['text'] = [line]
                    else:
                        data_dict_train['text'].append(line) 

    df_train = pd.DataFrame(data_dict_train, columns = ['label', 'text'])

    for file_name in glob.glob(join(directory, 'test', '*.txt')):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line != '\n':
                    if data_dict_test['label'] == None:
                        data_dict_test['label'] = [file_name.split('/')[-1].split('.')[0]]
                    else:
                        data_dict_test['label'].append(file_name.split('/')[-1].split('.')[0])
                    if data_dict_test['text'] == None:
                        data_dict_test['text'] = [line]
                    else:
                        data_dict_test['text'].append(line)

    df_test = pd.DataFrame(data_dict_test, columns = ['label', 'text'])

    for df in [df_train, df_test]:
        examples = []
        for key, row in df.iterrows():
            examples.append({'text': row['text'],
                             'label': row['label']})
        ret.append(Dataset(examples))

    if len(ret) == 1:
        return ret[0]
    else:
        return tuple(ret)
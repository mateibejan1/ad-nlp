from .reuters21578 import Reuters_Dataset
from .newsgroups20 import Newsgroups20_Dataset
from .imdb import IMDB_Dataset
from .agnews import AGN_Dataset
from .gutenberg_authors import Gutenberg_Authors_Dataset
from .gutenberg_categories import Gutenberg_Categories_Dataset
from .song_artists import Song_Artists_Dataset
from .song_genres import Song_Genres_Dataset
from .pan2011_mails import Pan2011_Mail_Dataset
from .pan2020_5 import Pan2020_5_Dataset
from .pan2020_15 import Pan2020_15_Dataset
from .pan2020_25 import Pan2020_25_Dataset
from .cola import Cola_Dataset
from .vua import Vua_Dataset

def load_dataset(dataset_name, data_path, normal_class, tokenizer='spacy', use_tfidf_weights=False,
                 append_sos=False, append_eos=False, clean_txt=False):
    """Loads the dataset."""

    implemented_datasets = ('reuters', 'newsgroups20', 'imdb', 'ag_news', 'gutenberg_authors', 
                            'gutenberg_categories', 'pan2011_mails', 'song_artists', 'song_genres', 
                            'pan2020_5', 'pan2020_15', 'pan2020_25', 'cola', 'vua')
    assert dataset_name in implemented_datasets

    dataset = None

    if dataset_name == 'reuters':
        dataset = Reuters_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                  use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                  clean_txt=clean_txt)

    if dataset_name == 'newsgroups20':
        dataset = Newsgroups20_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                       use_tfidf_weights=use_tfidf_weights, append_sos=append_sos,
                                       append_eos=append_eos, clean_txt=clean_txt)

    if dataset_name == 'imdb':
        dataset = IMDB_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                               use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                               clean_txt=clean_txt)

    if dataset_name == 'ag_news':
        dataset = AGN_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                               use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                               clean_txt=clean_txt)

    if dataset_name == 'gutenberg_authors':
        dataset = Gutenberg_Authors_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                            use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                            clean_txt=clean_txt)

    if dataset_name == 'gutenberg_categories':
        dataset = Gutenberg_Categories_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                               use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                               clean_txt=clean_txt)

    if dataset_name == 'song_artists':
        dataset = Song_Artists_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                       use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                       clean_txt=clean_txt)

    if dataset_name == 'song_genres':
        dataset = Song_Genres_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                      use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                      clean_txt=clean_txt)

    if dataset_name == 'pan2011_mails':
        dataset = Pan2011_Mail_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                       use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                       clean_txt=clean_txt)

    if dataset_name == 'pan2020_5':
        dataset = Pan2020_5_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                    use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                    clean_txt=clean_txt)

    if dataset_name == 'pan2020_15':
        dataset = Pan2020_15_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                     use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                     clean_txt=clean_txt)

    if dataset_name == 'pan2020_25':
        dataset = Pan2020_25_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                     use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                     clean_txt=clean_txt)

    if dataset_name == 'cola':
        dataset = Cola_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                clean_txt=clean_txt)

    if dataset_name == 'vua':
        dataset = Vua_Dataset(root=data_path, normal_class=normal_class, tokenizer=tokenizer,
                                use_tfidf_weights=use_tfidf_weights, append_sos=append_sos, append_eos=append_eos,
                                clean_txt=clean_txt)

    return dataset

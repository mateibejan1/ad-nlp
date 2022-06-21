import glob
import pandas as pd
import math
from os import listdir, mkdir
from os.path import isfile, join

root = '../data/'
directories = ['gutenberg_authors', 'gutenberg_categories', 'song_artists', 'song_genres', 'pan2011_mails']

for type_ in ['train', 'test']:
    for directory in directories:
        print(directory)
        files = [join(root, f) for f in listdir(join(root, directory, type_))]
        classes = [data_class.split('/')[-1].split('.')[0] for data_class in files]
        data_dict = {'label': None, 'text': None}

        for file_name in glob.glob(join(root, directory, type_, '*.txt')):
            with open(file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line != '\n':
                        if data_dict['label'] == None:
                            data_dict['label'] = [file_name.split('/')[-1].split('.')[0]]
                        else:
                            data_dict['label'].append(file_name.split('/')[-1].split('.')[0])
                        if data_dict['text'] == None:
                            data_dict['text'] = [line]
                        else:
                            data_dict['text'].append(line) 

        df = pd.DataFrame(data_dict, columns=['label', 'text'])

        print(type_)
        print(df.shape)


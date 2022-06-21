import glob
import pandas as pd
import math
from os import listdir, mkdir
from os.path import isfile, join

root = '../data/'
directories = ['pan2011_mails']
# directories = ['gutenberg_authors', 'gutenberg_categories', 'song_artists', 'song_genres', 'pan2011_mails']

for directory in directories:
    files = [join(root, f) for f in listdir(join(root, directory))]
    classes = [data_class.split('/')[-1].split('.')[0] for data_class in files]
    data_dict = {'label': None, 'text': None}

    for file_name in glob.glob(join(root, directory, '*.txt')):
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

    selected_dfs = {}

    for curr_class in classes:
        selected_dfs[curr_class] = df[df['label'] == curr_class].sample(math.ceil(df[df['label'] == curr_class].shape[0] * 0.2))

    df_test = pd.DataFrame(columns=['label', 'text'])

    for key, value in selected_dfs.items():
        df_test = df_test.append(value)
        df = df.drop(list(value.index))

    df_train = df

    print(directory)
    print('train', df_train.shape)
    print('test', df_test.shape)

    mkdir(join(root, directory, 'train'))
    for curr_class in classes:
        df_curr_class = df_train[df_train['label'] == curr_class]
        with open(join(root, directory, 'train', curr_class + '.txt'), 'a', encoding="utf8", errors='ignore') as f:
            for key, row in df_curr_class.iterrows():
                f.write(row['text'])
                f.write('\n\n')

    f.close()

    mkdir(join(root, directory, 'test'))

    for curr_class in classes:
        df_curr_class = df_test[df_test['label'] == curr_class]
        with open(join(root, directory, 'test', curr_class + '.txt'), 'a', encoding="utf8", errors='ignore') as f:
            for key, row in df_curr_class.iterrows():
                f.write(row['text'])
                f.write('\n\n')

    f.close()
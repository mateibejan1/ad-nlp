import os

dirs = ['gutenberg_authors', 'gutenberg_categories', 'song_genres', 'vua', 'cola']

for dir in dirs:
    for split in ['train', 'test']:
        wildcard = "./data/" + dir + '/'+ split
        total_sample_count = 0
        for file_name in os.listdir(wildcard):
            file_name = wildcard + "/" + file_name
            file = open(file_name, 'r')
            lines = file.readlines()
            total_sample_count += len(lines) / 3
            # print(file_name, len(lines) / 3)
        print(dir, split, total_sample_count)
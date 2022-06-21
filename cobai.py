from os import listdir
from os.path import isfile, join

root = './data/gutenberg_authors'

files = [join(root, f) for f in listdir(join(root, 'train')) if isfile(join(root, 'train',f))]
classes = [data_class.split('/')[-1].split('.')[0] for data_class in files]

print(files)
print()
print(classes)
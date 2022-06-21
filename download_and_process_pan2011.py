import os
import pandas as pd
import requests

# url = 'https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz'
# filename = url.split("/")[-1]
# with open(filename, "wb") as f:
#     r = requests.get(url)
#     f.write(r.content)

# os.system('tar xvzf enron_mail_20150507.tar.gz')

dirs = [name for name in os.listdir('./maildir/')]
dirs.sort()
subdirs = ['_sent_mail', 'sent', 'sent_items']

df_mails = pd.DataFrame(columns=['Author', 'Directory', 'Content'])

for dir in dirs:
    print(dir)
    for subdir in subdirs:
        if subdir in os.listdir('./maildir/' + dir):
            for name in os.listdir('./maildir/' + dir + '/' + subdir):
                if os.path.isfile('./maildir/' + dir + '/' + subdir + '/' + name):
                    with open('./maildir/' + dir + '/' + subdir + '/' + name, 
                            'r', encoding="utf8", errors='ignore') as f:
                        data = f.read()
                        text = ''.join(data.split('X-FileName:')[1].split('\n')[1:])
                        text = ' '.join(' '.join(' '.join(text.split('\n')).split('\t')).split('\r'))
                        if len(text.split(' ')) > 128:
                            df_mails = df_mails.append({'Author': dir, 
                                                        'Directory': subdir,
                                                        'Content': text}, 
                                                    ignore_index=True)

f = open('all_english_words.txt', 'r')
all_words = [word.strip() for word in f.readlines()]
f.close()

def clean_mail(row):    
    cleaned_row = []
    for token in row['Content'].split(' '):
        if token.lower() in all_words:
            cleaned_row.append(token.lower())
    return ' '.join(cleaned_row)

def sample_data(df):
    df_sample = pd.DataFrame(columns = ['Author', 'Directory', 'Content']) 
    authors = ['kaminski-v', 'mann-k', 'dasovich-j', 
               'shackleton-s', 'beck-s', 'germany-c', 'jones-t']
    selected_dfs = {}
    for author in authors:
        if df[df['Author'] == author].shape[0] > 2000:
            selected_dfs[author] = df[df['Author'] == author].sample(2000)
        else:
            selected_dfs[author] = df[df['Author'] == author]
    for author in authors:
        for key, value in selected_dfs[author].items():
            df_sample = df_sample.append(value)
    return df_sample

df_mails_select = sample_data(df_mails)

df_mails_select['Clean Content'] = df_mails_select.apply(clean_mail, axis=1)

authors = ['kaminski-v', 'mann-k', 'dasovich-j', 
           'shackleton-s', 'beck-s', 'germany-c', 'jones-t']

for author in authors:
    df = df_mails_select[df_mails_select['Author'] == author]
    filename = '_'.join(author.split('-'))
    f = open(filename + '.txt', 'a') 
    for key, row in df.iterrows():
        lyrics = str(row['Clean Content']).lower()
        f.write(' '.join(lyrics.split('\n')))
        f.write('\n\n')
    f.close()
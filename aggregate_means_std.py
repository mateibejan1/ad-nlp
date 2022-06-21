import glob
from statistics import mean, stdev

directories = ['./baselines_results/oc-svm',
                './baselines_results/isoforest',
               '../cvdd_log']

song_genres_classes = ['1_Pop', '3_Hip-Hop', '4_Electronic', '0_Indie', '8_Rock', '2_Metal', '5_Country', '6_Folk', '9_Jazz']
gutcat_classes = ['4_Biology', '1_Botany', '2_CIA', '7_Canada', '0_Detective', 
                  '9_Historical', '3_Mystery', '8_Science', '5_Childrens', '6_Harvard']
gutaut_classes = ['1_Arthur_Conan_Doyle', '0_Charles_Dickens', '3_Charles_Darwin', '2_Mark_Twain', '6_Edgar_Allan_Poe', 
                  '4_Walter_Scott', '7_United_States', '9_H', '8_L', '5_Agatha_Christie']
vua_classes = ['0_1', '1_0']
cola_classes = ['0_1', '1_0']
newsgroups20_classes = ['0_rec', '1_sci', '2_misc', '3_pol', '4_rel', '5_comp']
agnews_classes = ['0_business', '1_sports', '2_sci', '3_world']
datasets_dict ={'song_genres': song_genres_classes, 'gutenberg_categories': gutcat_classes,
                'gutenberg_authors': gutaut_classes, 'vua': vua_classes, 'cola': cola_classes,
                'newsgroups20': newsgroups20_classes, 'agnews': agnews_classes}

aggres_dict_auroc = {}
aggres_dict_auprin = {}
aggres_dict_auprout = {}

datasets = ['song_genres', 'gutenberg_categories', 'gutenberg_authors', 'cola', 'vua', 'newsgroups20', 'ag_news']

for directory in directories:
    if directory == '../cvdd_log':
        for dataset in datasets + ['ag_news']:
            fullpath = directory + '/' + dataset + '/log.txt'

            if fullpath not in aggres_dict_auroc:
                aggres_dict_auroc[fullpath] = []
            if fullpath not in aggres_dict_auprin:
                aggres_dict_auprin[fullpath] = []
            if fullpath not in aggres_dict_auprout:
                aggres_dict_auprout[fullpath] = []

            with open(fullpath, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'root - INFO - Test AUC:' in line:
                        aggres_dict_auroc[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
                    elif 'root - INFO - Test AUPR-In:' in line:
                        aggres_dict_auprin[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
                    elif 'root - INFO - Test AUPR-Out:' in line:
                        aggres_dict_auprout[fullpath].append(float(line.split(':')[-1].strip()[:-1]))

    for dataset in datasets:
        fullpath = directory + '/' + dataset + '/'
        
        if fullpath not in aggres_dict_auroc:
            aggres_dict_auroc[fullpath] = []
        if fullpath not in aggres_dict_auprin:
            aggres_dict_auprin[fullpath] = []
        if fullpath not in aggres_dict_auprout:
            aggres_dict_auprout[fullpath] = []

        for file in glob.glob(fullpath + '/*.txt'):
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'Test AUC:' in line:
                        aggres_dict_auroc[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
                    elif 'Test AUPR-In:' in line:
                        aggres_dict_auprin[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
                    elif 'Test AUPR-Out:' in line:
                        aggres_dict_auprout[fullpath].append(float(line.split(':')[-1].strip()[:-1]))

for fullpath in glob.glob('../log_date/*.txt'):
    if fullpath not in aggres_dict_auroc:
        aggres_dict_auroc[fullpath] = []
    if fullpath not in aggres_dict_auprin:
        aggres_dict_auprin[fullpath] = []
    if fullpath not in aggres_dict_auprout:
        aggres_dict_auprout[fullpath] = []
    with open(fullpath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'ROC' in line:
                aggres_dict_auroc[fullpath].append(float(line.split(':')[-1].strip()))
            elif 'AUPR-IN' in line:
                aggres_dict_auprin[fullpath].append(float(line.split(':')[-1].strip()))
            elif 'AUPR-OUT' in line:
                aggres_dict_auprout[fullpath].append(float(line.split(':')[-1].strip()))

print(aggres_dict_auroc)
print()
print()
print(aggres_dict_auprin)
print()
print()
print(aggres_dict_auprout)
print()
print()

with open('auroc_results.txt', 'a') as f:
    for key, value in aggres_dict_auroc.items():
        f.write(key + ' ' + str(round(mean(value), 1)) + ' $\pm$ ' + str(round(stdev(value), 1)) + '\n\n')

with open('auprin_results.txt', 'a') as f:
    for key, value in aggres_dict_auprin.items():
        f.write(key + ' ' + str(round(mean(value), 1)) + ' $\pm$ ' + str(round(stdev(value), 1)) + '\n\n')

with open('auprout_results.txt', 'a') as f:
    for key, value in aggres_dict_auprout.items():
        f.write(key + ' ' + str(round(mean(value), 1)) + ' $\pm$ ' + str(round(stdev(value), 1)) + '\n\n')

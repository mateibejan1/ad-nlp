import glob
from statistics import mean, stdev

aggres_dict_auroc = {}
aggres_dict_auprin = {}
aggres_dict_auprout = {}

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
            if 'ROC-AUC:' in line:
                aggres_dict_auroc[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
            elif 'PR-AUC-in:' in line:
                aggres_dict_auprin[fullpath].append(float(line.split(':')[-1].strip()[:-1]))
            elif 'PR-AUC-out:' in line:
                aggres_dict_auprout[fullpath].append(float(line.split(':')[-1].strip()[:-1]))


#DATE 63.3
#CVDD 64.3
#if 63.2
#ocsvm64.9
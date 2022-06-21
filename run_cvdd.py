from os import system, mkdir, listdir
from os.path import join, isfile, exists
import glob

if not exists('./dl_results/'):
    mkdir('./dl_results/')

for method in ['cvdd_Net']:
    if not exists('./dl_results/{}'.format(method)):
        mkdir('./dl_results/{}'.format(method))
    for dataset in ['ag_news', 'newsgroups20', 'cola', 'vua', 'gutenberg_authors', 'gutenberg_categories', 'song_genres']: 
        mkdir('./dl_results/{}/{}'.format(method, dataset))
        files = [join(join('./data/{}'.format(dataset)), f) for f in listdir(join('./data/{}'.format(dataset), 'train')) if isfile(join('./data/{}/train'.format(dataset), f))]
        for curr_class_id in range(len(files)):
            curr_class = files[curr_class_id].split('.')[1].split('/')[-1]
            if curr_class == 'R&B':
                curr_class = 'RB'
            if curr_class == "Children's":
                curr_class = 'Childrens'
            print(curr_class_id, curr_class)
            mkdir('./dl_results/{}/{}/{}'.format(method, dataset, '_'.join([str(curr_class_id), curr_class])))
            for pretrained_model in ['GloVe_6B']:
                    cmd_str = """nohup python main.py {} {} \
                                ../cvdd_log/{}/ ./data/{}/ \
                                --seed 1 --clean_txt \
                                --embedding_size 300 --pretrained_model {} \
                                --normal_class {} > ./dl_results/{}/{}/{}/{}"""\
                                .format(dataset, method, dataset, dataset, pretrained_model, curr_class_id,
                                        method, dataset, '_'.join([str(curr_class_id), curr_class]),
                                        '_'.join([method, dataset, curr_class, pretrained_model, '.txt']))
                    system(cmd_str)

            results = []
            for file in glob.glob(join('./dl_results/{}/{}/{}'.format(method, dataset, '_'.join([str(curr_class_id), curr_class])), '*.txt')):
                hyperparam_data = {}
                with open(file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:  
                        if 'INFO:root:Word vector embedding size:' in line:
                            hyperparam_data['embedding_size'] = line.split(':')[-1].strip()
                        elif 'INFO:root:Load pre-trained word vectors:' in line:
                            hyperparam_data['pre-trained word vectors'] = line.split(':')[-1].strip()
                        elif 'INFO:root:OC-SVM kernel:' in line:
                            hyperparam_data['OC-SVM kernel'] = line.split(':')[-1].strip()
                        elif 'INFO:root:Nu-paramerter' in line:
                            hyperparam_data['Nu-paramerter'] = line.split(':')[-1].strip()
                        elif 'INFO:root:Test AUC:' in line:
                            hyperparam_data['Test AUC'] = line.split(':')[-1].strip()
                        elif 'INFO:root:Test AUPR-In:' in line:
                            hyperparam_data['Test AUPR-In'] = line.split(':')[-1].strip()
                        elif 'INFO:root:Test AUPR-Out:' in line:
                            hyperparam_data['Test AUPR-Out'] = line.split(':')[-1].strip()
                results.append(hyperparam_data)

            max_auc, best_hyperparams = -1, None
            for result in results:
                if 'Test AUC' in result.keys() and float(result['Test AUC'][:-1]) > max_auc:
                    best_hyperparams = result

            if best_hyperparams != None:
                with open('./dl_results/{}/{}/best_{}_cvdd.txt'.format(method, dataset, '_'.join([str(curr_class_id), curr_class])), 'a') as f:
                    for key, value in best_hyperparams.items():
                        f.write(key)
                        f.write(': ')
                        f.write(value)
                        f.write('\n\n')
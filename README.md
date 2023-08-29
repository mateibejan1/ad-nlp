# AD-NLP
 A Benchmark for Anomaly Detection in Natural Language Processing
 
To reproduce our experiments, you must clone the repository, download the data and then run the provided Python scripts, as explained below.
 
To download the preprocessed data, run the `download_data.sh` script. It will pull the data from Google Drive and unzip it in the current directory. Althernatively, you can download the data manually at the following links: 

* Google Drive: https://drive.google.com/file/d/1-Qo-kcGnPvmvh33DDQn4yw_MlD2-28kV/view?usp=sharing.
* Zenodo: https://zenodo.org/record/7007980#.Yv6gyGFBx2U.

To redo our experiments, you must download the data and then run the following Python scripts:

1. `run_baselines.py`, which trains and tests both OCSVM and Isolation Forest.
2. `run_cvdd.py`, which trains and tests CVDD.
3. `some_script.py`, to be added by Andrei.

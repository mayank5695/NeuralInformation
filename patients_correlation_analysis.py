_Author_ = 'Mayank Yadav'
"""
Correlation of patient data with corresponding graph measures. Ignore the patients with -1 subject for each of graph measures.
"""
import pandas as pd
import numpy as np
folder_name = 'patient_data/'


def correlation_analysis(data_file,parcellation):
    """

    :param data_file: each parcellation patient file
    :return: correlation for both the patient behaviour data
    """
    data = pd.read_csv(data_file, delimiter=',', index_col=None)
    # get index for -1 so that it can be removed from analysis
    indexes = data.loc[data['Subject'] == -1].index.values

    data = data.drop(data.index[indexes]).reset_index(drop=True)

    measures = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                'clustering_coef', 'fiedler_value']
    measure_folder='measures/'

    for measure in measures:
        graph_data=pd.read_csv(measure_folder+measure+'.csv',delimiter=',',index_col=None)
        graph_data=graph_data[parcellation]
        graph_data = graph_data.drop(graph_data.index[indexes]).reset_index(drop=True)
        graph_data=graph_data.dropna()

        #Now do correlation for patient data and graph_data


        PSQI_data=data['PSQI_Score']
        List_sort=data['ListSort_AgeAdj']
        psqi_corr=np.corrcoef(PSQI_data.values,graph_data.values)
        list_corr=np.corrcoef(List_sort.values,graph_data.values)
        print(measure)
        print('PSQI Correlation')
        print(psqi_corr)
        print('List Score correlation')
        print(list_corr)
        print('--------------')

def call_each_parcellation():
    parcellations = ['aal', 'brainnatome', 'harvard', 'mindboggle']
    parcellation=['aal']

    for parc in parcellations:
        data_file = folder_name + parc + '.csv'
        print('**************')
        print(parc)
        correlation_analysis(data_file,parc)


call_each_parcellation()

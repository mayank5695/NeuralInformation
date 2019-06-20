import pandas as pd
folder='graphValues/'
import os
def txt_to_dataframe(folder,name_parcellation):
    """
    Convert a text file to usable dataframe.
    :param file: file
    :return: dataframe with columns
    """
    column_weight = ['patients','degree', 'density', 'global_efficiency', 'transitivity', 'assortavity', 'clustering_coef',
                     'fiedler_value', 'small_worldness','Null']

    file_name=folder+name_parcellation+'.txt'
    data=pd.read_csv(file_name,header=None,delimiter=';')
    data.columns=column_weight
    data=data.drop(['Null'],axis=1)
    return data

def get_graph_measure_parcellation(graph_name):
    """

    :param graph_name: the name of graph measure for all parcellation
    :return: dataframe with all patient value of each graph measure for all parcellations and save to a file to use later.
    """
    graphFolder='measures'
    name=['aal','brainnatome','harvard','mindboggle']
    graph_data = pd.DataFrame()
    for name_parcellation in name:
        data=txt_to_dataframe(folder,name_parcellation)
        data=data[graph_name]
        graph_data=graph_data.append(data)
    graph_data=graph_data.T
    graph_data.columns=name
    if not os.path.exists(graphFolder):
        os.mkdir(graphFolder)

    graph_data.to_csv(graphFolder+'/'+graph_name+'.csv',index=None)


def create_all_measures():
    measures = ['patients', 'degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                     'clustering_coef','fiedler_value']
    for measure in measures:
        get_graph_measure_parcellation(measure)


if __name__ == "__main__":
    create_all_measures()
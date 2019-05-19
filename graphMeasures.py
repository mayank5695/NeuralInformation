import scipy.io as sio
import h5py
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

file='SC_matrices/100307/aal90/DTI_CM.mat'


def dataImport(data):
    """

    :param data: The file .mat file which contains association matrix between nodes of each parcellation scheme
    :return: The numpy array of .mat file
    """
    array={}
    data=h5py.File(data)
    for k,v in data.items():
        array[k]=np.array(v)

    array=array['DTI_CM']
    return array

def convertMatrixtoGraph(arr):
    """
    Function returns the matrix to be in graph form which can be used for graph measures.
    :param arr: Adjacency matrix
    :return: networkX graph
    """
    gr=nx.MultiGraph(arr)
    nx.draw(gr)
    plt.show()
    return gr

def getDegree(graph):
    """

    :param graph: The graph of particular parcellation scheme
    :return: degreee of each node of the graph
    """
    degree=[]
    for i in range(0,len(G.nodes)):
        degree.append(G.degree[i])
    return degree

if __name__ == '__main__':

    array=dataImport(file)
    G = convertMatrixtoGraph(array)
    #add weight
    print(G.get_edge_data(*(0,0)))
    #print(len(G.nodes))
    deg=getDegree(G)
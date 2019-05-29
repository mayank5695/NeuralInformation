"""
@author : Mayank Yadav
@project : Neural Information Processing project
Graph measures for different parcellation schemes
Graph measures :
                -Degree -DONE
                -Shortest path length - TODO
                -Number of Triangles -DONE
                -Global Efficiency -DONE
                - Transitivity -DONE
                - Modularity-DONE
                - Navigation(from sites.google.com link) -TODO
                - Resilience -TODO
                - Characteristics Path  length (Average shortest path length) -TODO
                - Quasi Idempotence - TODO
                - Community delts
                - Measure of network small wordness.
                - Fiedel value -DONE
                - Randic index (a=1 , assortativity coefficient of graph) -DONE


"""

import h5py
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import community
file = 'SC_matrices/100307/aal90/DTI_CM.mat'
file_len='SC_matrices/100307/aal90/DTI_LEN.mat'

def data_import(data):
    """

    :param data: The file .mat file which contains association matrix between nodes of each parcellation scheme
    :return: The numpy array of .mat file
    """
    array = {}
    data = h5py.File(data)
    for k, v in data.items():
        array[k] = np.array(v)
    array = array['DTI_CM']

    for i in range(0,array.shape[0]):
        array[i][i]=0

    array=array.astype(int)
    return array


def convert_matrix_to_graph(arr):
    """
    Function returns the matrix to be in graph form which can be used for graph measures.
    We use multigraph because adjacency matrix contains a self loop.
    :param arr: Adjacency matrix
    :return: networkX graph
    """
    gr = nx.Graph(arr)
    # nx.draw(gr)
    # plt.show()
    return gr


def convert_node_float_to_integer(graph):
    """
    Convert the node weights from float to integer.
    :param graph: undirected weighted graph
    :return:
    """
    return 'you'


def get_degree(Graph):
    """

    :param graph: The graph of particular parcellation scheme
    :return: degreee of each node of the graph
    """
    degree = []
    for i in range(0, len(Graph.nodes)):
        degree.append(Graph.degree[i])
    return degree

def get_shortest_path_length(graph):
    """
    TODO
    :param graph: undirected weighted graph
    :return:
    """
    if (nx.is_connected(G)):
        len_path = dict(nx.all_pairs_dijkstra(graph))
    print(len_path)


def number_triangles(graph):
    """
    If a graph is triangle free then trace of A^3 will be 0 where A is the adjacency matrix.
    A graph is only triangle if it is complete graph.

    :param graph: undirected weighted graph
    :return:
    """
    triangle_per_node = []

    for i in range(len(graph.nodes)):
        triangle_per_node.append(nx.triangles(graph, i))
    return triangle_per_node


def global_efficiency_graph(graph):
    """
    It ignores the weights of the edge to calculate global efficiency.
    Returns the average global efficiency of the graph.

    The *efficiency* of a pair of nodes in a graph is the multiplicative
    inverse of the shortest path distance between the nodes. The *average
    global efficiency* of a graph is the average efficiency of all pairs of
    nodes.

    :param graph: undirected weighted graph
    :return:
    """
    return nx.global_efficiency(graph)


def transitivity(graph):
    """
    Compute graph transitivity, the fraction of all possible triangles
    present in G.

    Possible triangles are identified by the number of "triads"
    (two edges with a shared vertex).

    :param graph: undirected weighted graph
    :return: transitivity
    """
    return nx.transitivity(graph)


def assortativity(graph):
    """
    Compute degree assortativity of graph.

    Assortativity measures the similarity of connections
    in the graph with respect to the node degree.

    :param graph: undirected weighted graph
    :return: degree assortativity and peasrson assortativitity of graph
    """
    return (nx.degree_assortativity_coefficient(graph, weight='weight'), nx.degree_pearson_correlation_coefficient(graph,weight='weight'))

def modularity(graph):
    """
    FInd communities in graph using Clauset-Newman-Moore greedy modularity maximization. Does not consider 'EDGE WEIGHTS'
    :param graph: Undirected weighted graph
    :return: list of modularity

    NOT MAKE SENSE FOR THE GRAPH SO FAR. (To ask) Can count the communities. Will it make sense?

    """
    comm= nx.algorithms.community.asyn_lpa_communities(graph,weight='weight')
    for i in comm:
        print(i)
    print('HOLLA')
    for j in  nx.algorithms.community.asyn_fluidc(G,k=15):
        print(j)

def fiedler_value(graph):
    """
    The Fiedler value, or algebraic connectivity, was introduced by Fiedler in 1973 and
    can be thought of as a measure of network robustness (Fiedler, 1973). The Fiedler value is equal
     to the second-smallest eigenvalue of the Laplacian matrix. The second smallest eigenvalue is used
     as it can be proven that the smallest eigenvalue of the Laplacian is always zero (Fiedler, 1973).
    The Laplacian matrix combines both degree information and connectivity information in the same matrix.

    :param graph: undirected weighted graph
    :return: second smallest eigen value
    """
    return np.sort(nx.laplacian_spectrum(graph,weight='weight'))[1]

def small_wordness_sigma(graph):
    """
    Returns the small-world coefficient (sigma) of the given graph.

    The small-world coefficient is defined as: sigma = C/Cr / L/Lr where
    C and L : the average clustering coefficient and average shortest path length of G.
    Cr and Lr :the average clustering coefficient and average shortest path length of an equivalent random graph.

    A graph is commonly classified as small-world if sigma>1.

    :param graph: undirected graph
    :return: sigma value

    """
    return nx.algorithms.sigma(graph)

if __name__ == '__main__':

    adjacency = data_import(file)
    #length_matrix=data_import(file_len)
    G = convert_matrix_to_graph(adjacency)
    #print(G.get_edge_data(*(2,1)))
    print(small_wordness_sigma(G))


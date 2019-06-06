"""
@author : Mayank Yadav
@project : Neural Information Processing project
Graph measures for different parcellation schemes
Graph measures :
                -Degree -DONE
                - Density - DONE
                -Number of Triangles -DONE
                -Global Efficiency -DONE
                - Transitivity -DONE
                - Modularity-DONE, Updated, TODO again.
                - Clustering Coefficient - Done
                - Navigation(from sites.google.com link) -TODO
                - Resilience -Done but TODO (not sure how to do degree distribution) Can make a graph. Is that enough?
                - Characteristics Path  length (Average shortest path length) - Done
                - Quasi Idempotence - TODO Still needed
                - Measure of network small wordness. - Done
                - Fiedel value - DONE
                - Randic index (a=1 , assortativity coefficient of graph) - DONE
                - Eigen vector centrality - Done
                - Edge between centrality - Done
                - Betweeness Centrality - Done


"""
import collections
import h5py
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
import community

def data_import(data,name):
    """

    :param data: The file .mat file which contains association matrix between nodes of each parcellation scheme
    :return: The numpy array of .mat file
    """

    array = {}
    data = h5py.File(data)
    for k, v in data.items():
        array[k] = np.array(v)
    array = array[name]

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

def get_density(graph):
    """
    The density for undirected graphs is

        𝑑=2𝑚/𝑛(𝑛−1),
    The density is 0 for a graph without edges and 1 for a complete graph.

    :param graph: undirected weighted graph
    :return: density
    """
    return nx.density(graph)

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
    return (nx.degree_assortativity_coefficient(graph, weight='weight'))

def modularity(graph):
    """
    FInd communities in graph using Clauset-Newman-Moore greedy modularity maximization. Does not consider 'EDGE WEIGHTS'
    :param graph: Undirected weighted graph
    :return: list of modularity

    NOT MAKE SENSE FOR THE GRAPH SO FAR. (To ask) Can count the communities. Will it make sense?
    Now given all the modules, find the modularity. TODO

    """
    modularity_matrix = nx.modularity_matrix(graph_weight, weight='weight')



def clustering_coefficient(graph):
    """
    This function finds an approximate average clustering coefficient for G by repeating n times (defined in trials)
    the following experiment: choose a node at random, choose two of its neighbors at random, and check
    if they are connected.
    The approximate coefficient is the fraction of triangles found over the number of trials which
    in this case is 1000 as default.

    :param graph: undirected weighted graph
    :return: average clustering coefficient

    """
    return nx.algorithms.average_clustering(graph)

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
    :return: None

    """
    return nx.algorithms.sigma(graph)

def degree_distribution(graph):
    """
    Create a histogram of degree distribution

    :param graph: weighted undirected graph
    :return: return histogram
    Not know how to use it.

    ALREADY HAVE PDF, FIND CDF.

    """
    degree_sequence = sorted([d for n, d in graph.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    Gcc = sorted(nx.connected_component_subgraphs(graph), key=len, reverse=True)[0]
    pos = nx.spring_layout(graph)
    plt.axis('off')
    nx.draw_networkx_nodes(graph, pos, node_size=20)
    nx.draw_networkx_edges(graph, pos, alpha=0.4)

    plt.show()

def characteristic_path_length(graph):
    """
    Average shortest path length in a graph. The weight here is treated as the length of the graph.

    :param graph: adjcency matrix with length as weights.
    :return: average shortest path
    """
    return nx.average_shortest_path_length(graph,weight='weight')

def eigen_vector_centrality(graph):
    """
    Compute the eigenvector centrality for the graph G.

    Eigenvector centrality computes the centrality for a node based on the centrality of its neighbors.
    :param graph: undirected weighted graph
    :return: dictionary of eigen vector centrality for each node.
    """
    return nx.eigenvector_centrality_numpy(graph,weight='weight')

def edge_betweeness_centrality(graph):
    """

    :param graph:
    :return: dictionary
    """

    return nx.edge_betweenness_centrality(graph,k=math.floor(math.sqrt(len(graph.nodes))),weight='weight')

def betweeness_centrality(graph):
    """
    Use brandes algorithm

    :param graph:
    :return:
    """
    return nx.betweenness_centrality(graph,k=math.floor(math.sqrt(len(graph.nodes))),weight='weight')



def graph_function_calling(adjacency_file,length_file):

    adjacency = data_import(adjacency_file,'DTI_CM')
    np.savetxt('adj.csv',adjacency,delimiter=',')
    length_matrix=data_import(length_file,'DTI_LEN')
    graph_weight = convert_matrix_to_graph(adjacency)
    graph_len = convert_matrix_to_graph(length_matrix)


    #ONE VALUE FOR EACH NODE
    degree_per_node=get_degree(graph_weight)
    triangle_per_node = number_triangles(graph_weight)

    #ONE VALUE FOR GRAPH

    density=get_density(graph_weight)
    average_global_efficiency=global_efficiency_graph(graph_weight)
    transitivity_graph=transitivity(graph_weight)
    degree_assortavity=assortativity(graph_weight)
    average_clustering=clustering_coefficient(graph_weight)
    fiedler_graph=fiedler_value(graph_weight)
    #smallWorldness=small_wordness_sigma(graph_weight) #takes a lot of time, computation cost high
    smallWorldness=0
    average_path_length=characteristic_path_length(graph_len)

    value_lst=[density,average_global_efficiency,transitivity_graph,degree_assortavity,average_clustering,fiedler_graph,smallWorldness,average_path_length] #please do not interchange

    return value_lst
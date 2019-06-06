#NOT USED YET

import h5py
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

def data_import(data, name):
    """

    :param data: The file .mat file which contains association matrix between nodes of each parcellation scheme
    :return: The numpy array of .mat file
    """

    array = {}
    data = h5py.File(data)
    for k, v in data.items():
        array[k] = np.array(v)
    array = array[name]

    for i in range(0, array.shape[0]):
        array[i][i] = 0

    array = array.astype(int)
    return array

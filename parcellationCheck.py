import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def adjacent_placed_nodes(matrix):
    """
    The matrix is written in form :
    LRLR
    :return: (left,right,sum)
    """
    left=0
    right=0
    sum=0
    for i in range(0,matrix.shape[0]-1,2):
        for j in range(0,matrix.shape[1]-1,2):
            left+=matrix[i][j]
            right+=matrix[i+1][j+1]
    sum=np.sum(matrix)
    return ([left,right,sum])

def cluster_placed_nodes(matrix):
    """
    LLLLLRRRR placed nodes
    Mindboggle and Schaefer parcellation only
    :return:
    """
    left = 0
    right = 0

    for i in range(0, (int)(matrix.shape[0]/2)):
        for j in range(0,(int)(matrix.shape[1]/2)):
            left+=matrix[i][j]
            right+=matrix[i+((int)(matrix.shape[1]/2))][j+((int)(matrix.shape[1]/2))]
    sum=np.sum(matrix)
    return([left,right,sum])


#creating graphs
def create_graph(matrix,name):
    matrix=np.array(matrix)
    left=matrix[:,0]
    right=matrix[:,1]
    sum=matrix[:,2]
    if(name=='AAL' or name=='AAL_length' or name=='Schaefer_length'):
        x_value=np.arange(1,40,1)
    else:
        x_value=np.arange(1,41,1)
    plt.plot(x_value, left, 'rs--',label='left hem.')
    plt.plot(x_value, right, 'bs--',label='right hem.')
    plt.plot(x_value, sum, 'g^--',label='total')
    plt.title(name)
    plt.xlabel('Participants')
    plt.ylabel('Connectivity_Strength')
    plt.legend(loc=0)
    plt.legend()
    name=name+'.png'
    plt.savefig(name,bbox_inches='tight')
    plt.clf()


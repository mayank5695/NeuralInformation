import seaborn as sns
import matplotlib.pyplot as plt
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import numpy as np
import pandas as pd
import matplotlib
import os
matplotlib.use('agg') #to save in png

folder='measures/'

nodes=[62,90,111,246] #inorder [AAL,brainnatome,harvard,mindboggle]
node_initial=[90,246,111,62]
def fetch_the_measure(name):
    data=pd.read_csv(folder+name+'.csv',delimiter=',')

    return data


#create the box plot for each

def create_box_plot(name):
    """
    :param name: measure for box plot
    :return:
    """
    graphFolder='visual_graphs_new'
    parcellation = ['mindboggle','aal90', 'harvard', 'brainnatome']
    data=fetch_the_measure(name)
    array=data.values
    for i in range(0,4):
        array[:,i]=array[:,i]/node_initial[i]

    data_to_plot=[array[:,3],array[:,0],array[:,2],array[:,1]]
    data_mean = [np.mean(array[:, 3]), np.mean(array[:, 0]), np.mean(array[:, 2]), np.mean(array[:, 1])]


    #do correlation

    corr=np.corrcoef(data_mean,nodes)
    fig = plt.figure(1, figsize=(9, 6))

    #Create an axes instance
    ax = fig.add_subplot(111)
    ax.plot(list(range(1,5)),data_mean,'b',linewidth=1)
    ax.legend(['mean of parcellations'])
    # Create the boxplot
    bp = ax.boxplot(data_to_plot,notch=True )
    ax.set_xticklabels(parcellation)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.ylabel(name)
    plt.tight_layout()
    plt.xlabel('Parcellation scheme in order of increasing nodes')
    if not os.path.exists(graphFolder):
        os.mkdir(graphFolder)
    plt.savefig(graphFolder+'/'+name+'.png',bbox_inches='tight')
    plt.clf()
    return corr

if __name__ == "__main__":
    measures = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                'clustering_coef', 'fiedler_value']
    lst_name=[]
    lst=[]
    for m in measures:
        cor=create_box_plot(m)
        lst_name.append(m)
        lst.append(cor)

    col=['measures','correlation_array']
    df=pd.DataFrame({col[0]:lst_name})
    df[col[1]]=lst
    df.to_csv('correlation_new.csv',index=None)


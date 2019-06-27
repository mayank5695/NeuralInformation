import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pingouin import ancova
from statsmodels.stats.multicomp import pairwise_tukeyhsd,MultiComparison
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
from statsmodels.formula.api import ols

measures = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                'clustering_coef', 'fiedler_value','length']

parcellation_node_dict={'aal':90,'brainnatome':246,'harvard':110,'mindboggle':62}

parcellation_dict={'aal':1,'brainnatome':2,'harvard':3,'mindboggle':4}


def update_mean(data,parc,total_val):
    mean_node=0
    mean_parc=0
    for i in range(0,len(data)):
        mean_node+=data[i]*parcellation_node_dict[parc[i]]
        mean_parc+=data[i]*parcellation_dict[parc[i]]
    mean_node=mean_node/total_val
    mean_parc=mean_parc/total_val

    return [mean_node,mean_parc]




def update_data(data,name):

    column = 'graph_values'
    data=data[data[name]>-1000]
    data=data[name]
    dat=pd.DataFrame({column:data})
    #adding the parcellation_node_value
    nodes = [parcellation_node_dict[name]]*data.shape[0]
    parc= [parcellation_dict[name]]*data.shape[0]
    dat['parcellation']=pd.Series(parc)
    dat['nodes']=pd.Series(nodes)
    return dat

def final_data(data):
    parcellation = ['mindboggle', 'aal', 'harvard', 'brainnatome']
    column = ['graph_values', 'parcellation', 'nodes']
    brain = update_data(data,parcellation[3])
    aal=  update_data(data,parcellation[1])
    mind=update_data(data,parcellation[0])
    harvard= update_data(data,parcellation[2])


    count_list=[mind.count()[0],aal.count()[0],harvard.count()[0],brain.count()[0]]



    final_data_parcel=aal
    final_data_parcel=final_data_parcel.append(brain,ignore_index=True)
    final_data_parcel=final_data_parcel.append(mind,ignore_index=True)
    final_data_parcel=final_data_parcel.append(harvard,ignore_index=True)
    mean_values=update_mean(count_list, parcellation,final_data_parcel.count()[0])

    return (final_data_parcel,mean_values)


for i in range(0,1):

    print(' ')
    print(measures[i])

    data=pd.read_csv('measures/'+measures[i]+'.csv',delimiter=',')

    data=data.fillna(-1000)
    data_updated,mean_val = final_data(data)

    formula = 'graph_values ~ nodes + parcellation'
    lm = ols(formula, data_updated).fit()
    aov_table=sm.stats.anova_lm(lm,typ=2,robust='hc3')

    print(aov_table)
    print(' ')
    print(lm.summary())
    param=lm.params
    """
    param[0]= intercept , param[1] is coef of node, param[2] is  coef_of_parcellation
    now applying formula:
    Y_adj=Y_initial - param[1](node_init- node_mean) - param[2](parcellation_init - parcellation_mean)
    """
    print(mean_val[0])
    print(mean_val[1])
    adjusted_y=[]
    for i in range(0,data_updated.count()[0]):
        adjusted_y_val=data_updated['graph_values'].iloc[i]-param[1]*(data_updated['nodes'].iloc[i]-mean_val[0])
        adjusted_y.append(adjusted_y_val)

    data_updated['adjusted_y']=pd.Series(adjusted_y)

    formula = 'adjusted_y ~ nodes + parcellation'
    lm = ols(formula, data_updated).fit()
    aov_table = sm.stats.anova_lm(lm, typ=2, robust='hc3')

    print(aov_table)
    print(' ')
    print(lm.summary())



    #print(lm.model.data.orig_exog[:5])
    #infl = lm.get_influence()
    #print(infl.summary_table())




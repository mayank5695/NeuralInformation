import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pingouin import ancova
from statsmodels.stats.multicomp import pairwise_tukeyhsd,MultiComparison
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols

""""
   The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.

   1. The samples are independent.

   2. Each sample is from a normally distributed population.

   3. The population standard deviations of the groups are all equal. This property is known as homoscedasticity.

"""
measures = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                'clustering_coef', 'fiedler_value','length']

parcellation_node_dict={'aal':90,'brainnatome':246,'harvard':110,'mindboggle':62}

parcellation_dict={'aal':1,'brainnatome':2,'harvard':3,'mindboggle':4}

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
    final_data_parcel=aal
    final_data_parcel=final_data_parcel.append(brain,ignore_index=True)
    final_data_parcel=final_data_parcel.append(mind,ignore_index=True)
    final_data_parcel=final_data_parcel.append(harvard,ignore_index=True)

    return final_data_parcel


for i in range(0,1):

    print(' ')
    print(measures[i])

    data=pd.read_csv('measures/'+measures[i]+'.csv',delimiter=',')

    data=data.fillna(-1000)
    data_updated=final_data(data)
    #print(data_updated)
    #array=data.values
    formula = 'graph_values ~ nodes + parcellation'
    lm = ols(formula, data_updated).fit()
    print(lm.summary())

    # interX_lm = ols('graph_values ~ nodes * C(parcellation)', data=data_updated).fit()
    # print(lm.summary())
    #
    # table1 = anova_lm(lm, interX_lm)
    # print(table1)
    #print(ancova(data=data_updated, dv='graph_values', covar='nodes', between='parcellation'))




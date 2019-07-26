import numpy as np
import pandas as pd
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                         MultiComparison)
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib.pyplot import figure
from matplotlib.pyplot import text
import matplotlib.pyplot as plt
import seaborn as sns
from statsannot import add_stat_annotation
import os

measures = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity',
                'clustering_coef', 'fiedler_value','length']

Measures = ['Degree', 'Density', 'Global efficiency', 'Transitivity', 'Assortavity',
                'Clustering coefficient', 'Fiedler Value','Characteristic path length']

parcellation_node_dict={'aal':90,'brainnatome':246,'harvard':110,'mindboggle':62}

parcellation_dict={'aal':1,'brainnatome':2,'harvard':3,'mindboggle':4}


def get_data_mean(data_updated):
    data_mean=[]
    for i in range(0,4):
        aal_mean = data_updated[data_updated['parcellation'] == i+1]
        aal_mean = aal_mean['adjusted_y'].mean()
        data_mean.append(aal_mean)
    return data_mean

one_count=0
two_count=0

def get_annotation(x1,x2,data,value_hyp,p_val):
    global one_count
    global two_count

    y1=data[data['parcellation']==x1]
    y1=y1['adjusted_y'].max()

    y2=data[data['parcellation']==x2]
    y2=y2['adjusted_y'].max()
    y=max(y1,y2)

    y_trend=[0.03,0.6,0.9,1.2,1.5,1.7]
    x1=x1-1
    x2=x2-1

    if(value_hyp== False):
        col='k'
        txt='ns'
    else:
        col='r'
        if(p_val<0.01 and p_val>0.001):
            txt='*'
        else:
            txt='**'


    if(y<1 and y>0.20):
        h = 0.007
        if(x1==0):
            y=1.1*y+one_count*(h+0.004)
            one_count+=1
        elif(x1==1):
            y=1.1*y+two_count*(h+0.004)
            two_count+=1
        else:
            y=1.1*y

    elif(y<=0.20 and y>0.05):
        h = 0.009
        if (x1 == 0):
            y = 1.1 * y + one_count * (h + 0.009)
            one_count += 1
        elif (x1 == 1):
            y = 1.1 * y + two_count * (h + 0.009)
            two_count += 1
        else:
            y = 1.1 * y


    elif(y<0.05):
        h = 0.005
        if (x1 == 0):
            y = 1.1 * y + one_count * (h+0.005)
            one_count += 1
        elif (x1 == 1):
            y = 1.1 * y + two_count * (h+0.005)
            two_count += 1
        else:
            y = 1.1 * y

    elif(y<40 and y>5):
        h=0.5
        if (x1 == 0):
            y = 1.1 * y + one_count * (h+0.25)
            one_count += 1
        elif (x1 == 1):
            y = 1.1 * y + two_count * (h+0.25)
            two_count += 1
        else:
            y = 1.1 * y
    elif(y>100):
        h=5
        if (x1 == 0):
            y = 1.1 * y + one_count * (h+2)
            one_count += 1
        elif (x1 == 1):
            y = 1.1 * y + two_count * (h+2)
            two_count += 1
        else:
            y = 1.1 * y
    elif(y>40 and y<100):
        h=2
        if (x1 == 0):
            y = 1.1 * y + one_count * (h+1.0)
            one_count += 1
        elif (x1 == 1):
            y = 1.1 * y + two_count * (h+1.0)
            two_count += 1
        else:
            y = 1.1 * y

    plt.plot([x1, x1, x2-0.1, x2-0.1], [y, y + h, y + h, y], lw=1.5, c='k')
    plt.text((x1 + x2) * .5, y + h,txt, ha='center', va='bottom', color=col)



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

def statistical_measures_graph():

    global one_count
    global two_count
    graphFolder='tukey_Graph/'
    for i in range(0,len(measures)):
        one_count=0
        two_count=0


        print(' ')
        print(measures[i])

        data=pd.read_csv('measures/'+measures[i]+'.csv',delimiter=',')

        data=data.fillna(-1000)
        data_updated,mean_val = final_data(data)

        formula = 'graph_values ~ nodes + parcellation'
        lm = ols(formula, data_updated).fit()
        aov_table=sm.stats.anova_lm(lm,typ=2,robust='hc3')

        print(aov_table)
        # print(' ')
        print(lm.summary())
        param=lm.params
        """
        param[0]= intercept , param[1] is coef of node, param[2] is  coef_of_parcellation
        now applying formula:
        Y_adj=Y_initial - param[1](node_init- node_mean) - param[2](parcellation_init - parcellation_mean)
        """
        adjusted_y=[]
        for j in range(0,data_updated.count()[0]):
            adjusted_y_val=data_updated['graph_values'].iloc[j]-param[1]*(data_updated['nodes'].iloc[j]-mean_val[0])
            adjusted_y.append(adjusted_y_val)

        data_updated['adjusted_y']=pd.Series(adjusted_y)
        formula = 'adjusted_y ~ nodes + parcellation'
        lm = ols(formula, data_updated).fit()
        aov_table = sm.stats.anova_lm(lm, typ=2, robust='hc3')
        # print(aov_table)
        # print(' ')
        # print(lm.summary())
        # print(' ')

        means=get_data_mean(data_updated)
        #print(means)


        mod = MultiComparison(data_updated['adjusted_y'], data_updated['parcellation'])
        fig,ax=plt.subplots()

        Results=mod.tukeyhsd(alpha=0.05/len(measures))
        data_tukey=pd.DataFrame(data=Results._results_table.data[1:], columns=Results._results_table.data[0])
        #print(data_tukey)

        x = "parcellation"
        y = "adjusted_y"
        sns.boxplot(data=data_updated, x=x, y=y,palette='Set3')
        #sns.swarmplot(x=x, y=y, data=data_updated, color=".25")
        for j in range(0,data_tukey.count()[0]):
            value_hypothesis=data_tukey['reject'].iloc[j]
            p_val=data_tukey['p-adj'].iloc[j]
            get_annotation(data_tukey['group1'].iloc[j],data_tukey['group2'].iloc[j],data_updated,value_hypothesis,p_val)

        ax.set_xticks([0,1,2,3])
        ax.set_xticklabels(('AAL', 'BRAINETOMME', 'HARVARD', 'MINDBOGGLE'))
        ax.set(xlabel='PARCELLATIONS', ylabel=Measures[i].upper())
        #plt.show()
        if not os.path.exists(graphFolder):
            os.mkdir(graphFolder)

        plt.savefig(graphFolder + measures[i] + '.png', bbox_inches='tight',dpi=300)
        plt.clf()

statistical_measures_graph()


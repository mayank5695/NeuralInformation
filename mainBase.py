"""
TO extract values for all the classes
"""
from graphMeasures import data_import
from parcellationCheck import cluster_placed_nodes,adjacent_placed_nodes,create_graph,statistics_check
import pandas as pd
import json
import sys
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
# file = 'SC_matrices/100307/aal90/DTI_CM.mat'
# file_len='SC_matrices/100307/aal90/DTI_LEN.mat'
#
# column_names = ['density', 'global_efficiency', 'transitivity', 'assortavity', 'clustering_coef', 'fiedler_value',
#                 'small_worldness', 'average_path']
#
# all_value_graphs_one_patient_all_parcellation=[]
#
# #write next two lines in the loop to work
# values_graph=graph_function_calling(file,file_len)
# all_value_graphs_one_patient_all_parcellation.append(values_graph)
#
# pd.DataFrame(all_value_graphs_one_patient_all_parcellation,columns=column_names)

path_patients='SC_matrices/*'
patients=[]
parcellations=['aal90','Harvard Oxford Thr25 2mm Whole Brain (Makris 2006)','Mindboggle 101 - Desikan protocol (Klein 2012)','Brainnetome Atlas (Fan 2016)','AICHA (Joliot 2015)','Schaefer2018_1000Parcels_17Networks_order (Schaefer 2018)']
aal=[]
harvard=[]
mindboggle=[]
brainnetome=[]
aicha=[]
schaefer=[]
aal_len=[]
harvard_len=[]
mindboggle_len=[]
brainnetome_len=[]
aicha_len=[]
schaefer_len=[]


for dir in glob.iglob(path_patients,recursive=True):
    if os.path.isdir(dir):
        dir2=dir+'/*'
        patient=dir.strip(path_patients)
        patients.append(patient)

        for subdir in glob.iglob(dir2,recursive=True):

            parcel=subdir[len(dir)+1:]
            subdir2=subdir+'/*'

            for file in glob.iglob(subdir2,recursive=True):
                file_name=file[len(subdir)+1:]

                #AAL parcellation
                if(parcel==parcellations[0]):
                    if(file_name=='DTI_CM.mat'):
                        matrix_adj=data_import(file,'DTI_CM')
                        matrix_values=adjacent_placed_nodes(matrix_adj) #gives (left,right,sum)
                        aal.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        aal_len.append(matrix_values)

                #Harvard parcellation
                if (parcel == parcellations[1]):
                    if (file_name == 'DTI_CM.mat'):
                        matrix_adj = data_import(file, 'DTI_CM')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        harvard.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        harvard_len.append(matrix_values)

                #Mindboggle
                if (parcel == parcellations[2]):
                    if (file_name == 'DTI_CM.mat'):
                        matrix_adj = data_import(file, 'DTI_CM')
                        matrix_values = cluster_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        mindboggle.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = cluster_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        mindboggle_len.append(matrix_values)

                #brainnatome
                if (parcel == parcellations[3]):
                    if (file_name == 'DTI_CM.mat'):
                        matrix_adj = data_import(file, 'DTI_CM')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        brainnetome.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        brainnetome_len.append(matrix_values)
                #Aicha
                if (parcel == parcellations[4]):
                    if (file_name == 'DTI_CM.mat'):
                        matrix_adj = data_import(file, 'DTI_CM')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        aicha.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = adjacent_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        aicha_len.append(matrix_values)

                #Schaefer
                if (parcel == parcellations[5]):
                    if (file_name == 'DTI_CM.mat'):
                        matrix_adj = data_import(file, 'DTI_CM')
                        matrix_values = cluster_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        schaefer.append(matrix_values)
                    if (file_name == 'DTI_LEN.mat'):
                        matrix_adj = data_import(file, 'DTI_LEN')
                        matrix_values = cluster_placed_nodes(matrix_adj)  # gives (left,right,sum)
                        schaefer_len.append(matrix_values)

name=['aal','harvard','mindboggle','schaefer','aicha','brainnetome']
len='_len'

#
# create_graph(aal,'AAL')
# create_graph(aal_len,'AAL_length')
# create_graph(harvard,'Harvard')
# create_graph(harvard_len,'Harvard_length')
# create_graph(mindboggle,'Mindboggle')
# create_graph(mindboggle_len,'Mindboggle_length')
# create_graph(schaefer_len,'Schaefer_length')
# create_graph(schaefer,'Schaefer')
# create_graph(aicha,'Aicha')
# create_graph(aicha_len,'Aicha_length')
# create_graph(brainnetome,'Brainnatome')
# create_graph(brainnetome_len,'Brainnatome_length')

patients_outlier={}
statistics={}

#AAL statistics
data=statistics_check(aal,patients,name[0])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(aal_len,patients,(name[0]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#harvard statistics
data=statistics_check(harvard,patients,name[1])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(harvard_len,patients,(name[1]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#mindboggle
data=statistics_check(mindboggle,patients,name[2])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(mindboggle_len,patients,(name[2]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#Schaefer


data=statistics_check(schaefer,patients,name[3])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(schaefer_len,patients,(name[3]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#aicha


data=statistics_check(aicha,patients,name[5])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(aicha_len,patients,(name[4]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#brainnetome


data=statistics_check(brainnetome,patients,name[5])
statistics.update(data[0])
patients_outlier.update(data[1])

data=statistics_check(brainnetome_len,patients,(name[5]+len))
statistics.update(data[0])
patients_outlier.update(data[1])

#Saving the data now
f = open("data/statistics.json","w")
f.write(str(statistics))
f.close()

f = open("data/patients_outliers.json","w")
f.write(str(patients_outlier))
f.close()


#SAVING PARCELLATION DATA
pat=pd.Series(patients)
column=['left','right','total']
dat='data/'

df=pd.DataFrame(aal,columns=column)
df['patients']=pat.values
df.to_csv(dat+name[0]+'.csv',index=False)

df=pd.DataFrame(aal_len,columns=column)
df['patients']=pat.values
df.to_csv(dat+name[0]+len+'.csv',index=False)

df = pd.DataFrame(harvard, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[1] + '.csv', index=False)

df = pd.DataFrame(harvard_len, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[1] + len + '.csv', index=False)

df = pd.DataFrame(mindboggle, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[2] + '.csv', index=False)

df = pd.DataFrame(mindboggle_len, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[2] + len + '.csv', index=False)

df = pd.DataFrame(schaefer, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[3] + '.csv', index=False)

df = pd.DataFrame(schaefer_len, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[3] + len + '.csv', index=False)

df = pd.DataFrame(aicha, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[4] + '.csv', index=False)

df = pd.DataFrame(aicha_len, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[4] + len + '.csv', index=False)

df = pd.DataFrame(brainnetome, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[5] + '.csv', index=False)

df = pd.DataFrame(brainnetome_len, columns=column)
df['patients'] = pat.values
df.to_csv(dat + name[5] + len + '.csv', index=False)

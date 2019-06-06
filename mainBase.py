"""
TO extract values for all the classes
"""
from graphMeasures import data_import
from parcellationCheck import cluster_placed_nodes,adjacent_placed_nodes,create_graph
import pandas as pd
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



create_graph(aal,'AAL')
create_graph(aal_len,'AAL_length')
create_graph(harvard,'Harvard')
create_graph(harvard_len,'Harvard_length')
create_graph(mindboggle,'Mindboggle')
create_graph(mindboggle_len,'Mindboggle_length')
create_graph(schaefer_len,'Schaefer_length')
create_graph(schaefer,'Schaefer')
create_graph(aicha,'Aicha')
create_graph(aicha_len,'Aicha_length')
create_graph(brainnetome,'Brainnatome')
create_graph(brainnetome_len,'Brainnatome_length')


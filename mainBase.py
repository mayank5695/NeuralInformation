"""
TO extract values for all the classes
"""
from graphMeasures import graph_function_calling
import pandas as pd
import sys
import os
import glob

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
for dir in glob.iglob(path_patients,recursive=True):
    if os.path.isdir(dir):
        dir2=dir+'/*'
        for subdir in glob.iglob(dir2,recursive=True):
            subdir2=subdir+'/*'
            for file in glob.iglob(subdir2,recursive=True):
                if os.path.isfile(file):
                    print(file)
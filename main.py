import pandas as pd
from graphMeasures import graph_function_calling,graph_function_length
import sys
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

path_patients='SC_matrices/*'
patients=[]
parcellations=['aal90','Harvard Oxford Thr25 2mm Whole Brain (Makris 2006)','Mindboggle 101 - Desikan protocol (Klein 2012)','Brainnetome Atlas (Fan 2016)','AICHA (Joliot 2015)','Schaefer2018_1000Parcels_17Networks_order (Schaefer 2018)']
aal=[]
harvard=[]
mindboggle=[]
brainnetome=[]
aicha=[]
schaefer=[]

#creating average length
aal_len=[]
harvard_len=[]
mindboggle_len=[]
brainnetome_len=[]
aicha_len=[]
schaefer_len=[]

def iterate():
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
                            matrix_values=graph_function_calling(file) #gives (left,right,sum)
                            outF=open("graphValues/aal_small.txt","a")
                            outF.write((patient + ';'))
                            for line in range(0,len(matrix_values)):
                                lin = str(matrix_values[line])
                                outF.write(lin)
                                outF.write(';')
                            outF.write("\n")
                            outF.close()
                            #aal.append(matrix_values)

                        # if (file_name == 'DTI_LEN.mat'):
                        #     matrix_values = graph_function_length(file)  # gives (left,right,sum)
                        #     outF = open("graphValues/aal_len.txt", "a")
                        #     outF.write((patient + ';'))
                        #
                        #     for line in range(0,len(matrix_values)):
                        #         lin = str(matrix_values[line])
                        #         outF.write(lin)
                        #         outF.write(';')
                        #     outF.write("\n")
                        #     outF.close()

                        print('Doing AAL')

                    #Harvard parcellation
                    if (parcel == parcellations[1]):

                        if (file_name == 'DTI_CM.mat'):

                            matrix_values = graph_function_calling(file)  # gives (left,right,sum)
                            #harvard.append(matrix_values)
                            outF = open("graphValues/harvard_small.txt", "a")
                            outF.write((patient + ';'))

                            for line in range(0, len(matrix_values)):
                                lin = str(matrix_values[line])
                                outF.write(lin)

                                outF.write(';')
                            outF.write("\n")
                            outF.close()

                        # if (file_name == 'DTI_LEN.mat'):
                        #     matrix_values = graph_function_length(file)  # gives (left,right,sum)
                        #     #harvard_len.append(matrix_values)
                        #     outF = open("graphValues/harvard_len.txt", "a")
                        #     outF.write((patient + ';'))
                        #
                        #     for line in range(0, len(matrix_values)):
                        #         lin = str(matrix_values[line])
                        #         outF.write(lin)
                        #
                        #         outF.write(';')
                        #     outF.write("\n")
                        #     outF.close()

                        print('Doing Harvard')

                    #Mindboggle
                    if (parcel == parcellations[2]):
                        if (file_name == 'DTI_CM.mat'):
                            matrix_values = graph_function_calling(file)  # gives (left,right,sum)
                            #mindboggle.append(matrix_values)
                            outF = open("graphValues/mindboggle_small.txt", "a")
                            outF.write((patient + ';'))

                            for line in range(0, len(matrix_values)):
                                lin = str(matrix_values[line])
                                outF.write(lin)

                                outF.write(';')
                            outF.write("\n")
                            outF.close()

                        # if (file_name == 'DTI_LEN.mat'):
                        #     matrix_values = graph_function_length(file)  # gives (left,right,sum)
                        #     #mindboggle_len.append(matrix_values)
                        #     outF = open("graphValues/mindboggle_len.txt", "a")
                        #     outF.write((patient + ';'))
                        #
                        #     for line in range(0, len(matrix_values)):
                        #         lin = str(matrix_values[line])
                        #         outF.write(lin)
                        #
                        #         outF.write(';')
                        #     outF.write("\n")
                        #     outF.close()

                        print('Doing mindboggle')

                    #brainnatome
                    if (parcel == parcellations[3]):
                        if (file_name == 'DTI_CM.mat'):
                            matrix_values = graph_function_calling(file)  # gives (left,right,sum)
                            #brainnetome.append(matrix_values)
                            outF = open("small/brainnatome_small.txt", "a")
                            outF.write((patient+';'))
                            for line in range(0, len(matrix_values)):
                                lin = str(matrix_values[line])
                                outF.write(lin)

                                outF.write(';')
                            outF.write("\n")
                            outF.close()

                        # if (file_name == 'DTI_LEN.mat'):
                        #     matrix_values = graph_function_length(file)  # gives (left,right,sum)
                        #     #brainnetome_len.append(matrix_values)
                        #     outF = open("graphValues/brainnatome_len.txt", "a")
                        #     outF.write((patient + ';'))
                        #     for line in range(0, len(matrix_values)):
                        #         lin = str(matrix_values[line])
                        #         outF.write(lin)
                        #
                        #         outF.write(';')
                        #     outF.write("\n")
                        #     outF.close()

                        print('Doing brainnatome')

                    # #Aicha
                    # if (parcel == parcellations[4]):
                    #     if (file_name == 'DTI_CM.mat'):
                    #         matrix_values = graph_function_calling(file)  # gives (left,right,sum)
                    #         #aicha.append(matrix_values)
                    #         outF = open("graphValues/aicha.txt", "a")
                    #         outF.write((patient + ';'))
                    #         for line in range(0, len(matrix_values)):
                    #             lin = str(matrix_values[line])
                    #             outF.write(lin)
                    #
                    #             outF.write(';')
                    #         outF.write("\n")
                    #         outF.close()
                    #
                    #     if (file_name == 'DTI_LEN.mat'):
                    #         matrix_values = graph_function_length(file)  # gives (left,right,sum)
                    #         #aicha_len.append(matrix_values)
                    #         outF = open("graphValues/aicha_len.txt", "a")
                    #         outF.write((patient + ';'))
                    #         for line in range(0, len(matrix_values)):
                    #             lin = str(matrix_values[line])
                    #             outF.write(lin)
                    #
                    #             outF.write(';')
                    #         outF.write("\n")
                    #         outF.close()
                    #
                    #     print('Doing Aicha')
                    #Schaefer
                    # if (parcel == parcellations[5]):
                    #     if (file_name == 'DTI_CM.mat'):
                    #         matrix_values = graph_function_calling(file)  # gives (left,right,sum)
                    #         #schaefer.append(matrix_values)
                    #         outF = open("graphValues/schaefer.txt", "a")
                    #         outF.write((patient + ';'))
                    #         for line in range(0, len(matrix_values)):
                    #             lin = str(matrix_values[line])
                    #             outF.write(lin)
                    #             outF.write(';')
                    #         outF.write("\n")
                    #         outF.close()
                    #
                    #     if (file_name == 'DTI_LEN.mat'):
                    #         matrix_values = graph_function_length(file)  # gives (left,right,sum)
                    #         #schaefer_len.append(matrix_values)
                    #         outF = open("graphValues/schaefer_len.txt", "a")
                    #         outF.write((patient + ';'))
                    #         for line in range(0, len(matrix_values)):
                    #             lin = str(matrix_values[line])
                    #             outF.write(lin)
                    #             outF.write(';')
                    #         outF.write("\n")
                    #         outF.close()
                    #
                    #     print('Doing Schaefer')




def graph_measures_to_file(weight_lst,length_lst,patients,name):

    column_weight = ['degree', 'density', 'global_efficiency', 'transitivity', 'assortavity', 'clustering_coef',
                    'fiedler_value','small_worldness']
    patient_Series = pd.Series(patients)
    length_series=pd.Series(length_lst)
    df=pd.DataFrame(weight_lst,columns=column_weight)
    df.insert(loc=0,column='Patient',value=patient_Series.values)
    df['average_length']=length_series.values
    folder='graphValues/'
    df.to_csv(folder+name+'.csv',index=False)

def run_measures():

    # name = ['aal', 'harvard', 'mindboggle', 'brainnetome', 'aicha', 'schaefer']
    print('starting iteration')

    iterate()

    # print('starting file saving')
    #
    # graph_measures_to_file(aal, aal_len, patients, name[0])
    #
    # graph_measures_to_file(harvard, harvard_len, patients, name[1])
    #
    # graph_measures_to_file(mindboggle, mindboggle_len, patients, name[2])
    #
    # graph_measures_to_file(brainnetome, brainnetome_len, patients, name[3])
    #
    # graph_measures_to_file(aicha, aicha_len, patients, name[4])
    #
    # graph_measures_to_file(schaefer, schaefer_len, patients, name[5])
    #

run_measures()
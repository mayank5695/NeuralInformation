_Author_ = 'Mayank P. Yadav'

"""
This module checks the correlation of different parcellation schemes of different patients with their PSQI score and List Sorting.
Check following link for more detail on the topic: 
https://wiki.humanconnectome.org/display/PublicData/HCP+Data+Dictionary+Public-+Updated+for+the+1200+Subject+Release
"""
import pandas as pd

file_name = 'patient_data.csv'
patient_list = 'measures/patients.csv'


def get_data_from_patients(data_file, patient_file):
    """

    :param data_file: csv file of data
    :return:
    """
    columns = ['Subject', 'PSQI_Score', 'ListSort_AgeAdj']
    parcellation = ['aal', 'brainnatome', 'harvard', 'mindboggle']
    data = pd.read_csv(data_file, delimiter=',', index_col=None)
    patient_file = pd.read_csv(patient_file, delimiter=',')
    data = data[columns]
    aal = []
    brainnetome = []
    harvard = []
    mindboggle = []

    for iter in range(0, patient_file.count()[0]):
        for iter2 in range(0, 4):

            if pd.isna(patient_file[parcellation[iter2]].iloc[iter]):
                continue
            else:
                if (iter2 == 0):
                    row = data.loc[data['Subject'] == patient_file[parcellation[iter2]].iloc[iter]]
                    row = row[['Subject', 'PSQI_Score', 'ListSort_AgeAdj']]

                    data_list = row.values.tolist()
                    if (len(data_list) == 0):
                        data_list = [[-1, -1, -1]]
                    aal.append(data_list[0])
                elif iter2 == 1:
                    row = data.loc[data['Subject'] == patient_file[parcellation[iter2]].iloc[iter]]
                    row = row[['Subject', 'PSQI_Score', 'ListSort_AgeAdj']]

                    data_list = row.values.tolist()
                    if (len(data_list) == 0):
                        data_list = [[-1, -1, -1]]
                    brainnetome.append(data_list[0])
                elif iter2 == 2:
                    row = data.loc[data['Subject'] == patient_file[parcellation[iter2]].iloc[iter]]
                    row = row[['Subject', 'PSQI_Score', 'ListSort_AgeAdj']]

                    data_list = row.values.tolist()
                    if (len(data_list) == 0):
                        data_list = [[-1, -1, -1]]
                    harvard.append(data_list[0])
                elif iter2 == 3:
                    row = data.loc[data['Subject'] == patient_file[parcellation[iter2]].iloc[iter]]
                    row = row[['Subject', 'PSQI_Score', 'ListSort_AgeAdj']]

                    data_list = row.values.tolist()
                    if (len(data_list) == 0):
                        data_list = [[-1, -1, -1]]
                    mindboggle.append(data_list[0])


    convert_to_dataframe(mindboggle, 'mindboggle')
    convert_to_dataframe(harvard, 'harvard')
    convert_to_dataframe(aal, 'aal')
    convert_to_dataframe(brainnetome, 'brainnetome')


def convert_to_dataframe(list_iter, name):
    folder = 'patient_data/'
    col = ['Subject', 'PSQI_Score', 'ListSort_AgeAdj']
    df = pd.DataFrame(list_iter)
    df.columns = col
    df.to_csv(folder + name + '.csv', index=False)


get_data_from_patients(file_name, patient_list)

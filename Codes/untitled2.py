# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:48:41 2022

@author: manou
"""

def get_all_metric_V2(file_path, patient_numbers, bool_metric):
    
    """
    Parameters
    ----------
    file_path : List of strings 
        Links of the considerind files. For example, [link of FA, link of MD] 
    patient_numbers : List of strings
        Number of all patients in string ["02"] for example.    
    bool_metric : boolean
        Specify if we work in WM only or in both GM and WM.
        
    Returns
    -------
    all_metric : Matrix of int
        The columns are representing the patient and the rows the atlases. For example, this matrix will be (141*4) x 35 : "*4" because of the four DTI metrics. So the first 141 are representing the values of FA in each atlas for each patient and so on.
    """
    
    nb_metrics = len(file_path)
    atlas_list = get_corr_atlas_list(get_atlas_list(onlywhite = bool_metric))

    dic = {} #contient les zones du cerveau que l'on retire de l'étude car données manquantes 
    for metric, j in zip(file_path, range(nb_metrics)):
        for patient_nb, i in zip(patient_numbers, range(len(patient_numbers))):
            worksheet = pd.read_excel(metric, sheet_name=patient_nb)
            worksheet = worksheet.to_numpy()
            worksheet = np.nan_to_num(worksheet)
            a = np.nan_to_num(worksheet[:,0])  #Atlas name 
            b = np.nan_to_num(worksheet[:,1])  #Mean at E1
            c = np.nan_to_num(worksheet[:,2])  #Mean at E2
            d = np.nan_to_num(worksheet[:,3])  #Mean at E3
            e = np.nan_to_num(worksheet[:,4])  #Percentage change bewteen E2 and E1  
 
            for k in range(len(e)) : 
                if b[k]==0 or c[k]==0:
                    key = a[k] 
                    if key not in dic.keys():
                        dic[key] = [patient_nb]
                    else:
                        if patient_nb not in dic[key]:
                            dic[key].append(patient_nb)
    print(len(dic))
    with open("sample.json", "w") as outfile:
        json.dump(dic, outfile) 
    
    
    percentage_change_all = np.zeros((len(atlas_list), len(patient_numbers)))
    all_metric = np.zeros((len(atlas_list)*nb_metrics, len(patient_numbers)))
    for metric, j in zip(file_path, range(nb_metrics)):
        for patient_nb, i in zip(patient_numbers, range(len(patient_numbers))):
            worksheet = pd.read_excel(metric, sheet_name=patient_nb)
            worksheet = worksheet.to_numpy()
            worksheet = np.nan_to_num(worksheet)
            a = np.nan_to_num(worksheet[:,0])
            b = np.nan_to_num(worksheet[:,1])
            c = np.nan_to_num(worksheet[:,2]) 
            d = np.nan_to_num(worksheet[:,3])
            e = np.nan_to_num(worksheet[:,4])          
            percentage_change_all[:,i] = e
        start = j*len(atlas_list)
        stop = (len(atlas_list))+j*len(atlas_list)
        all_metric[start:(stop),:] = percentage_change_all
        
    return all_metric
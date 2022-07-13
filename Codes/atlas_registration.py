"""
Created on Wed Mar  9 09:35:09 2022

@author: Fauston
"""

import numpy as np
from CN2 import getTransform, applyTransform
from atlas_modif_name import get_corr_atlas_list, get_atlas_list

def registration_atlas(folder_path, patient_path):

    perso_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/"
    
    # =============================================================================
    # PATIENTS
    # =============================================================================
    perfect = perso_path + "Atlas/FSL_HCP1065_FA_1mm.nii.gz"
    
    # =============================================================================
    # ATLAS
    # =============================================================================
    atlas_list = get_atlas_list(with_CC=False)
    atlas_name = get_corr_atlas_list(atlas_list)
    
    list_time = ["T1", "T2"]
    # =============================================================================
    # REGISTRATION 
    # =============================================================================
    # DESCRIPTION : getTransform(static_file, moving_file,...) and applyTransform(moving_file, mapping calculated by getTransform(), static_file).
    #               Mapping here is transform1 which is the transformation |b| T1 (static) of each patient and the perfect patient (moving) on which the atlased are based.
    #               Then we apply this transform1 on the atlas to make it fit to the T1 of each patient. We do the same for T2 as we work in the patient space.
    
    # ATTENTION - pas besoin de registrer le corps calleux 
    
    name = str(patient_path)
    if ("sub" in name):
        name = name.replace('sub','')
        name = name.replace('_T1','')
    
    for time in list_time:
        Patient = np.array([perfect, 
                            perso_path + "alcoholic_study/subjects/sub" + name + "_" + time + "/dMRI/microstructure/dti/sub" + name + "_" + time + "_FA.nii.gz"])
        
        transform1 = getTransform(Patient[1], Patient[0], onlyAffine=False, diffeomorph=True, sanity_check=False)
        for Atlas in atlas_name:
            name_atlas = str(Atlas[1])
            if ('.nii.gz' in name_atlas):
                name_atlas = name_atlas.replace('.nii.gz', '')
            applyTransform(perso_path + "Atlas/" + Atlas[1], transform1, Patient[1], 
                           perso_path + "Patients/#" + name + "/Atlas/" + name_atlas + "_reg_on_sub" + name + "_" + time + ".nii.gz", binary = False)  
        
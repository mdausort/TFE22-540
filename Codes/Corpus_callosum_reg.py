"""
Created on Fri Apr  8 10:41:42 2022

@author: Fauston
"""

import numpy as np
from CN2 import getTransform, applyTransform
import nibabel as nib

# Transformation of the Corpus Callosum coming from Natbrainlab to fit it with the perfect patient.
# Then will be registered on each patient (T1 and T2) thanks to the atlas_registration script.


atlas_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Atlas/"
metric_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"
patients_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Patients/"

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]

# =============================================================================
# REGISTRATION
# =============================================================================
def registration_CC_on_perfect(folder_path, patient_path):
    
    """
    Parameters
    ----------
    folder_path : String 
        Link of the file in which we are. 
    patient_path : List of strings
        Number of all patients in string ["sub#_T1"] for example.
        
    Returns
    -------
    None. Save a .nii.gz file of the transformation of the CC.
    """
    
    Patient = [atlas_path + "00Average_Brain.nii",
               atlas_path + "FSL_HCP1065_FA_1mm.nii.gz",
               atlas_path + "CC/Corpus_Callosum.nii.gz"]

    transform1 = getTransform(Patient[1], Patient[0], onlyAffine = False, diffeomorph = True, sanity_check = False)
    applyTransform(Patient[2], transform1, Patient[1], atlas_path + "CC/Corpus_Callosum_reg.nii.gz",binary = False)
    
def reg_CC_on_sub(folder_path, patient_path):

    """
    Parameters
    ----------
    folder_path : String 
        Link of the file in which we are. 

    patient_path : List of strings
        Number of all patients in string ["sub#_T1"] for example.
        
    Returns
    -------
    None. Save a .nii.gz file of the transformation of the considered atlas.
    """
    
    name = str(patient_path)
    if ("sub" in name):
        name = name.replace('sub','')
        name = name.replace('_T1','')
           
    Patient = [atlas_path + "FSL_HCP1065_FA_1mm.nii.gz",
               metric_path + "sub" + name + "_T1/dMRI/microstructure/dti/sub" + name + "_T1_FA.nii.gz",
               metric_path + "sub" + name + "_T2/dMRI/microstructure/dti/sub" + name + "_T2_FA.nii.gz",
               atlas_path + "CC/Corpus_callosum_hand_drawn.nii.gz"]
               
    transform_T1 = getTransform(Patient[1], Patient[0], onlyAffine=False, diffeomorph=True, sanity_check=False)
    transform_T2 = getTransform(Patient[2], Patient[0], onlyAffine=False, diffeomorph=True, sanity_check=False)
    
    applyTransform(Patient[3], transform_T1, Patient[1], patients_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_reg_on_sub" + name + "_T1.nii.gz",binary = False)
    applyTransform(Patient[3], transform_T2, Patient[2], patients_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_reg_on_sub" + name + "_T2.nii.gz",binary = False)



# =============================================================================
# MASK FA
# =============================================================================
def mask_wm_FA(FA):
    """
    Parameters
    ----------
    FA : File path (already load by nibabel) of the FA map of the perfect patient. 
    
    Returns
    -------
    a : Matrix of int
        Map of FA corresponding to a mask of FA so characterizing only the white matter.
    """
    
    FA_bis = FA.get_fdata()
    a = np.copy(FA_bis)
    a[a <= 0.34] = 0
    a[a > 0.34] = 1

    return a
    
# Corpus_callosum = nib.load(atlas_path + "CC/Corpus_Callosum_reg.nii.gz").get_fdata()
# perfect_path = nib.load(atlas_path + "FSL_HCP1065_FA_1mm.nii.gz")

# Creation of a mask of Corpus Callosum area 
# CC_mask = Corpus_callosum.copy()
# CC_mask[CC_mask <= 0.14] = 0

# FA_mask = mask_wm_FA(perfect_path)
# mask_final_CC = FA_mask*CC_mask

# out1 = nib.Nifti1Image(mask_final_CC, perfect_path.affine, header = perfect_path.header)
# out1.to_filename(atlas_path + "CC/Corpus_callosum_apres_FA_et_seuil_CC.nii.gz")


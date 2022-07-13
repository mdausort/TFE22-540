"""
Created on Sat Apr  9 09:44:36 2022

@author: Fauston
"""

from skimage.morphology import area_opening,area_closing
import nibabel as nib 

def closing_opening(name):
    
    """
    Parameters
    ----------
    patient_number : String
        Number of the patient.

    Returns
    -------
    None. Save a .nii.gz file after having apply two morphological operations (opening and closing) on the CC.

    """
    
    patient_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Patients/"
    
    path_T1 = patient_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_reg_on_sub" + name + "_T1.nii.gz"
    path_T2 = patient_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_reg_on_sub" + name + "_T2.nii.gz"
    
    image_T1 = nib.load(path_T1).get_fdata()
    image_T2 = nib.load(path_T2).get_fdata()
    
    opening_mask_T1 = area_opening(image_T1, area_threshold=30, connectivity=1, parent=None, tree_traverser=None) #15
    closing_mask_T1 = area_closing(opening_mask_T1, area_threshold=30, connectivity=1, parent=None, tree_traverser=None) #18
    
    opening_mask_T2 = area_opening(image_T2, area_threshold=30, connectivity=1, parent=None, tree_traverser=None) #15
    closing_mask_T2 = area_closing(opening_mask_T2, area_threshold=30, connectivity=1, parent=None, tree_traverser=None) #18
    
    out_T1 = nib.Nifti1Image(closing_mask_T1, affine = nib.load(path_T1).affine, header = nib.load(path_T1).header)
    out_T1.to_filename(patient_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_morpho_reg_on_sub" + name + "_T1.nii.gz")
    
    out_T2 = nib.Nifti1Image(closing_mask_T2, affine = nib.load(path_T2).affine, header = nib.load(path_T2).header)
    out_T2.to_filename(patient_path + "#" + name + "/Atlas/CC/Corpus_callosum_hand_drawn_morpho_reg_on_sub" + name + "_T2.nii.gz")
    
    

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]

for i in patient_numbers:
    closing_opening(i)
    
    
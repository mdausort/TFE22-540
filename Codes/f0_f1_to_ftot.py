"""
Created on Thu Apr 28 14:20:37 2022

@author: Fauston
"""

import nibabel as nib


perso_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]    

# =============================================================================
# MF
# =============================================================================
metric_mf = ["mf_frac_f0",
             "mf_frac_f1",
             "mf_fvf_f0",
             "mf_fvf_f1"]

for patient_nb in patient_numbers:
    
    path_f0_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_" + metric_mf[0] + ".nii.gz"
    path_f0_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_" + metric_mf[0] + ".nii.gz"
    
    path_f1_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_" + metric_mf[1] + ".nii.gz"
    path_f1_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_" + metric_mf[1] + ".nii.gz"
    
    path_fvf_f0_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_" + metric_mf[2] + ".nii.gz"
    path_fvf_f0_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_" + metric_mf[2] + ".nii.gz"
    
    path_fvf_f1_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_" + metric_mf[3] + ".nii.gz"
    path_fvf_f1_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_" + metric_mf[3] + ".nii.gz"
    
    f0_T1 = nib.load(path_f0_T1)   
    f0_T2 = nib.load(path_f0_T2)
    
    f1_T1 = nib.load(path_f1_T1)   
    f1_T2 = nib.load(path_f1_T2) 
    
    fvf_f0_T1 = nib.load(path_fvf_f0_T1)   
    fvf_f0_T2 = nib.load(path_fvf_f0_T2)
    
    fvf_f1_T1 = nib.load(path_fvf_f1_T1)   
    fvf_f1_T2 = nib.load(path_fvf_f1_T2) 
    
    ff_T1 =   f0_T1.get_fdata() + f1_T1.get_fdata()
    ff_T2 =   f0_T2.get_fdata() + f1_T2.get_fdata()
    
    wfvf_T1 = ((f0_T1.get_fdata()*fvf_f0_T1.get_fdata()) + (f1_T1.get_fdata()*fvf_f1_T1.get_fdata()))/(f0_T1.get_fdata() + f1_T1.get_fdata())
    wfvf_T2 = ((f0_T2.get_fdata()*fvf_f0_T2.get_fdata()) + (f1_T2.get_fdata()*fvf_f1_T2.get_fdata()))/(f0_T2.get_fdata() + f1_T2.get_fdata())
    
    out1 = nib.Nifti1Image(ff_T1, affine = f0_T1.affine, header = f0_T1.header)
    out1.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_frac_ftot.nii.gz")
    
    out2 = nib.Nifti1Image(ff_T2, affine = f0_T2.affine, header = f0_T2.header)
    out2.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_frac_ftot.nii.gz")
     
    out3 = nib.Nifti1Image(wfvf_T1, f0_T1.affine, header = f0_T1.header)
    out3.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_wfvf.nii.gz")
    
    out4 = nib.Nifti1Image(wfvf_T2, f0_T2.affine, header = f0_T2.header)
    out4.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_wfvf.nii.gz")
  
# =============================================================================
# DMD
# =============================================================================
metric_dmd = ["diamond_fractions_f0",
              "diamond_fractions_f1"]

for patient_nb in patient_numbers:
    path_f0_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_" + metric_dmd[0] + ".nii.gz"
    path_f0_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_" + metric_dmd[0] + ".nii.gz"
    path_f1_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_" + metric_dmd[1] + ".nii.gz"
    path_f1_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_" + metric_dmd[1] + ".nii.gz"
    
    f0_T1 = nib.load(path_f0_T1)   
    f0_T2 = nib.load(path_f0_T2)
    f1_T1 = nib.load(path_f1_T1)   
    f1_T2 = nib.load(path_f1_T2)   
    
    ff_T1 =   f0_T1.get_fdata()+ f1_T1.get_fdata()
    ff_T2 =   f0_T2.get_fdata()+ f1_T2.get_fdata()
    
    out1 = nib.Nifti1Image(ff_T1, f0_T1.affine, header = f0_T1.header)
    out1.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_fractions_ftot.nii.gz")
    out2 = nib.Nifti1Image(ff_T2, f0_T2.affine, header = f0_T2.header)
    out2.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_ftot.nii.gz")
             



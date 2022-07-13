"""
Created on Fri Mar  4 09:40:49 2022

@author: Fauston
"""

import numpy as np
from CN2 import getTransform, applyTransform

perso_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]    


# =============================================================================
# PATIENTS FA
# =============================================================================
FA_all = np.array(["FA_T1","FA_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T1_FA.nii.gz",
                      perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T2_FA.nii.gz"])
    FA_all = np.append(FA_all,paths,axis=0)
FA_all = np.reshape(FA_all,((len(patient_numbers)+1),2))
FA_all = np.delete(FA_all, (0), axis=0)


# =============================================================================
# PATIENTS MD
# =============================================================================
MD_all = np.array(["MD_T1", "MD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T1_MD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T2_MD.nii.gz"])
    MD_all = np.append(MD_all, paths, axis=0)
MD_all = np.reshape(MD_all, ((len(patient_numbers)+1), 2))
MD_all = np.delete(MD_all, (0), axis=0)


# =============================================================================
# PATIENTS AD
# =============================================================================
AD_all = np.array(["AD_T1", "AD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T1_AD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T2_AD.nii.gz"])
    AD_all = np.append(AD_all, paths, axis=0)
AD_all = np.reshape(AD_all, ((len(patient_numbers)+1), 2))
AD_all = np.delete(AD_all, (0), axis=0)


# =============================================================================
# PATIENTS RD
# =============================================================================
RD_all = np.array(["RD_T1", "RD_T2",])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T1_RD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T2_RD.nii.gz"])
    RD_all = np.append(RD_all, paths, axis=0)
RD_all = np.reshape(RD_all, ((len(patient_numbers)+1), 2))
RD_all = np.delete(RD_all, (0), axis=0)


# =============================================================================
# METRIC REGISTRATION 
# =============================================================================
def register_metric(metric_all, metric_name):
    
    """
    Parameters
    ----------
    metric_all : List of file path of the metric of one patient at T1 and T2.
    metric_name : List of string
        Containing all the metrics of DTI.

    Returns
    -------
    None. Save a .nii.gz file of the registered metric
    """
    
    to_register = patient_numbers
    
    for Patient,patient_nb in zip(metric_all,to_register):
        transform1 = getTransform(Patient[0], Patient[1], onlyAffine=False, diffeomorph=True, sanity_check=False)
        applyTransform(Patient[1], transform1, 
                       Patient[0], perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/dti/sub" + patient_nb + "_T2_" + metric_name + "_reg.nii.gz",
                       binary = False)  

metric_name = ["FA","AD","RD","MD"]
register_metric(FA_all,metric_name[0])
register_metric(AD_all,metric_name[1])
register_metric(RD_all,metric_name[2])
register_metric(MD_all,metric_name[3])


# =============================================================================
# PATIENTS FA - wFA
# =============================================================================
FA_all = np.array(["cFA_T1","cFA_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cFA_T1.nii.gz",
                      perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cFA_T2.nii.gz"])
    FA_all = np.append(FA_all,paths,axis=0)
FA_all = np.reshape(FA_all,((len(patient_numbers)+1),2))
cFA_all = np.delete(FA_all, (0), axis=0)


# =============================================================================
# PATIENTS MD - wMD
# =============================================================================
MD_all = np.array(["cMD_T1", "cMD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cMD_T1.nii.gz",
                      perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cMD_T2.nii.gz"])
    MD_all = np.append(MD_all, paths, axis=0)
MD_all = np.reshape(MD_all, ((len(patient_numbers)+1), 2))
cMD_all = np.delete(MD_all, (0), axis=0)


# =============================================================================
# PATIENTS AD - wAD
# =============================================================================
AD_all = np.array(["cAD_T1", "cAD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cAD_T1.nii.gz",
                      perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cAD_T2.nii.gz"])
    AD_all = np.append(AD_all, paths, axis=0)
AD_all = np.reshape(AD_all, ((len(patient_numbers)+1), 2))
cAD_all = np.delete(AD_all, (0), axis=0)


# =============================================================================
# PATIENTS RD - wRD
# =============================================================================
RD_all = np.array(["cRD_T1", "cRD_T2",])
for patient_nb in patient_numbers:
    paths = np.array([perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cRD_T1.nii.gz",
                      perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cRD_T2.nii.gz"])
    RD_all = np.append(RD_all, paths, axis=0)
RD_all = np.reshape(RD_all, ((len(patient_numbers)+1), 2))
cRD_all = np.delete(RD_all, (0), axis=0)


# =============================================================================
# REGISTRATION 
# =============================================================================
def registration(to_register, tenseur):
  
  if (tenseur == False):
      for Patient, patient_nb in zip(fractions_all_bis, to_register):
          print("-----------------------------")
          print("Patient n°",patient_nb)
          print("-----------------------------")
          transform1 = getTransform(Patient[0], Patient[3], onlyAffine=False, diffeomorph=True, sanity_check=False)
          applyTransform(Patient[3], transform1, Patient[0], 
                         perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_f0_reg.nii.gz",
                         binary = False) 
          applyTransform(Patient[4], transform1, Patient[1], 
                         perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_f1_reg.nii.gz",
                         binary = False)  
          applyTransform(Patient[5], transform1, Patient[2], 
                         perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_csf_reg.nii.gz",
                         binary = False)  
          
  else:
      for Patient, MD_Patient, AD_Patient, RD_Patient, patient_nb in zip(cFA_all, cMD_all, cAD_all, cRD_all, to_register):
          print("-----------------------------")
          print("Patient n°",patient_nb)
          print("-----------------------------")
          transform1 = getTransform(Patient[0], Patient[1], onlyAffine=False, diffeomorph=True, sanity_check=False)
          applyTransform(Patient[1], transform1, Patient[0], 
                          perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cFA_T2_regMF.nii.gz",
                          binary = False) 
          applyTransform(MD_Patient[1], transform1, MD_Patient[0], 
                          perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cMD_T2_regMF.nii.gz",
                          binary = False)  
          applyTransform(AD_Patient[1], transform1, AD_Patient[0], 
                          perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cAD_T2_regMF.nii.gz",
                          binary = False)  
          applyTransform(RD_Patient[1], transform1, RD_Patient[0], 
                          perso_path+"/PATIENTS/#"+patient_nb+"/ELIKOPY/DIAMOND/sub"+patient_nb+"_cRD_T2_regMF.nii.gz",
                          binary = False)  

to_register = patient_numbers
# registration(to_register, False)
# registration(to_register, True)









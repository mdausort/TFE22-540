"""
Created on Wed Apr 13 09:14:26 2022

@author: Fauston
"""

import numpy as np
import nibabel as nib
import time

perso_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]    

def get_FA_DIAMOND(folder_path, patient_path):

    """
    Parameters
    ----------
    folder_path : String 
        Link of the file in which we are. 
    patient_path : List of strings
        Number of all patients in string ["sub#_T1"] for example.

    Returns
    -------
    None. But creation of files containing the cFA, cMD, cAD and cRD for each patient. "c" stands for compartment.
    """
    
    tenseur_list = ["t0", "t1"]
    
    patient_nb = str(patient_path)
    if ("sub" in patient_nb):
        patient_nb = patient_nb.replace('sub','')
        patient_nb = patient_nb.replace('_T1','')
    
    for tenseur in tenseur_list:
        start_time = time.time()
        
        path = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/dti/sub" + patient_nb + "_T1_FA.nii.gz"
        
        comp_T1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_" + tenseur + ".nii.gz"
        comp_T2 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_" + tenseur + ".nii.gz"
        
        comp_T1 = nib.load(comp_T1).get_fdata()
        comp_T2 = nib.load(comp_T2).get_fdata()

        MD_T1 = np.zeros((comp_T1.shape[0],comp_T1.shape[1],comp_T1.shape[2]))
        AD_T1 = np.zeros((comp_T1.shape[0],comp_T1.shape[1],comp_T1.shape[2]))
        RD_T1 = np.zeros((comp_T1.shape[0],comp_T1.shape[1],comp_T1.shape[2]))
        FA_T1 = np.zeros((comp_T1.shape[0],comp_T1.shape[1],comp_T1.shape[2]))
        
        MD_T2 = np.zeros((comp_T2.shape[0],comp_T2.shape[1],comp_T2.shape[2]))
        AD_T2 = np.zeros((comp_T2.shape[0],comp_T2.shape[1],comp_T2.shape[2]))
        RD_T2 = np.zeros((comp_T2.shape[0],comp_T2.shape[1],comp_T2.shape[2]))
        FA_T2 = np.zeros((comp_T2.shape[0],comp_T2.shape[1],comp_T2.shape[2]))
        
        D_T1 = np.array([[np.squeeze(comp_T1[:,:,:,:,0]) , np.squeeze(comp_T1[:,:,:,:,1]) , np.squeeze(comp_T1[:,:,:,:,3])],
                         [np.squeeze(comp_T1[:,:,:,:,1]) , np.squeeze(comp_T1[:,:,:,:,2]) , np.squeeze(comp_T1[:,:,:,:,4])],
                         [np.squeeze(comp_T1[:,:,:,:,3]) , np.squeeze(comp_T1[:,:,:,:,4]) , np.squeeze(comp_T1[:,:,:,:,5])]])
        

        D_T2 = np.array([[np.squeeze(comp_T2[:,:,:,:,0]) , np.squeeze(comp_T2[:,:,:,:,1]) , np.squeeze(comp_T2[:,:,:,:,3])],
                          [np.squeeze(comp_T2[:,:,:,:,1]) , np.squeeze(comp_T2[:,:,:,:,2]) , np.squeeze(comp_T2[:,:,:,:,4])],
                          [np.squeeze(comp_T2[:,:,:,:,3]) , np.squeeze(comp_T2[:,:,:,:,4]) , np.squeeze(comp_T2[:,:,:,:,5])]])

        for i in range(comp_T1.shape[0]):
            for j in range(comp_T1.shape[1]):
                for k in range(comp_T1.shape[2]):
                    valeurs_propres_T1 = np.array(np.linalg.eigvals(D_T1[:,:,i,j,k]))
                    max_valeur_T1 = max(np.abs(valeurs_propres_T1))
                    index_lambda1 = [l for l in range(len(valeurs_propres_T1)) if abs(valeurs_propres_T1[l])==max_valeur_T1]
        
                    copy_valeurs_propres_T1 = np.copy(valeurs_propres_T1)
                    copy_valeurs_propres_T1 = np.delete(copy_valeurs_propres_T1, index_lambda1[0])
                    copy_valeurs_propres_T1 = np.array(copy_valeurs_propres_T1)
                    
                    MD_T1[i,j,k] = (valeurs_propres_T1[0] + valeurs_propres_T1[1] + valeurs_propres_T1[2])/3
                    AD_T1[i,j,k] = valeurs_propres_T1[index_lambda1[0]]
                    RD_T1[i,j,k] = (copy_valeurs_propres_T1[0]+copy_valeurs_propres_T1[1])/2
                    if((valeurs_propres_T1[0]**2 + valeurs_propres_T1[1]**2 + valeurs_propres_T1[2]**2) == 0):
                        FA_T1[i,j,k] = 0
                    else:
                        FA_T1[i,j,k] = np.sqrt(3/2)*np.sqrt(((valeurs_propres_T1[0] - MD_T1[i,j,k])**2 + (valeurs_propres_T1[1] - MD_T1[i,j,k])**2 + (valeurs_propres_T1[2] - MD_T1[i,j,k])**2)/(valeurs_propres_T1[0]**2 + valeurs_propres_T1[1]**2 + valeurs_propres_T1[2]**2))
                    
                    valeurs_propres_T2 = np.array(np.linalg.eigvals(D_T2[:,:,i,j,k]))
                    max_valeur_T2 = max(np.abs(valeurs_propres_T2))
                    index_lambda2 = [l for l in range(len(valeurs_propres_T2)) if abs(valeurs_propres_T2[l])==max_valeur_T2]
        
                    copy_valeurs_propres_T2 = np.copy(valeurs_propres_T2)
                    copy_valeurs_propres_T2 = np.delete(copy_valeurs_propres_T2, index_lambda2[0])
                    copy_valeurs_propres_T2 = np.array(copy_valeurs_propres_T2)
                    
                    MD_T2[i,j,k] = (valeurs_propres_T2[0] + valeurs_propres_T2[1] + valeurs_propres_T2[2])/3
                    AD_T2[i,j,k] = valeurs_propres_T2[index_lambda2[0]]
                    RD_T2[i,j,k] = (copy_valeurs_propres_T2[0]+copy_valeurs_propres_T2[1])/2
                    if ((valeurs_propres_T2[0]**2 + valeurs_propres_T2[1]**2 + valeurs_propres_T2[2]**2)==0):
                        FA_T2[i,j,k] = 0
                    else:
                        FA_T2[i,j,k] = np.sqrt(3/2)*np.sqrt(((valeurs_propres_T2[0] - MD_T2[i,j,k])**2 + (valeurs_propres_T2[1] - MD_T2[i,j,k])**2 + (valeurs_propres_T2[2] - MD_T2[i,j,k])**2)/(valeurs_propres_T2[0]**2 + valeurs_propres_T2[1]**2 + valeurs_propres_T2[2]**2))
                    
        # MD_T1 = MD_T1/np.max(MD_T1[np.isnan(MD_T1)==False])
        out = nib.Nifti1Image(MD_T1, affine = nib.load(path).affine, header = nib.load(path).header)
        out.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_MD_DMD_" + tenseur + ".nii.gz")
        
        # AD_T1 = AD_T1/np.max(AD_T1[np.isnan(AD_T1)==False]) 
        out1 = nib.Nifti1Image(AD_T1, affine = nib.load(path).affine, header = nib.load(path).header)
        out1.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_AD_DMD_" + tenseur + ".nii.gz")
        
        # RD_T1 = RD_T1/np.max(RD_T1[np.isnan(RD_T1)==False])
        out2 = nib.Nifti1Image(RD_T1, affine = nib.load(path).affine, header = nib.load(path).header)
        out2.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_RD_DMD_" + tenseur + ".nii.gz")
        
        # FA_T1 = FA_T1/np.max(FA_T1[np.isnan(FA_T1)==False])
        out3 = nib.Nifti1Image(FA_T1, affine = nib.load(path).affine, header = nib.load(path).header)
        out3.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_FA_DMD_" + tenseur + ".nii.gz")
        
        # MD_T2 = MD_T2/np.max(MD_T2[np.isnan(MD_T2)==False])
        out4 = nib.Nifti1Image(MD_T2, affine = nib.load(path).affine, header = nib.load(path).header)
        out4.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_MD_DMD_" + tenseur + ".nii.gz")
        
        # AD_T2 = AD_T2/np.max(AD_T2[np.isnan(AD_T2)==False])
        out5 = nib.Nifti1Image(AD_T2, affine = nib.load(path).affine, header = nib.load(path).header)
        out5.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_AD_DMD_" + tenseur + ".nii.gz")
        
        # RD_T2 = RD_T2/np.max(MD_T2[np.isnan(MD_T2)==False])
        out6 = nib.Nifti1Image(RD_T2, affine = nib.load(path).affine, header = nib.load(path).header)
        out6.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_RD_DMD_" + tenseur + ".nii.gz")
        
        # FA_T2 = FA_T2/np.max(FA_T2[np.isnan(FA_T2)==False])
        out7 = nib.Nifti1Image(FA_T2, affine = nib.load(path).affine, header = nib.load(path).header)
        out7.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_FA_DMD_" + tenseur + ".nii.gz")
        
        print("Temps mis:", time.time() - start_time)
    

def get_cMetrics(folder_path, patient_path):

    """
    Parameters
    ----------
    folder_path : String 
        Link of the file in which we are. 
    patient_path : List of strings
        Number of all patients in string ["sub#_T1"] for example.

    Returns
    -------
    None. But creation of files containing the wFA, wMD, wAD and wRD for each patient. "w" stands for weigthed.
    """
    
    patient_nb = str(patient_path)
    if ("sub" in patient_nb):
        patient_nb = patient_nb.replace('sub','')
        patient_nb = patient_nb.replace('_T1','')
    
    metrics = ["FA","MD","AD","RD"]
    
    for metric in metrics :    
        metric_T1_t0 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_" + metric + "_DMD_t0.nii.gz"
        metric_T2_t0 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_" + metric + "_DMD_t0.nii.gz"
        
        metric_T1_t1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_" + metric + "_DMD_t1.nii.gz"
        metric_T2_t1 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_" + metric + "_DMD_t1.nii.gz"
        
        fraction_T1_t0 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_fractions_f0.nii.gz"
        fraction_T2_t0 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_f0.nii.gz"
        
        fraction_T1_t1 = perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_fractions_f1.nii.gz"
        fraction_T2_t1 = perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_f1.nii.gz"

        cMetric_T1 = (nib.load(metric_T1_t0).get_fdata() * nib.load(fraction_T1_t0).get_fdata() + nib.load(metric_T1_t1).get_fdata() * nib.load(fraction_T1_t1).get_fdata())/(nib.load(fraction_T1_t1).get_fdata() + nib.load(fraction_T1_t0).get_fdata())
        cMetric_T2 = (nib.load(metric_T2_t0).get_fdata() * nib.load(fraction_T2_t0).get_fdata() + nib.load(metric_T2_t1).get_fdata() * nib.load(fraction_T2_t1).get_fdata())/(nib.load(fraction_T2_t1).get_fdata() + nib.load(fraction_T2_t0).get_fdata())
        
        out = nib.Nifti1Image(cMetric_T1, affine = nib.load(metric_T1_t0).affine, header = nib.load(metric_T1_t0).header)
        out.to_filename(perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_w" + metric + ".nii.gz")
        
        out1 = nib.Nifti1Image(cMetric_T2, affine = nib.load(metric_T2_t0).affine, header = nib.load(metric_T2_t0).header)
        out1.to_filename(perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_w" + metric + ".nii.gz")


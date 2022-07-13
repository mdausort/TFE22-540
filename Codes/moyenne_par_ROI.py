"""
Created on Wed Mar  9 22:39:41 2022

@author: Fauston
"""

import numpy as np
import nibabel as nib
from atlas_modif_name import get_corr_atlas_list, get_atlas_list
import xlsxwriter
import time
import math


perso_path = "D:/EPL/MASTER/TFE/Patients/" # "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]    

"#04\Elikopy\DTI\sub04_T1_FA.nii.gz"
# =============================================================================
# DTI
# =============================================================================
#----------------------------- PATIENTS FA ------------------------------------
FA_all = np.array(["FA_T1","FA_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T1_FA.nii.gz",
                      perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T2_FA.nii.gz"])
    FA_all = np.append(FA_all,paths,axis=0)
FA_all = np.reshape(FA_all,((len(patient_numbers)+1),2))
FA_all = np.delete(FA_all, (0), axis=0)


#----------------------------- PATIENTS MD ------------------------------------
MD_all = np.array(["MD_T1", "MD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T1_MD.nii.gz",
                      perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T2_MD.nii.gz"])
    MD_all = np.append(MD_all, paths, axis=0)
MD_all = np.reshape(MD_all, ((len(patient_numbers)+1), 2))
MD_all = np.delete(MD_all, (0), axis=0)


#----------------------------- PATIENTS AD ------------------------------------
AD_all = np.array(["AD_T1", "AD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T1_AD.nii.gz",
                      perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T2_AD.nii.gz"])
    AD_all = np.append(AD_all, paths, axis=0)
AD_all = np.reshape(AD_all, ((len(patient_numbers)+1), 2))
AD_all = np.delete(AD_all, (0), axis=0)


#----------------------------- PATIENTS RD ------------------------------------
RD_all = np.array(["RD_T1", "RD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T1_RD.nii.gz",
                      perso_path + "#" + patient_nb + "/Elikopy/DTI/sub" + patient_nb + "_T2_RD.nii.gz"])
    RD_all = np.append(RD_all, paths, axis=0)
RD_all = np.reshape(RD_all, ((len(patient_numbers)+1), 2))
RD_all = np.delete(RD_all, (0), axis=0)


DTI_metrics = [FA_all,MD_all,AD_all,RD_all]
DTI_names = ["FA","MD","AD","RD"]


# =============================================================================
# NODDI
# =============================================================================
#--------------------------------- FBUNDLE ------------------------------------
fbundle_all = np.array(["fbundle_T1","fbundle_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_fbundle.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_fbundle.nii.gz"])
    fbundle_all = np.append(fbundle_all,paths,axis=0)
fbundle_all = np.reshape(fbundle_all,((len(patient_numbers)+1),2))
fbundle_all = np.delete(fbundle_all, (0), axis=0)


#--------------------------------- FEXTRA -------------------------------------
fextra_all = np.array(["fextra_T1","fextra_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_fextra.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_fextra.nii.gz"])
    fextra_all = np.append(fextra_all,paths,axis=0)
fextra_all = np.reshape(fextra_all,((len(patient_numbers)+1),2))
fextra_all = np.delete(fextra_all, (0), axis=0)


#--------------------------------- FINTRA -------------------------------------
fintra_all = np.array(["fintra_T1","fintra_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_fintra.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_fintra.nii.gz"])
    fintra_all = np.append(fintra_all,paths,axis=0)
fintra_all = np.reshape(fintra_all,((len(patient_numbers)+1),2))
fintra_all = np.delete(fintra_all, (0), axis=0)


#--------------------------------- FISO ---------------------------------------
fiso_all = np.array(["fiso_T1","fiso_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_fiso.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_fiso.nii.gz"])
    fiso_all = np.append(fiso_all,paths,axis=0)
fiso_all = np.reshape(fiso_all,((len(patient_numbers)+1),2))
fiso_all = np.delete(fiso_all, (0), axis=0)


#--------------------------------- FICVF --------------------------------------
icvf_all = np.array(["icvf_T1","icvf_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_icvf.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_icvf.nii.gz"])
    icvf_all = np.append(icvf_all,paths,axis=0)
icvf_all = np.reshape(icvf_all,((len(patient_numbers)+1),2))
icvf_all = np.delete(icvf_all, (0), axis=0)


#--------------------------------- ODI ----------------------------------------
odi_all = np.array(["odi_T1","odi_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/noddi/sub" + patient_nb + "_T1_noddi_odi.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/noddi/sub" + patient_nb + "_T2_noddi_odi.nii.gz"])
    odi_all = np.append(odi_all,paths,axis=0)
odi_all = np.reshape(odi_all,((len(patient_numbers)+1),2))
odi_all = np.delete(odi_all, (0), axis=0)


NODDI_metrics = [fbundle_all,fextra_all,fintra_all,fiso_all,icvf_all,odi_all]
NODDI_names = ["noddi_fbundle","noddi_fextra","noddi_fintra","noddi_fiso","noddi_icvf","noddi_odi"]


# =============================================================================
# DIAMOND
# =============================================================================
#---------------------------------  FRAC_FTOT  --------------------------------
fractions_all2 = np.array(["fractions_T1","fractions_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_fractions_ftot.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_ftot.nii.gz"])                      
    fractions_all2 = np.append(fractions_all2, paths, axis=0)
fractions_all2 = np.reshape(fractions_all2,((len(patient_numbers)+1),2))
fractions_all2 = np.delete(fractions_all2, (0), axis=0)


#---------------------------------  FRAC_CSF  ---------------------------------
fractions_all3 = np.array(["fractions_T1","fractions_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_diamond_fractions_csf.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_diamond_fractions_csf.nii.gz"])                      
    fractions_all3 = np.append(fractions_all3, paths, axis=0)
fractions_all3 = np.reshape(fractions_all3,((len(patient_numbers)+1),2))
fractions_all3 = np.delete(fractions_all3, (0), axis=0)


DIAMOND_metrics = [fractions_all2, fractions_all3] 
DIAMOND_names = ["diamond_fractions_ftot", "diamond_fractions_csf"]


#----------------------------- PATIENTS wFA ------------------------------------
wFA_all = np.array(["wFA_T1","wFA_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_wFA.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_wFA.nii.gz"])
    wFA_all = np.append(wFA_all,paths,axis=0)
wFA_all = np.reshape(wFA_all,((len(patient_numbers)+1),2))
wFA_all = np.delete(wFA_all, (0), axis=0)


#----------------------------- PATIENTS wMD ------------------------------------
wMD_all = np.array(["wMD_T1", "wMD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_wMD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_wMD.nii.gz"])
    wMD_all = np.append(wMD_all, paths, axis=0)
wMD_all = np.reshape(wMD_all, ((len(patient_numbers)+1), 2))
wMD_all = np.delete(wMD_all, (0), axis=0)


#----------------------------- PATIENTS wAD ------------------------------------
wAD_all = np.array(["wAD_T1", "wAD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_wAD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_wAD.nii.gz"])
    wAD_all = np.append(wAD_all, paths, axis=0)
wAD_all = np.reshape(wAD_all, ((len(patient_numbers)+1), 2))
wAD_all = np.delete(wAD_all, (0), axis=0)


#----------------------------- PATIENTS wRD ------------------------------------
wRD_all = np.array(["wRD_T1", "wRD_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/diamond/sub" + patient_nb + "_T1_wRD.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/diamond/sub" + patient_nb + "_T2_wRD.nii.gz"])
    wRD_all = np.append(wRD_all, paths, axis=0)
wRD_all = np.reshape(wRD_all, ((len(patient_numbers)+1), 2))
wRD_all = np.delete(wRD_all, (0), axis=0)


cDIAMOND_metrics = [wFA_all,wMD_all,wAD_all,wRD_all]
cDIAMOND_names = ["wFA","wMD","wAD","wRD"]


# =============================================================================
# MF
# =============================================================================
#---------------------------------  FRAC_FTOT  --------------------------------
frac_ftot_all = np.array(["frac_f1_T1","frac_f1_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_frac_ftot.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_frac_ftot.nii.gz"])
    frac_ftot_all = np.append(frac_ftot_all,paths,axis=0) 
frac_ftot_all = np.reshape(frac_ftot_all,((len(patient_numbers)+1),2))
frac_ftot_all = np.delete(frac_ftot_all, (0), axis=0)


#--------------------------------  FRAC_CSF  ----------------------------------
frac_csf_all = np.array(["frac_csf_T1","frac_csf_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_frac_csf.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_frac_csf.nii.gz"])
    frac_csf_all = np.append(frac_csf_all,paths,axis=0) 
frac_csf_all = np.reshape(frac_csf_all,((len(patient_numbers)+1),2))
frac_csf_all = np.delete(frac_csf_all, (0), axis=0)


#----------------------------------  WFVF  ------------------------------------
wfvf_all = np.array(["fvf_f1_T1","fvf_f1_T2"])
for patient_nb in patient_numbers :                     
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_wfvf.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_wfvf.nii.gz"])
    wfvf_all = np.append(wfvf_all,paths,axis=0) 
wfvf_all = np.reshape(wfvf_all,((len(patient_numbers)+1),2))
wfvf_all = np.delete(wfvf_all, (0), axis=0)


#---------------------------------  FVF_TOT  ----------------------------------
fvf_tot_all = np.array(["fvf_tot_T1","fvf_tot_T2"])
for patient_nb in patient_numbers :
    paths = np.array([perso_path + "sub" + patient_nb + "_T1/dMRI/microstructure/mf/sub" + patient_nb + "_T1_mf_fvf_tot.nii.gz",
                      perso_path + "sub" + patient_nb + "_T2/dMRI/microstructure/mf/sub" + patient_nb + "_T2_mf_fvf_tot.nii.gz"])
    fvf_tot_all = np.append(fvf_tot_all,paths,axis=0) 
fvf_tot_all = np.reshape(fvf_tot_all,((len(patient_numbers)+1),2))
fvf_tot_all = np.delete(fvf_tot_all, (0), axis=0)


MF_metrics = [frac_csf_all,frac_ftot_all,wfvf_all,fvf_tot_all]
MF_names = ["mf_frac_csf","mf_frac_ftot","mf_wfvf","mf_fvf_tot"]


# =============================================================================
# MASK
# =============================================================================
#---------------------------------  BRAIN  ------------------------------------
brain_mask_all = np.array(["brain_mask_T1", "brain_mask_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "#" + patient_nb + "/sub" + patient_nb + "_T1_brain_mask.nii.gz",
                      perso_path + "#" + patient_nb + "/sub" + patient_nb + "_T2_brain_mask.nii.gz"])
    brain_mask_all = np.append(brain_mask_all, paths, axis=0)
brain_mask_all = np.reshape(brain_mask_all, ((len(patient_numbers)+1), 2))
brain_mask_all = np.delete(brain_mask_all, (0), axis=0)


#---------------------------------  WHITE  ------------------------------------
wm_mask_all = np.array(["wm_mask_T1", "wm_mask_T2"])
for patient_nb in patient_numbers:
    paths = np.array([perso_path + "#" + patient_nb + "/sub" + patient_nb + "_T1_wm_mask.nii.gz",
                      perso_path + "#" + patient_nb + "/sub" + patient_nb + "_T2_wm_mask.nii.gz"])
    wm_mask_all = np.append(wm_mask_all, paths, axis=0)
wm_mask_all = np.reshape(wm_mask_all, ((len(patient_numbers)+1), 2))
wm_mask_all = np.delete(wm_mask_all, (0), axis=0)


metric_list = []
metric_name = []
for i in range(4):
    metric_list.append(DTI_metrics[i])
    metric_name.append(DTI_names[i])
for i in range(6):
    metric_list.append(NODDI_metrics[i])
    metric_name.append(NODDI_names[i])
for i in range(2):
    metric_list.append(DIAMOND_metrics[i])
    metric_name.append(DIAMOND_names[i])
for i in range(4):
    metric_list.append(cDIAMOND_metrics[i])
    metric_name.append(cDIAMOND_names[i])
for i in range(4): 
    metric_list.append(MF_metrics[i])
    metric_name.append(MF_names[i])

# =============================================================================
# MOYENNE PAR ZONE
# =============================================================================
def moyenne_par_roi(folder_path, patient_path):
    
    """
    Parameters
    ----------
    folder_path : String 
        Link of the file in which we are. 
    patient_path : List of strings
        Number of all patients in string ["sub#_T1"] for example.

    Returns
    -------
    None. But creation of Excel files for each metric of each model.
    """
    
    analyse_path = "D:/EPL/MASTER/TFE/alcoolique/Analyse/Excel/" #"/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Analyse/Excel/"
    
    start_time = time.time()
    
    # DTI
    if (patient_path == "sub02_T1"):
        patient_all = metric_list[0]
        metric = metric_name[0]
        bool_metric = False
    if (patient_path == "sub04_T1"):
        patient_all = metric_list[1]
        metric = metric_name[1]
        bool_metric = False
    if (patient_path == "sub05_T1"):
        patient_all = metric_list[2]
        metric = metric_name[2]
        bool_metric = False
    if (patient_path == "sub08_T1"):
        patient_all = metric_list[3]
        metric = metric_name[3]
        bool_metric = False
    # NODDI
    if (patient_path == "sub09_T1"):
        patient_all = metric_list[4]
        metric = metric_name[4]
        bool_metric = True
    if (patient_path == "sub11_T1"):
        patient_all = metric_list[5]
        metric = metric_name[5]
        bool_metric = True
    if (patient_path == "sub12_T1"):
        patient_all = metric_list[6]
        metric = metric_name[6]
        bool_metric = True
    if (patient_path == "sub13_T1"):
        patient_all = metric_list[7]
        metric = metric_name[7]
        bool_metric = True
    if (patient_path == "sub14_T1"):
        patient_all = metric_list[8]
        metric = metric_name[8]
        bool_metric = True
    if (patient_path == "sub15_T1"):
        patient_all = metric_list[9]
        metric = metric_name[9]
        bool_metric = True
    # DIAMOND
    if (patient_path == "sub17_T1"):
        patient_all = metric_list[10]
        metric = metric_name[10]
        bool_metric = True
    if (patient_path == "sub19_T1"):
        patient_all = metric_list[11]
        metric = metric_name[11]
        bool_metric = True
    if (patient_path == "sub20_T1"):
        patient_all = metric_list[12]
        metric = metric_name[12]
        bool_metric = True
    if (patient_path == "sub21_T1"):
        patient_all = metric_list[13]
        metric = metric_name[13]
        bool_metric = True
    if (patient_path == "sub22_T1"):
        patient_all = metric_list[14]
        metric = metric_name[14]
        bool_metric = True
    if (patient_path == "sub24_T1"):
        patient_all = metric_list[15]
        metric = metric_name[15]
        bool_metric = True
    # MF
    if (patient_path == "sub26_T1"):
        patient_all = metric_list[16]
        metric = metric_name[16]
        bool_metric = True
    if (patient_path == "sub27_T1"):
        patient_all = metric_list[17]
        metric = metric_name[17]
        bool_metric = True
    if (patient_path == "sub28_T1"):
        patient_all = metric_list[18]
        metric = metric_name[18]
        bool_metric = True
    if (patient_path == "sub30_T1"):
        patient_all = metric_list[19]
        metric = metric_name[19]
        bool_metric = True
    
    atlas_list = get_atlas_list(onlywhite = bool_metric) 
    atlas_list_name = get_corr_atlas_list(atlas_list) 

    workbook = xlsxwriter.Workbook(analyse_path + 'Mean_ROI_' + metric + '.xlsx')
    
    for patient, brain_mask, wm_mask, patient_nb in zip(patient_all, brain_mask_all, wm_mask_all, patient_numbers):
        
        img = nib.load(patient[0])
        img1 = nib.load(patient[1])
        
        worksheet = workbook.add_worksheet(patient_nb)
    
        azer = 2
    
        path_atlas_reg = "D:/EPL/MASTER/TFE/Patients/#" + patient_nb #"/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Patients/#" + patient_nb 
        
        brain_mask_T1 = nib.load(brain_mask[0]).get_fdata()
        brain_mask_T1[:,:,0] = 0
        brain_mask_T1[:,:,-1] = 0
        brain_mask_T2 = nib.load(brain_mask[1]).get_fdata()
        brain_mask_T2[:,:,0] = 0
        brain_mask_T2[:,:,-1] = 0
        
        wm_mask_T1 = nib.load(wm_mask[0]).get_fdata()
        wm_mask_T1[:,:,0] = 0
        wm_mask_T1[:,:,-1] = 0
        wm_mask_T2 = nib.load(wm_mask[1]).get_fdata()
        wm_mask_T2[:,:,0] = 0
        wm_mask_T2[:,:,-1] = 0
    
        for atlas_path in atlas_list_name:
            atlas_name = str(atlas_path[1])
            # if ('.nii.gz' in atlas_name):
            #     atlas_name = atlas_name.replace('.nii.gz','')
            
            atlas_file_T1 = nib.load(path_atlas_reg + "/Atlas/" + atlas_name + "_reg_on_sub" + patient_nb + ".nii.gz").get_fdata()
            atlas_file_T2 = nib.load(path_atlas_reg + "/Atlas/" + atlas_name + "_reg_on_sub" + patient_nb + "_T2.nii.gz").get_fdata()
            
            patient_file_T1 = nib.load(patient[0]).get_fdata()
            patient_file_T1[np.isnan(patient_file_T1) == True] = 0.0
            
            patient_file_T2 = nib.load(patient[1]).get_fdata()
            patient_file_T2[np.isnan(patient_file_T2) == True] = 0.0

            mask_zone_T1 = np.zeros(patient_file_T1.shape)
            mask_zone_T2 = np.zeros(patient_file_T2.shape)
            
            mask_zone_T1[atlas_file_T1 > float(atlas_path[2])] = 1
            mask_zone_T2[atlas_file_T2 > float(atlas_path[2])] = 1
            
            if(atlas_path[3] == "0" or atlas_path[3] == "2" or atlas_path[3] == "4" or atlas_path[3] == "5" or atlas_path[3] == "6"):
                mask_zone_T1 = mask_zone_T1 * brain_mask_T1
                mask_zone_T2 = mask_zone_T2 * brain_mask_T2
                
            elif(atlas_path[3] == "1" or atlas_path[3] == "3"): #WHITE MATTER
                mask_zone_T1 = mask_zone_T1 * wm_mask_T1
                mask_zone_T2 = mask_zone_T2 * wm_mask_T2

            else:
                print('Not ok again')

            mask_zone_T1[patient_file_T1 == 0] = 0
            mask_zone_T2[patient_file_T2 == 0] = 0
        
            interm_T1 = patient_file_T1*mask_zone_T1
            moyenne_T1 = np.mean(interm_T1[interm_T1 != 0])
            
            interm_T2 = patient_file_T2*mask_zone_T2
            moyenne_T2 = np.mean(interm_T2[interm_T2 != 0])
            
            percentage_change = (moyenne_T2 - moyenne_T1)*100/moyenne_T1
        
            if (math.isnan(moyenne_T1) == True or math.isnan(moyenne_T2) == True):
                moyenne_T1 = 0
                moyenne_T2 = 0

            if(np.isnan(percentage_change) == True):
                percentage_change = 0
   
            worksheet.write('A1', "Atlas names")
            worksheet.write('B1', "Mean at T1")
            worksheet.write('C1', "Mean at T2")
            worksheet.write('D1', "Percentage change bewteen T2 and T1")
            worksheet.write('A' + str(azer), atlas_path[0])
            worksheet.write('B' + str(azer), moyenne_T1)
            worksheet.write('C' + str(azer), moyenne_T2)
            worksheet.write('D' + str(azer), percentage_change)
    
            azer += 1
            
            #A RUN POUR SEULEMENT UNE METRIQUE
            atlas_name1 = str(atlas_path[1])
            if ('.nii.gz' in atlas_name1):
                atlas_name1 = atlas_name1.replace('.nii.gz', '')
            if("Cerebellar/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Cerebellar/', '')
            if("Cerebelar" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Cerebelar', 'Cerebellar')
            if("Cerebellum/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Cerebellum/', '')
            if("Harvard/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Harvard/', '')
            if("Harvard_cortex/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Harvard_cortex/', '')
            if("Lobes/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('Lobes/', '')
            if("XTRACT/" in atlas_name1):
                atlas_name1 = atlas_name1.replace('XTRACT/', '')
            if("CC/" in atlas_name1): 
                atlas_name1 = atlas_name1.replace('CC/', '')
                
            # out = nib.Nifti1Image(mask_zone_T1, affine = img.affine, header = img.header)
            # out.to_filename(path_atlas_reg + "/Mask/" + "sub" + patient_nb + "_" + atlas_name1 + "_mask_T1.nii.gz")

            # out1 = nib.Nifti1Image(mask_zone_T2, affine = img1.affine, header = img1.header)
            # out1.to_filename(path_atlas_reg + "/Mask/" + "sub" + patient_nb + "_" + atlas_name1 + "_mask_T2.nii.gz")
    
    workbook.close()
    print("Temps:", time.time() - start_time)

moyenne_par_roi("folder_path", "sub05_T1")
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:36:51 2022

@author: manou
"""

import numpy as np
import os
from pathlib import Path
# from perso_path import perso_path_string

list_dir = os.listdir("D:/EPL/MASTER/TFE/alcoolique/alcoholic_study/subjects/")

patient_list = ["sub27_E3", "sub34_E3", "sub09_E3", "sub02_E3", "sub30_E3", "sub17_E3", "sub36_E3", "sub22_E3", "sub20_E3", "sub03_E3"]
                # ["sub01_E1", "sub02_E1", "sub04_E1", "sub05_E1", "sub08_E1", "sub09_E1", "sub10_E1", "sub11_E1", 
                # "sub12_E1", "sub13_E1", "sub14_E1", "sub15_E1", "sub16_E1", "sub17_E1", "sub18_E1", "sub19_E1",      
                # "sub20_E1", "sub21_E1", "sub22_E1", "sub23_E1", "sub24_E1", "sub26_E1", "sub27_E1", "sub28_E1",
                # "sub29_E1", "sub30_E1", "sub31_E1", "sub32_E1", "sub33_E1", "sub34_E1", "sub35_E1", "sub36_E1", 
                # "sub37_E1", "sub38_E1", "sub39_E1", "sub40_E1", "sub41_E1", "sub42_E1", "sub43_E1", "sub44_E1", 
                # "sub45_E1", "sub46_E1", "sub47_E1", "sub48_E1", "sub50_E1", "sub51_E1", "sub52_E1", "sub53_E1",     
                # "sub01_E2", "sub02_E2", "sub03_E2", "sub04_E2", "sub05_E2", "sub06_E2", "sub07_E2", "sub08_E2", 
                # "sub09_E2", "sub11_E2", "sub12_E2", "sub13_E2", "sub14_E2", "sub15_E2", "sub17_E2", "sub18_E2", 
                # "sub19_E2", "sub20_E2", "sub21_E2", "sub22_E2", "sub24_E2", "sub25_E2", "sub26_E2", "sub27_E2",
                # "sub28_E2", "sub29_E2", "sub30_E2", "sub31_E2", "sub32_E2", "sub33_E2", "sub34_E2", "sub35_E2", 
                # "sub36_E2", "sub37_E2", "sub39_E2", "sub40_E2", "sub41_E2", "sub42_E2", "sub43_E2", "sub45_E2", 
                # "sub46_E2", "sub48_E2", "sub50_E2", "sub51_E2", "sub52_E2", "sub53_E2"]

for i in patient_list:
    
    bFA = False
    bMD = False
    bRD = False
    bAD = False
    
    bdiamond_fractions = False
    bdiamond_t0 = False
    bdiamond_t1 = False
    bwFA = False
    bwMD = False
    bwRD = False
    bwAD = False
    
    bfrac_csf = False
    bfrac_f0 = False
    bfrac_f1 = False
    bfrac_ftot = False
    bfvf_f0 = False
    bfvf_f1 = False
    bfvf_tot = False
    bwfvf = False
    
    bfintra = False
    bfextra = False
    bfiso = False
    bfbundle = False
    bicvf = False
    bodi = False
    
    bwm_FSL = False
    bFSL = False
    bbrain_mask = False
    bwm_AP = False
    
    micro = "D:/EPL/MASTER/TFE/alcoolique/alcoholic_study/subjects/" + i + "/dMRI/microstructure" 
    mask = "D:/EPL/MASTER/TFE/alcoolique/alcoholic_study/subjects/" + i + "/masks" 
    
    for j in os.listdir(micro + "/dti/"):
        if "FA" in j:
            bFA = True
        elif "MD" in j:
            bMD = True
        elif "AD" in j:
            bAD = True
        elif "RD" in j:
            bRD = True
   
    for j in os.listdir(micro + "/diamond/"):
        if "diamond_fractions" in j:
            bdiamond_fractions = True
        elif "diamond_t1" in j:
            bdiamond_t1 = True
        elif "diamond_t0" in j:
            bdiamond_t0 = True
        elif "wFA" in j:
            bwFA = True
        elif "wMD" in j:
            bwMD = True
        elif "wAD" in j:
            bwAD = True
        elif "wRD" in j:
            bwRD = True
            
    for j in os.listdir(micro + "/mf/"):
        if "frac_csf" in j:
            bfrac_csf = True
        elif "frac_f0" in j:
            bfrac_f0 = True
        elif "frac_f1" in j:
            bfrac_f1 = True
        elif "frac_ftot" in j:
            bfrac_ftot = True
        elif "fvf_f0" in j:
            bfvf_f0 = True
        elif "fvf_f1" in j:
            bfvf_f1 = True
        elif "fvf_tot" in j:
            bfvf_tot = True
        elif "wfvf" in j:
            bwfvf = True

    for j in os.listdir(micro + "/noddi/"):
        if "fextra" in j:
            bfextra = True 
        elif "fintra" in j:
            bfintra = True 
        elif "fiso" in j:
            bfiso = True
        elif "icvf" in j:
            bicvf = True
        elif "odi" in j:
            bodi = True
        elif "fbundle" in j:
            bfbundle = True

    for j in os.listdir(mask):
        if "E1_brain_mask" in j or "E2_brain_mask" in j or "E3_brain_mask" in j:
            bbrain_mask = True 
        elif "E1_wm_mask_AP" in j or "E2_wm_mask_AP" in j or "E3_wm_mask_AP" in j:
            bwm_AP = True 
        elif "E1_wm_mask_FSL_T1" in j or "E2_wm_mask_FSL_T1" in j or "E3_wm_mask_FSL_T1" in j:
            bwm_FSL = True

    if bFA == False:
        print("Miss FA file for " + i)
    if bMD == False:
        print("Miss MD file for " + i)
    if bRD == False:
        print("Miss RD file for " + i)
    if bAD == False:
        print("Miss AD file for " + i)
    
    if bdiamond_fractions == False:
        print("Miss bdiamond_fractions file for " + i)
    if bdiamond_t0 == False:
        print("Miss bdiamond_t0 file for " + i)
    if bdiamond_t1 == False:
        print("Miss bdiamond_t1 file for " + i)
    if bwFA == False:
        print("Miss bwFA file for " + i)
    if bwMD == False:
        print("Miss bwMD file for " + i)
    if bwRD == False:
        print("Miss bwRD file for " + i)
    if bwAD == False:
        print("Miss bwAD file for " + i)
    
    if bfrac_csf == False:
        print("Miss bfrac_csf file for " + i)
    if bfrac_f0 == False:
        print("Miss bfrac_f0 file for " + i)
    if bfrac_f1 == False:
        print("Miss bfrac_f1 file for " + i)
    if bfrac_ftot == False:
        print("Miss bfrac_ftot file for " + i)
    if bfvf_f0 == False:
        print("Miss bfvf_f0 file for " + i)
    if bfvf_f1 == False:
        print("Miss bfvf_f1 file for " + i)
    if bfvf_tot == False:
        print("Miss bfvf_tot file for " + i)
    if bwfvf == False:
        print("Miss bwfvf file for " + i)
    
    if bfintra == False:
        print("Miss bfintra file for " + i)
    if bfextra == False:
        print("Miss bfextra file for " + i)
    if bfiso == False:
        print("Miss bfiso file for " + i)
    # if bfbundle == False:
    #     print("Miss bfbundle file for " + i)
    if bicvf == False:
        print("Miss bicvf file for " + i)
    if bodi == False:
        print("Miss bodi file for " + i)
    
    if bwm_FSL == False:
        print("Miss bwm_FSL file for " + i)
    if bbrain_mask == False:
        print("Miss bbrain_mask file for " + i)
    if bwm_AP == False:
        print("Miss bwm_AP file for " + i)
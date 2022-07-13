import os
import datetime
import time
import numpy as np
from future.utils import iteritems
import subprocess

def makedir(dir_path):
    """
    Create a directory in the location specified by the dir_path and write the log in the log_path.

    :param dir_path: The path to the directory to create.
    :param log_path: The path to the log file to write verbose data.
    :param log_prefix: The prefix to use in the log file.
    """
    if not(os.path.exists(dir_path)):
        try:
            os.makedirs(dir_path)
        except OSError:
            print ("Creation of the directory %s failed" % dir_path)
        else:
            print ("Successfully created the directory %s " % dir_path)
   
   
def folder_patients(patient_numbers, folder_path, sub_files, sub_sub_files):
    for i in patient_numbers:
        out_dir = os.path.join(folder_path, "#" + i + "/")
        makedir(out_dir)
        for j in sub_files:
            out_dir_sub = os.path.join(out_dir + j + "/")
            makedir(out_dir_sub)
            if (j == "Atlas"):
                for k in sub_sub_files: 
                    out_dir_sub_sub = os.path.join(out_dir_sub + k + "/")
                    makedir(out_dir_sub_sub)

def folder_patients_bis(patient_numbers, folder_path_bis, sub_files_bis, sub_sub_files_bis, sub_sub_sub_files_bis):
    for i in patient_numbers:
        out_dir_T1 = os.path.join(folder_path_bis, "sub" + i + "_T1/")
        makedir(out_dir_T1)
        
        out_dir_T2 = os.path.join(folder_path_bis, "sub" + i + "_T2/")
        makedir(out_dir_T2)
        for j in sub_files_bis:
            out_dir_sub_T1 = os.path.join(out_dir_T1 + j + "/")
            makedir(out_dir_sub_T1)
            
            out_dir_sub_T2 = os.path.join(out_dir_T2 + j + "/")
            makedir(out_dir_sub_T2)
            if (j == "dMRI"):
                out_dir_sub_sub_T1 = os.path.join(out_dir_sub_T1 + sub_sub_files_bis + "/")
                makedir(out_dir_sub_sub_T1)
                
                out_dir_sub_sub_T2 = os.path.join(out_dir_sub_T2 + sub_sub_files_bis + "/")
                makedir(out_dir_sub_sub_T2)
                
                for m in sub_sub_sub_files_bis:
                    out_dir_sub_sub_sub_T1 = os.path.join(out_dir_sub_sub_T1 + m + "/")
                    makedir(out_dir_sub_sub_sub_T1)
                    
                    out_dir_sub_sub_sub_T2 = os.path.join(out_dir_sub_sub_T2 + m + "/")
                    makedir(out_dir_sub_sub_sub_T2)

patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]    

sub_files = ["Anat", "Atlas", "Mask", "Maps"]
sub_sub_files = ["CC", "Cerebellar", "Cerebellum", "Harvard", "Harvard_cortex", "Lobes", "XTRACT"]

folder_path = "D:/EPL/MASTER/TFE/alcoolique/Patients/" # "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Patients/"

sub_files_bis = ["dMRI", "masks"]
sub_sub_files_bis = "microstructure"
sub_sub_sub_files_bis = ["dti", "diamond", "noddi", "mf"]

folder_path_bis = "D:/EPL/MASTER/TFE/alcoolique/Alcoolique study/subjects/" # "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/subjects/"

if __name__ == '__main__':
    folder_patients(patient_numbers, folder_path, sub_files, sub_sub_files)
    folder_patients_bis(patient_numbers, folder_path_bis, sub_files_bis, sub_sub_files_bis, sub_sub_sub_files_bis)
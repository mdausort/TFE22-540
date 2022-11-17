import elikopy 
import elikopy.utils
from elikopy.individual_subject_processing import report_solo

f_path="/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/alcoholic_study/" 
dic_path="/home/users/q/d/qdessain/Script_python/fixed_rad_dist.mat"

patient_list = None#["sub02_T1", "sub04_T1", "sub05_T1", "sub08_T1", "sub09_T1", "sub11_T1", "sub12_T1", "sub13_T1", "sub14_T1", "sub15_T1", "sub17_T1", "sub18_T1", "sub19_T1", "sub20_T1", "sub21_T1", "sub22_T1", "sub24_T1", "sub26_T1", "sub27_T1", "sub28_T1", "sub30_T1", "sub31_T1", "sub32_T1", "sub33_T1", "sub34_T1", "sub35_T1", "sub36_T1", "sub37_T1", "sub39_T1", "sub40_T1", "sub41_T1", "sub42_T1", "sub43_T1", "sub45_T1", "sub46_T1", "sub02_T2", "sub04_T2", "sub05_T2", "sub08_T2", "sub09_T2", "sub11_T2", "sub12_T2", "sub13_T2", "sub14_T2", "sub15_T2", "sub17_T2", "sub18_T2", "sub19_T2", "sub20_T2", "sub21_T2", "sub22_T2", "sub24_T2", "sub26_T2", "sub27_T2", "sub28_T2", "sub30_T2", "sub31_T2", "sub32_T2", "sub33_T2", "sub34_T2", "sub35_T2", "sub36_T2", "sub37_T2", "sub39_T2", "sub40_T2", "sub41_T2", "sub42_T2", "sub43_T2", "sub45_T2", "sub46_T2"]
                                   
study = elikopy.core.Elikopy(f_path, slurm=True, slurm_email='manon.dausort@student.uclouvain.be', cuda=False)

# =============================================================================
# Patient list
# =============================================================================
study.patient_list()

# =============================================================================
# Preprocessing
# =============================================================================
# study.preproc(eddy=True,
# 	            topup=True,
#               denoising=True, 
#               mppca_legacy_denoising=True, 
#               reslice=True, 
#               gibbs=False, 
#               biasfield=False,
# 	            patient_list_m=patient_list, 
#               qc_reg=True,
# 	            starting_state="post_report", 
#               report=True)

# =============================================================================
# Mask de matière blanche
# =============================================================================
# study.white_mask(patient_list_m=patient_list, corr_gibbs=True, cpus=2, debug=False) 
   
# =============================================================================
# Modèles microstructuraux 
# =============================================================================
# study.dti(patient_list_m=patient_list)
# study.noddi(use_wm_mask=False, patient_list_m=patient_list, cpus=4)
# study.fingerprinting(dic_path, patient_list_m=patient_list, cpus=8, CSD_bvalue=6000)
# study.diamond(patient_list_m=patient_list,slurm_timeout="30:00:00",cpus=8)

# =============================================================================
# Statistiques
# =============================================================================
# grp1=[1]
# grp2=[2]

# study.regall_FA(grp1=grp1,grp2=grp2, registration_type="-T", postreg_type="-S", prestats_treshold=0.2, cpus=8)

# metrics={'_noddi_odi':'noddi','_mf_fvf_tot':'mf'}
# study.regall(grp1=grp1,grp2=grp2, metrics_dic=metrics)
# study.randomise_all(randomise_numberofpermutation=0,skeletonised=True,metrics_dic=metrics,regionWiseMean=True,cpus=1,slurm_timeout="1:00:00")

# =============================================================================
# Export
# =============================================================================
# study.export(tractography=True, raw=False, preprocessing=False, dti=True, noddi=False, diamond=False, mf=False, wm_mask=False, report=False, preprocessed_first_b0=False, patient_list_m=None)
# elikopy.utils.merge_all_reports(f_path)

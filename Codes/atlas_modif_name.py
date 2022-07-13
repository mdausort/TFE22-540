"""
Created on Thu Mar 17 12:15:10 2022

@author: Fauston
"""

import numpy as np


def get_atlas_list(onlywhite=False, with_CC=True):
    
    """
    Parameters
    ----------
    onlywhite : Boolean, optional
        To choose the type of matter: true for white matter atlases only and false for all atlases. The default is False.

    Returns
    -------
    atlas_list : List of tuples. 
        The latter contains the path of the atlas, its threshold and a number used to descriminate the different areas.
    """
    
    # perso_path = "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Atlas/"
    
    cortico_ponto_cerebellum_left = "Cerebellar/Cortico_Ponto_Cerebellum_Left.nii.gz"
    cortico_ponto_cerebellum_right = "Cerebellar/Cortico_Ponto_Cerebellum_Right.nii.gz"
    Inferior_Cerebellar_Pedunculus_Left = "Cerebellar/Inferior_Cerebellar_Pedunculus_Left.nii.gz"
    Inferior_Cerebellar_Pedunculus_Right = "Cerebellar/Inferior_Cerebellar_Pedunculus_Right.nii.gz"
    Superior_Cerebelar_Pedunculus_Left = "Cerebellar/Superior_Cerebelar_Pedunculus_Left.nii.gz"
    Superior_Cerebelar_Pedunculus_Right = "Cerebellar/Superior_Cerebelar_Pedunculus_Right.nii.gz"
    
    cerebellum_mniflirt_prob_Left_Crus_I = "Cerebellum/cerebellum_mniflirt_prob_Left_Crus_I.nii.gz"
    cerebellum_mniflirt_prob_Left_Crus_II = "Cerebellum/cerebellum_mniflirt_prob_Left_Crus_II.nii.gz"
    cerebellum_mniflirt_prob_Left_I_IV = "Cerebellum/cerebellum_mniflirt_prob_Left_I-IV.nii.gz"
    cerebellum_mniflirt_prob_Left_IX = "Cerebellum/cerebellum_mniflirt_prob_Left_IX.nii.gz"
    cerebellum_mniflirt_prob_Left_V = "Cerebellum/cerebellum_mniflirt_prob_Left_V.nii.gz"
    cerebellum_mniflirt_prob_Left_VI = "Cerebellum/cerebellum_mniflirt_prob_Left_VI.nii.gz"
    cerebellum_mniflirt_prob_Left_VIIb = "Cerebellum/cerebellum_mniflirt_prob_Left_VIIb.nii.gz"
    cerebellum_mniflirt_prob_Left_VIIIa = "Cerebellum/cerebellum_mniflirt_prob_Left_VIIIa.nii.gz"
    cerebellum_mniflirt_prob_Left_VIIIb = "Cerebellum/cerebellum_mniflirt_prob_Left_VIIIb.nii.gz"
    cerebellum_mniflirt_prob_Left_X = "Cerebellum/cerebellum_mniflirt_prob_Left_X.nii.gz"
    cerebellum_mniflirt_prob_Right_Crus_I = "Cerebellum/cerebellum_mniflirt_prob_Right_Crus_I.nii.gz"
    cerebellum_mniflirt_prob_Right_Crus_II = "Cerebellum/cerebellum_mniflirt_prob_Right_Crus_II.nii.gz"
    cerebellum_mniflirt_prob_Right_I_IV = "Cerebellum/cerebellum_mniflirt_prob_Right_I-IV.nii.gz"
    cerebellum_mniflirt_prob_Right_IX = "Cerebellum/cerebellum_mniflirt_prob_Right_IX.nii.gz"
    cerebellum_mniflirt_prob_Right_V = "Cerebellum/cerebellum_mniflirt_prob_Right_V.nii.gz"
    cerebellum_mniflirt_prob_Right_VI = "Cerebellum/cerebellum_mniflirt_prob_Right_VI.nii.gz"
    cerebellum_mniflirt_prob_Right_VIIb = "Cerebellum/cerebellum_mniflirt_prob_Right_VIIb.nii.gz"
    cerebellum_mniflirt_prob_Right_VIIIa = "Cerebellum/cerebellum_mniflirt_prob_Right_VIIIa.nii.gz"
    cerebellum_mniflirt_prob_Right_VIIIb = "Cerebellum/cerebellum_mniflirt_prob_Right_VIIIb.nii.gz"
    cerebellum_mniflirt_prob_Right_X = "Cerebellum/cerebellum_mniflirt_prob_Right_X.nii.gz"
    cerebellum_mniflirt_prob_Vermis = "Cerebellum/cerebellum_mniflirt_prob_Vermis.nii.gz"
    
    harvardoxford_subcortical_prob_Brain_Stem = "Harvard/harvardoxford-subcortical_prob_Brain-Stem.nii.gz"
    harvardoxford_subcortical_prob_Left_Amygdala = "Harvard/harvardoxford-subcortical_prob_Left Amygdala.nii.gz"
    harvardoxford_subcortical_prob_Left_Caudate = "Harvard/harvardoxford-subcortical_prob_Left Caudate.nii.gz"
    harvardoxford_subcortical_prob_Left_Cerebral_White_Matter = "Harvard/harvardoxford-subcortical_prob_Left Cerebral White Matter.nii.gz"
    harvardoxford_subcortical_prob_Left_Hippocampus = "Harvard/harvardoxford-subcortical_prob_Left Hippocampus.nii.gz"
    harvardoxford_subcortical_prob_Left_Thalamus = "Harvard/harvardoxford-subcortical_prob_Left Thalamus.nii.gz"
    harvardoxford_subcortical_prob_Right_Amygdala = "Harvard/harvardoxford-subcortical_prob_Right Amygdala.nii.gz"
    harvardoxford_subcortical_prob_Right_Caudate = "Harvard/harvardoxford-subcortical_prob_Right Caudate.nii.gz"
    harvardoxford_subcortical_prob_Right_Cerebral_White_Matter = "Harvard/harvardoxford-subcortical_prob_Right Cerebral White Matter.nii.gz"
    harvardoxford_subcortical_prob_Right_Hippocampus = "Harvard/harvardoxford-subcortical_prob_Right Hippocampus.nii.gz"
    harvardoxford_subcortical_prob_Right_Thalamus = "Harvard/harvardoxford-subcortical_prob_Right Thalamus.nii.gz"
    harvardoxford_subcortical_prob_Left_Putamen = "Harvard/harvardoxford-subcortical_prob_Left Putamen.nii.gz"
    harvardoxford_subcortical_prob_Right_Putamen = "Harvard/harvardoxford-subcortical_prob_Right Putamen.nii.gz"
    
    harvardoxford_cortical_prob_Angular_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Angular_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Central_Opercular_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Central_Opercular_Cortex.nii.gz"
    harvardoxford_cortical_prob_Cingulate_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Cingulate_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Cingulate_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Cingulate_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Cuneal_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Cuneal_Cortex.nii.gz"
    harvardoxford_cortical_prob_Frontal_Medial_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Frontal_Medial_Cortex.nii.gz"
    harvardoxford_cortical_prob_Frontal_Operculum_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Frontal_Operculum_Cortex.nii.gz"
    harvardoxford_cortical_prob_Frontal_Orbital_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Frontal_Orbital_Cortex.nii.gz"
    harvardoxford_cortical_prob_Frontal_Pole = "Harvard_cortex/harvardoxford-cortical_prob_Frontal_Pole.nii.gz"
    harvardoxford_cortical_prob_Heschl_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Heschl_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_opercularis = "Harvard_cortex/harvardoxford-cortical_prob_Inferior_Frontal_Gyrus_pars_opercularis.nii.gz"
    harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_triangularis = "Harvard_cortex/harvardoxford-cortical_prob_Inferior_Frontal_Gyrus_pars_triangularis.nii.gz"
    harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Inferior_Temporal_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Inferior_Temporal_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_temporooccipital_part = "Harvard_cortex/harvardoxford-cortical_prob_Inferior_Temporal_Gyrus_temporooccipital_part.nii.gz"
    harvardoxford_cortical_prob_Insular_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Insular_Cortex.nii.gz"
    harvardoxford_cortical_prob_Intracalcarine_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Intracalcarine_Cortex.nii.gz"
    harvardoxford_cortical_prob_Juxtapositional_Lobule_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Juxtapositional_Lobule_Cortex_(formerly_Supplementary_Motor_Cortex).nii.gz"
    harvardoxford_cortical_prob_Lateral_Occipital_Cortex_inferior = "Harvard_cortex/harvardoxford-cortical_prob_Lateral_Occipital_Cortex_inferior.nii.gz"
    harvardoxford_cortical_prob_Lateral_Occipital_Cortex_superior = "Harvard_cortex/harvardoxford-cortical_prob_Lateral_Occipital_Cortex_superior.nii.gz"
    harvardoxford_cortical_prob_Lingual_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Lingual_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Middle_Frontal_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Middle_Frontal_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Middle_Temporal_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Middle_Temporal_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Middle_Temporal_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Middle_Temporal_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Middle_Temporal_Gyrus_temporooccipital_part = "Harvard_cortex/harvardoxford-cortical_prob_Middle_Temporal_Gyrus_temporooccipital_part.nii.gz"
    harvardoxford_cortical_prob_Occipital_Fusiform_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Occipital_Fusiform_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Occipital_Pole = "Harvard_cortex/harvardoxford-cortical_prob_Occipital_Pole.nii.gz"
    harvardoxford_cortical_prob_Paracingulate_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Paracingulate_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Parahippocampal_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Parahippocampal_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Parahippocampal_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Parahippocampal_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Parietal_Operculum_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Parietal_Operculum_Cortex.nii.gz"
    harvardoxford_cortical_prob_Planum_Polare = "Harvard_cortex/harvardoxford-cortical_prob_Planum_Polare.nii.gz"
    harvardoxford_cortical_prob_Planum_Temporale = "Harvard_cortex/harvardoxford-cortical_prob_Planum_Temporale.nii.gz"
    harvardoxford_cortical_prob_Postcentral_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Postcentral_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Precentral_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Precentral_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Precuneous_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Precuneous_Cortex.nii.gz"
    harvardoxford_cortical_prob_Subcallosal_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Subcallosal_Cortex.nii.gz"
    harvardoxford_cortical_prob_Superior_Frontal_Gyrus = "Harvard_cortex/harvardoxford-cortical_prob_Superior_Frontal_Gyrus.nii.gz"
    harvardoxford_cortical_prob_Superior_Parietal_Lobule = "Harvard_cortex/harvardoxford-cortical_prob_Superior_Parietal_Lobule.nii.gz"
    harvardoxford_cortical_prob_Superior_Temporal_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Superior_Temporal_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Superior_Temporal_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Superior_Temporal_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Supracalcarine_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Supracalcarine_Cortex.nii.gz"
    harvardoxford_cortical_prob_Supramarginal_Gyrus_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Supramarginal_Gyrus_anterior.nii.gz"
    harvardoxford_cortical_prob_Supramarginal_Gyrus_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Supramarginal_Gyrus_posterior.nii.gz"
    harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_anterior = "Harvard_cortex/harvardoxford-cortical_prob_Temporal_Fusiform_Cortex_anterior.nii.gz"
    harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_posterior = "Harvard_cortex/harvardoxford-cortical_prob_Temporal_Fusiform_Cortex_posterior.nii.gz"
    harvardoxford_cortical_prob_Temporal_Occipital_Fusiform_Cortex = "Harvard_cortex/harvardoxford-cortical_prob_Temporal_Occipital_Fusiform_Cortex.nii.gz"
    harvardoxford_cortical_prob_Temporal_Pole = "Harvard_cortex/harvardoxford-cortical_prob_Temporal_Pole.nii.gz"
        
    mni_prob_Frontal_Lobe = "Lobes/mni_prob_Frontal_Lobe.nii.gz"
    mni_prob_Insula = "Lobes/mni_prob_Insula.nii.gz"
    mni_prob_Occipital_Lobe = "Lobes/mni_prob_Occipital_Lobe.nii.gz"
    mni_prob_Parietal_Lobe = "Lobes/mni_prob_Parietal_Lobe.nii.gz"
    mni_prob_Temporal_Lobe = "Lobes/mni_prob_Temporal_Lobe.nii.gz"
    
    xtract_prob_Acoustic_Radiation_L = "XTRACT/xtract_prob_Acoustic_Radiation_L.nii.gz"
    xtract_prob_Acoustic_Radiation_R = "XTRACT/xtract_prob_Acoustic_Radiation_R.nii.gz"
    xtract_prob_Anterior_Commissure = "XTRACT/xtract_prob_Anterior_Commissure.nii.gz"
    xtract_prob_Anterior_Thalamic_Radiation_L = "XTRACT/xtract_prob_Anterior_Thalamic_Radiation_L.nii.gz"
    xtract_prob_Anterior_Thalamic_Radiation_R = "XTRACT/xtract_prob_Anterior_Thalamic_Radiation_R.nii.gz"
    xtract_prob_Arcuate_Fasciculus_L = "XTRACT/xtract_prob_Arcuate_Fasciculus_L.nii.gz"
    xtract_prob_Arcuate_Fasciculus_R = "XTRACT/xtract_prob_Arcuate_Fasciculus_R.nii.gz"
    xtract_prob_Cingulum_subsection_Dorsal_L = "XTRACT/xtract_prob_Cingulum_subsection_Dorsal_L.nii.gz"
    xtract_prob_Cingulum_subsection_Dorsal_R = "XTRACT/xtract_prob_Cingulum_subsection_Dorsal_R.nii.gz"
    xtract_prob_Cingulum_subsection_Peri_genual_L = "XTRACT/xtract_prob_Cingulum_subsection_Peri-genual_L.nii.gz"
    xtract_prob_Cingulum_subsection_Peri_genual_R = "XTRACT/xtract_prob_Cingulum_subsection_Peri-genual_R.nii.gz"
    xtract_prob_Cingulum_subsection_Temporal_L = "XTRACT/xtract_prob_Cingulum_subsection_Temporal_L.nii.gz"
    xtract_prob_Cingulum_subsection_Temporal_R = "XTRACT/xtract_prob_Cingulum_subsection_Temporal_R.nii.gz"
    xtract_prob_Corticospinal_Tract_L = "XTRACT/xtract_prob_Corticospinal_Tract_L.nii.gz"
    xtract_prob_Corticospinal_Tract_R = "XTRACT/xtract_prob_Corticospinal_Tract_R.nii.gz"
    xtract_prob_Forceps_Major = "XTRACT/xtract_prob_Forceps_Major.nii.gz"
    xtract_prob_Forceps_Minor = "XTRACT/xtract_prob_Forceps_Minor.nii.gz"
    xtract_prob_Fornix_L = "XTRACT/xtract_prob_Fornix_L.nii.gz"
    xtract_prob_Fornix_R = "XTRACT/xtract_prob_Fornix_R.nii.gz"
    xtract_prob_Frontal_Aslant_Tract_L = "XTRACT/xtract_prob_Frontal_Aslant_Tract_L.nii.gz"
    xtract_prob_Frontal_Aslant_Tract_R = "XTRACT/xtract_prob_Frontal_Aslant_Tract_R.nii.gz"
    xtract_prob_Inferior_Fronto_Occipital_Fasciculus_L = "XTRACT/xtract_prob_Inferior_Fronto-Occipital_Fasciculus_L.nii.gz"
    xtract_prob_Inferior_Fronto_Occipital_Fasciculus_R = "XTRACT/xtract_prob_Inferior_Fronto-Occipital_Fasciculus_R.nii.gz"
    xtract_prob_Inferior_Longitudinal_Fasciculus_L = "XTRACT/xtract_prob_Inferior_Longitudinal_Fasciculus_L.nii.gz"
    xtract_prob_Inferior_Longitudinal_Fasciculus_R = "XTRACT/xtract_prob_Inferior_Longitudinal_Fasciculus_R.nii.gz"
    xtract_prob_Middle_Cerebellar_Peduncle = "XTRACT/xtract_prob_Middle_Cerebellar_Peduncle.nii.gz"
    xtract_prob_Middle_Longitudinal_Fasciculus_L = "XTRACT/xtract_prob_Middle_Longitudinal_Fasciculus_L.nii.gz"
    xtract_prob_Middle_Longitudinal_Fasciculus_R = "XTRACT/xtract_prob_Middle_Longitudinal_Fasciculus_R.nii.gz"
    xtract_prob_Optic_Radiation_L = "XTRACT/xtract_prob_Optic_Radiation_L.nii.gz"
    xtract_prob_Optic_Radiation_R = "XTRACT/xtract_prob_Optic_Radiation_R.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_1_L = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_1_L.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_1_R = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_1_R.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_2_L = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_2_L.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_2_R = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_2_R.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_3_L = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_3_L.nii.gz"
    xtract_prob_Superior_Longitudinal_Fasciculus_3_R = "XTRACT/xtract_prob_Superior_Longitudinal_Fasciculus_3_R.nii.gz"
    xtract_prob_Superior_Thalamic_Radiation_L = "XTRACT/xtract_prob_Superior_Thalamic_Radiation_L.nii.gz"
    xtract_prob_Superior_Thalamic_Radiation_R = "XTRACT/xtract_prob_Superior_Thalamic_Radiation_R.nii.gz"
    xtract_prob_Uncinate_Fasciculus_L = "XTRACT/xtract_prob_Uncinate_Fasciculus_L.nii.gz"
    xtract_prob_Uncinate_Fasciculus_R = "XTRACT/xtract_prob_Uncinate_Fasciculus_R.nii.gz"
    xtract_prob_Vertical_Occipital_Fasciculus_L = "XTRACT/xtract_prob_Vertical_Occipital_Fasciculus_L.nii.gz"
    xtract_prob_Vertical_Occipital_Fasciculus_R = "XTRACT/xtract_prob_Vertical_Occipital_Fasciculus_R.nii.gz"

    corpus_callosum = "CC/Corpus_callosum_hand_drawn_morpho.nii.gz"
    corpus_callosum_genu = "CC/Corpus_callosum_genu.nii.gz"
    corpus_callosum_anterior_midbody = "CC/Corpus_callosum_anterior_midbody.nii.gz"
    corpus_callosum_posterior_midbody = "CC/Corpus_callosum_posterior_midbody.nii.gz"
    corpus_callosum_isthmus = "CC/Corpus_callosum_isthmus.nii.gz"
    corpus_callosum_splenium = "CC/Corpus_callosum_splenium.nii.gz"
    
    # THRESHOLD
    seuil_cerebellar = 0.2
    seuil_cerebellum = 50
    seuil_xtract = 30
    seuil_harvard = 30
    seuil_lobes = 30
    seuil_cortex = 30
    seuil_CC = 0
    
    #NUMBER : 0 = GM
    #         1 = WM
    #         2 = SUBCORTICAL
    #         3 = PEDUNCULUS (CEREBELLAR)
    #         4 = CEREBELLUM
    #         5 = LOBES
    #         6 = CC
    
    if (onlywhite==False):
        if(with_CC==True):
            atlas_list = [
                [cortico_ponto_cerebellum_left, seuil_cerebellar, 3],
                [cortico_ponto_cerebellum_right, seuil_cerebellar, 3],
                [Inferior_Cerebellar_Pedunculus_Left, seuil_cerebellar, 3],
                [Inferior_Cerebellar_Pedunculus_Right, seuil_cerebellar, 3],
                [Superior_Cerebelar_Pedunculus_Left, seuil_cerebellar, 3],
                [Superior_Cerebelar_Pedunculus_Right, seuil_cerebellar, 3],
            
                [cerebellum_mniflirt_prob_Left_Crus_I, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_Crus_II, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_I_IV, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_IX, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_V, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_VI, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_VIIb, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_VIIIa, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_VIIIb, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Left_X, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_Crus_I, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_Crus_II, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_I_IV, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_IX, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_V, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_VI, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_VIIb, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_VIIIa, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_VIIIb, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Right_X, seuil_cerebellum, 4],
                [cerebellum_mniflirt_prob_Vermis, seuil_cerebellum, 4],
            
                [harvardoxford_subcortical_prob_Brain_Stem, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Amygdala, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Caudate, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Cerebral_White_Matter, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Hippocampus, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Thalamus, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Amygdala, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Caudate, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Cerebral_White_Matter, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Hippocampus, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Thalamus, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Left_Putamen, seuil_harvard, 2],
                [harvardoxford_subcortical_prob_Right_Putamen, seuil_harvard, 2],
            
                [harvardoxford_cortical_prob_Angular_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Central_Opercular_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Cingulate_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Cingulate_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Cuneal_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Frontal_Medial_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Frontal_Operculum_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Frontal_Orbital_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Frontal_Pole, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Heschl_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_opercularis, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_triangularis, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_temporooccipital_part, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Insular_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Intracalcarine_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Juxtapositional_Lobule_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Lateral_Occipital_Cortex_inferior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Lateral_Occipital_Cortex_superior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Lingual_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Middle_Frontal_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_temporooccipital_part, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Occipital_Fusiform_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Occipital_Pole, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Paracingulate_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Parahippocampal_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Parahippocampal_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Parietal_Operculum_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Planum_Polare, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Planum_Temporale, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Postcentral_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Precentral_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Precuneous_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Subcallosal_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Superior_Frontal_Gyrus, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Superior_Parietal_Lobule, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Superior_Temporal_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Superior_Temporal_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Supracalcarine_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Supramarginal_Gyrus_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Supramarginal_Gyrus_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_anterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_posterior, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Temporal_Occipital_Fusiform_Cortex, seuil_cortex, 0],
                [harvardoxford_cortical_prob_Temporal_Pole, seuil_cortex, 0],
                
                [mni_prob_Frontal_Lobe, seuil_lobes, 5],
                [mni_prob_Insula, seuil_lobes, 5],
                [mni_prob_Occipital_Lobe, seuil_lobes, 5],
                [mni_prob_Parietal_Lobe, seuil_lobes, 5],
                [mni_prob_Temporal_Lobe, seuil_lobes, 5],
            
                [xtract_prob_Acoustic_Radiation_L, seuil_xtract, 1],
                [xtract_prob_Acoustic_Radiation_R, seuil_xtract, 1],
                [xtract_prob_Anterior_Commissure, seuil_xtract, 1],
                [xtract_prob_Anterior_Thalamic_Radiation_L, seuil_xtract, 1],
                [xtract_prob_Anterior_Thalamic_Radiation_R, seuil_xtract, 1],
                [xtract_prob_Arcuate_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Arcuate_Fasciculus_R, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Dorsal_L, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Dorsal_R, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Peri_genual_L, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Peri_genual_R, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Temporal_L, seuil_xtract, 1],
                [xtract_prob_Cingulum_subsection_Temporal_R, seuil_xtract, 1],
                [xtract_prob_Corticospinal_Tract_L, seuil_xtract, 1],
                [xtract_prob_Corticospinal_Tract_R, seuil_xtract, 1],
                [xtract_prob_Forceps_Major, seuil_xtract, 1],
                [xtract_prob_Forceps_Minor, seuil_xtract, 1],
                [xtract_prob_Fornix_L, seuil_xtract, 1],
                [xtract_prob_Fornix_R, seuil_xtract, 1],
                [xtract_prob_Frontal_Aslant_Tract_L, seuil_xtract, 1],
                [xtract_prob_Frontal_Aslant_Tract_R, seuil_xtract, 1],
                [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_R, seuil_xtract, 1],
                [xtract_prob_Inferior_Longitudinal_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Inferior_Longitudinal_Fasciculus_R, seuil_xtract, 1],
                [xtract_prob_Middle_Cerebellar_Peduncle, seuil_xtract, 1],
                [xtract_prob_Middle_Longitudinal_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Middle_Longitudinal_Fasciculus_R, seuil_xtract, 1],
                [xtract_prob_Optic_Radiation_L, seuil_xtract, 1],
                [xtract_prob_Optic_Radiation_R, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_1_L, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_1_R, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_2_L, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_2_R, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_3_L, seuil_xtract, 1],
                [xtract_prob_Superior_Longitudinal_Fasciculus_3_R, seuil_xtract, 1],
                [xtract_prob_Superior_Thalamic_Radiation_L, seuil_xtract, 1],
                [xtract_prob_Superior_Thalamic_Radiation_R, seuil_xtract, 1],
                [xtract_prob_Uncinate_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Uncinate_Fasciculus_R, seuil_xtract, 1],
                [xtract_prob_Vertical_Occipital_Fasciculus_L, seuil_xtract, 1],
                [xtract_prob_Vertical_Occipital_Fasciculus_R, seuil_xtract, 1],
                
                [corpus_callosum, seuil_CC,6],
                [corpus_callosum_genu, seuil_CC, 6],
                [corpus_callosum_anterior_midbody , seuil_CC, 6],
                [corpus_callosum_posterior_midbody, seuil_CC, 6],
                [corpus_callosum_isthmus, seuil_CC, 6],
                [corpus_callosum_splenium, seuil_CC ,6]
            ]
        else: 
            atlas_list = [
            [cortico_ponto_cerebellum_left, seuil_cerebellar, 3],
            [cortico_ponto_cerebellum_right, seuil_cerebellar, 3],
            [Inferior_Cerebellar_Pedunculus_Left, seuil_cerebellar, 3],
            [Inferior_Cerebellar_Pedunculus_Right, seuil_cerebellar, 3],
            [Superior_Cerebelar_Pedunculus_Left, seuil_cerebellar, 3],
            [Superior_Cerebelar_Pedunculus_Right, seuil_cerebellar, 3],
        
            [cerebellum_mniflirt_prob_Left_Crus_I, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_Crus_II, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_I_IV, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_IX, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_V, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VI, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIIa, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_X, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_Crus_I, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_Crus_II, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_I_IV, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_IX, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_V, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VI, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIIa, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_X, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Vermis, seuil_cerebellum, 4],
        
            [harvardoxford_subcortical_prob_Brain_Stem, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Amygdala, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Caudate, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Cerebral_White_Matter, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Hippocampus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Thalamus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Amygdala, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Caudate, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Cerebral_White_Matter, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Hippocampus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Thalamus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Putamen, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Putamen, seuil_harvard, 2],
        
            [harvardoxford_cortical_prob_Angular_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Central_Opercular_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Cingulate_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Cingulate_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Cuneal_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Frontal_Medial_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Frontal_Operculum_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Frontal_Orbital_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Frontal_Pole, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Heschl_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_opercularis, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Inferior_Frontal_Gyrus_pars_triangularis, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Inferior_Temporal_Gyrus_temporooccipital_part, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Insular_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Intracalcarine_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Juxtapositional_Lobule_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Lateral_Occipital_Cortex_inferior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Lateral_Occipital_Cortex_superior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Lingual_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Middle_Frontal_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Middle_Temporal_Gyrus_temporooccipital_part, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Occipital_Fusiform_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Occipital_Pole, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Paracingulate_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Parahippocampal_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Parahippocampal_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Parietal_Operculum_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Planum_Polare, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Planum_Temporale, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Postcentral_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Precentral_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Precuneous_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Subcallosal_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Superior_Frontal_Gyrus, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Superior_Parietal_Lobule, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Superior_Temporal_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Superior_Temporal_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Supracalcarine_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Supramarginal_Gyrus_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Supramarginal_Gyrus_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_anterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Temporal_Fusiform_Cortex_posterior, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Temporal_Occipital_Fusiform_Cortex, seuil_cortex, 0],
            [harvardoxford_cortical_prob_Temporal_Pole, seuil_cortex, 0],
            
            [mni_prob_Frontal_Lobe, seuil_lobes, 5],
            [mni_prob_Insula, seuil_lobes, 5],
            [mni_prob_Occipital_Lobe, seuil_lobes, 5],
            [mni_prob_Parietal_Lobe, seuil_lobes, 5],
            [mni_prob_Temporal_Lobe, seuil_lobes, 5],
        
            [xtract_prob_Acoustic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Acoustic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Anterior_Commissure, seuil_xtract, 1],
            [xtract_prob_Anterior_Thalamic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Anterior_Thalamic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Arcuate_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Arcuate_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Dorsal_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Dorsal_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Peri_genual_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Peri_genual_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Temporal_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Temporal_R, seuil_xtract, 1],
            [xtract_prob_Corticospinal_Tract_L, seuil_xtract, 1],
            [xtract_prob_Corticospinal_Tract_R, seuil_xtract, 1],
            [xtract_prob_Forceps_Major, seuil_xtract, 1],
            [xtract_prob_Forceps_Minor, seuil_xtract, 1],
            [xtract_prob_Fornix_L, seuil_xtract, 1],
            [xtract_prob_Fornix_R, seuil_xtract, 1],
            [xtract_prob_Frontal_Aslant_Tract_L, seuil_xtract, 1],
            [xtract_prob_Frontal_Aslant_Tract_R, seuil_xtract, 1],
            [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Inferior_Longitudinal_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Inferior_Longitudinal_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Middle_Cerebellar_Peduncle, seuil_xtract, 1],
            [xtract_prob_Middle_Longitudinal_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Middle_Longitudinal_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Optic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Optic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_1_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_1_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_2_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_2_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_3_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_3_R, seuil_xtract, 1],
            [xtract_prob_Superior_Thalamic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Superior_Thalamic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Uncinate_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Uncinate_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Vertical_Occipital_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Vertical_Occipital_Fasciculus_R, seuil_xtract, 1],
        
        ]
    else : 
        atlas_list = [
            [cortico_ponto_cerebellum_left, seuil_cerebellar, 3],
            [cortico_ponto_cerebellum_right, seuil_cerebellar, 3],
            [Inferior_Cerebellar_Pedunculus_Left, seuil_cerebellar,3],
            [Inferior_Cerebellar_Pedunculus_Right, seuil_cerebellar, 3],
            [Superior_Cerebelar_Pedunculus_Left, seuil_cerebellar, 3],
            [Superior_Cerebelar_Pedunculus_Right, seuil_cerebellar, 3],
        
            [cerebellum_mniflirt_prob_Left_Crus_I, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_Crus_II, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_I_IV, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_IX, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_V, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VI, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIIa, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_VIIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Left_X, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_Crus_I, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_Crus_II, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_I_IV, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_IX, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_V, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VI, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIIa, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_VIIIb, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Right_X, seuil_cerebellum, 4],
            [cerebellum_mniflirt_prob_Vermis, seuil_cerebellum, 4],

            [harvardoxford_subcortical_prob_Brain_Stem, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Amygdala, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Caudate, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Cerebral_White_Matter, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Hippocampus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Thalamus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Amygdala, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Caudate, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Cerebral_White_Matter, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Hippocampus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Thalamus, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Left_Putamen, seuil_harvard, 2],
            [harvardoxford_subcortical_prob_Right_Putamen, seuil_harvard, 2],
        
            [xtract_prob_Acoustic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Acoustic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Anterior_Commissure, seuil_xtract, 1],
            [xtract_prob_Anterior_Thalamic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Anterior_Thalamic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Arcuate_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Arcuate_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Dorsal_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Dorsal_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Peri_genual_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Peri_genual_R, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Temporal_L, seuil_xtract, 1],
            [xtract_prob_Cingulum_subsection_Temporal_R, seuil_xtract, 1],
            [xtract_prob_Corticospinal_Tract_L, seuil_xtract, 1],
            [xtract_prob_Corticospinal_Tract_R, seuil_xtract, 1],
            [xtract_prob_Forceps_Major, seuil_xtract, 1],
            [xtract_prob_Forceps_Minor, seuil_xtract, 1],
            [xtract_prob_Fornix_L, seuil_xtract, 1],
            [xtract_prob_Fornix_R, seuil_xtract, 1],
            [xtract_prob_Frontal_Aslant_Tract_L, seuil_xtract, 1],
            [xtract_prob_Frontal_Aslant_Tract_R, seuil_xtract, 1],
            [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Inferior_Fronto_Occipital_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Inferior_Longitudinal_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Inferior_Longitudinal_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Middle_Cerebellar_Peduncle, seuil_xtract, 1],
            [xtract_prob_Middle_Longitudinal_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Middle_Longitudinal_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Optic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Optic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_1_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_1_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_2_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_2_R, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_3_L, seuil_xtract, 1],
            [xtract_prob_Superior_Longitudinal_Fasciculus_3_R, seuil_xtract, 1],
            [xtract_prob_Superior_Thalamic_Radiation_L, seuil_xtract, 1],
            [xtract_prob_Superior_Thalamic_Radiation_R, seuil_xtract, 1],
            [xtract_prob_Uncinate_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Uncinate_Fasciculus_R, seuil_xtract, 1],
            [xtract_prob_Vertical_Occipital_Fasciculus_L, seuil_xtract, 1],
            [xtract_prob_Vertical_Occipital_Fasciculus_R, seuil_xtract, 1],
            
            [corpus_callosum, seuil_CC,6],
            [corpus_callosum_genu , seuil_CC, 6],
            [corpus_callosum_anterior_midbody , seuil_CC, 6],
            [corpus_callosum_posterior_midbody, seuil_CC, 6],
            [corpus_callosum_isthmus, seuil_CC, 6],
            [corpus_callosum_splenium, seuil_CC ,6]
        ]

    return atlas_list

def get_corr_atlas_list(atlas_list):
    
    """
    Parameters
    ----------
    atlas_list : List of tuples. 
        List of tuples coming from get_atlas_list() function.

    Returns
    -------
    atlas_name : List of tuples.
        Same list of tuples of atlas list but with an extra component in the tuple corresponding to a corrected name of the atlas.
    """
    
    atlas_name = np.array(["altas_corr","atlas", 0, 0])

    for i in range(len(atlas_list)):
        name = (atlas_list[i])[0]
        if("xtract" in name):
            name = name.replace('xtract_prob_', '')
        if("harvardoxford" in name):
            name = name.replace('harvardoxford-subcortical_', '')
            name = name.replace('harvardoxford-cortical_', '')
            name = name.replace('prob_', '')
        if("mni_" in name):
            name = name.replace('mni_prob_', '')
        if("cerebellum_mniflirt_prob_" in name):
            name = name.replace('mniflirt_prob_', '')
        if("Cerebellar/" in name):
            name = name.replace('Cerebellar/', '')
        if("Cerebelar" in name):
            name = name.replace('Cerebelar', 'Cerebellar')
        if("Cerebellum/" in name):
            name = name.replace('Cerebellum/', '')
        if("Harvard/" in name):
            name = name.replace('Harvard/', '')
        if("Harvard_cortex/" in name):
            name = name.replace('Harvard_cortex/', '')
        if("Lobes/" in name):
            name = name.replace('Lobes/', '')
        if("XTRACT/" in name):
            name = name.replace('XTRACT/', '')
        if("CC/" in name): 
            name = name.replace('CC/', '')
        if("Juxtapositional" in name):
            name = name.replace('(formerly_Supplementary_Motor_Cortex)','')
        if("cerebellum" in name):
            name = name.replace('cerebellum','Cerebellum')
        if("Amygdala" in name):
            name = name.replace(' Amygdala','Amygdala')
        if("Thalamus" in name):
            name = name.replace(' Thalamus','Thalamus')
        if("Caudate" in name):
            name = name.replace(' Caudate','Caudate')
        if("Cerebral" in name):
            name = name.replace(' Cerebral','Cerebral')
        if("Hippocampus" in name):
            name = name.replace(' Hippocampus','Hippocampus')
        if('Putamen' in name):
            name = name.replace(' Putamen','Putamen')
        if("Right" in name):
            name = name.replace('Right','')
            name = name + " R"
        if("Left" in name):
            name = name.replace('Left','')
            name = name + " L"
        if("_hand_drawn_morpho" in name):
            name = name.replace('_hand_drawn_morpho', '')
        name = name.replace('.nii.gz', '')
        name = name.replace('_', ' ')
        
        vecteur = np.array([name, (atlas_list[i])[0], (atlas_list[i])[1], (atlas_list[i])[2]])
        atlas_name = np.append(atlas_name, vecteur, axis=0)
    
    atlas_name = np.reshape(atlas_name, ((len(atlas_list)+1),4))
    atlas_name = np.delete(atlas_name, (0), axis=0)
    atlas_name = atlas_name.tolist()
    atlas_name = sorted(atlas_name, key=lambda x:x[0])
    atlas_name = np.array(atlas_name)

    return atlas_name
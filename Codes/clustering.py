"""
Created on Thu Mar 24 14:18:48 2022

@author: Fauston

"""

import numpy as np
from atlas_modif_name import get_corr_atlas_list, get_atlas_list
from plot_functions import histo_hori, boxplot_dti, cluster_plot
import pandas as pd
from DTI_kmeans_clustering import get_all_metric, get_kmeans
from ttest import get_results_ttest, get_excel_ttest_DTI, get_excel_ttest_MULTICOMP


perso_path = "D:/EPL/MASTER/TFE/alcoolique/Analyse/" # "/CECI/proj/pilab/PermeableAccess/alcoolique_TnB32xGDr7h/Analyse/Excel/"  

# =============================================================================
# FUNCTIONS
# =============================================================================
def get_cluster(ypred, patient_list, n_clusters):
    
    """
    Parameters
    ----------
    ypred : List of int
        List containing the label for each patient. It is either (if we have 3 clusters) 0, 1 or 2 depending on the cluster to which each patient is assigned. 
    patient_list : List of string
        List of the number of each patient in string.
    n_clusters : Int
        Number of clusters. 

    Returns
    -------
    clusters : List of list (size = n_clusters).
        List of list containing the numbers of the patients belonging to the cluster.
    """
    
    clusters = []
    for n in range(n_clusters):
        sublist = []
        for i, patient_nb in zip(ypred,patient_list):
            if (i==n) :
                sublist.append(patient_nb)
        clusters.append(sublist)
    return clusters
    

def cluster_to_df(clusters, file_path, type_matter):
    
    """
    Parameters
    ----------
    clusters : List of list 
        List containing the lists of the different clusters.
    file_path : String 
        File path of the concerned metric.
    type_matter : List of string representing the different matter of the brain 
        For DTI ["wm", "gm", "lobes", "subcorticals", "cerebellum"] and for the rest ["wm", "subcorticals", "cerebellum"].

    Returns
    -------
    all_clusters_df : Dataframe
        Table of a metric for the concerned atlases and the concerned patients (from a specific cluster).
    """
    
    atlas_list = get_corr_atlas_list(get_atlas_list(onlywhite = False))
    atlas_name = np.array(atlas_list)
    
    number_wm = atlas_name[atlas_name[:,3] == "1"]
    number_wm = np.append(number_wm, atlas_name[atlas_name[:,3] == "3"], axis = 0)
    number_wm = np.append(number_wm, atlas_name[atlas_name[:,3] == "6"], axis = 0)
    number_wm = number_wm[number_wm[:, 0].argsort()]
    
    number_gm = atlas_name[atlas_name[:,3] == "0"]
    number_lobes = atlas_name[atlas_name[:,3] == "5"]
    number_subcortical = atlas_name[atlas_name[:,3] == "2"]
    number_cerebellum = atlas_name[atlas_name[:,3] == "4"]
    
    all_clusters_df = []            
    atlas_list = get_corr_atlas_list(get_atlas_list(onlywhite=False))    
    atlas_name = np.array(atlas_list)[:,0]
    
    for cluster in clusters :
        
        if (type_matter == "wm"):
            percentage_change_all = np.zeros((number_wm.shape[0], len(cluster)))
        
        elif (type_matter == "gm"):
            percentage_change_all = np.zeros((number_gm.shape[0], len(cluster)))
        
        elif (type_matter == "lobes"):
            percentage_change_all = np.zeros((number_lobes.shape[0], len(cluster)))
        
        elif (type_matter == "subcortical"):
            percentage_change_all = np.zeros((number_subcortical.shape[0], len(cluster)))
            
        elif (type_matter == "cerebellum"):
            percentage_change_all = np.zeros((number_cerebellum.shape[0], len(cluster)))
        
        else: 
            percentage_change_all = np.zeros((len(atlas_list), len(cluster)))
        
        for patient_nb, i in zip(cluster, range(len(cluster))):
            worksheet = pd.read_excel(file_path, sheet_name=patient_nb)
            worksheet = worksheet.to_numpy()
            
            if (type_matter == "wm"):
                for k in range(worksheet.shape[0]):
                    for l,m in zip(number_wm[:,0],range(number_wm.shape[0])):
                        if (worksheet[k,0] == l):
                            percentage_change_all[m,i] = worksheet[k,3]
                            
            elif (type_matter == "gm"):
                for k in range(worksheet.shape[0]):
                    for l,m in zip(number_gm[:,0],range(number_gm.shape[0])):
                        if (worksheet[k,0] == l):
                            percentage_change_all[m,i] = worksheet[k,3]
                            
            elif (type_matter == "lobes"):
                for k in range(worksheet.shape[0]):
                    for l,m in zip(number_lobes[:,0],range(number_lobes.shape[0])):
                        if (worksheet[k,0] == l):
                            percentage_change_all[m,i] = worksheet[k,3]
                            
            elif (type_matter == "subcortical"):
                for k in range(worksheet.shape[0]):
                    for l,m in zip(number_subcortical[:,0],range(number_subcortical.shape[0])):
                        if (worksheet[k,0] == l):
                            percentage_change_all[m,i] = worksheet[k,3]
                            
            elif (type_matter == "cerebellum"):
                for k in range(worksheet.shape[0]):
                    for l,m in zip(number_cerebellum[:,0],range(number_cerebellum.shape[0])):
                        if (worksheet[k,0] == l):
                            percentage_change_all[m,i] = worksheet[k,3]
                            
            else: 
                percentage_change_all[:,i] = worksheet[:,3]
                    
        if (type_matter == "wm"):
            cluster_df = pd.DataFrame(percentage_change_all, index = number_wm[:,0], columns = cluster)
            
        elif (type_matter == "gm"):
            cluster_df = pd.DataFrame(percentage_change_all, index = number_gm[:,0], columns = cluster)
            
        elif (type_matter == "lobes"):
            cluster_df = pd.DataFrame(percentage_change_all, index = number_lobes[:,0], columns = cluster)
            
        elif (type_matter == "subcortical"):
            cluster_df = pd.DataFrame(percentage_change_all, index = number_subcortical[:,0], columns = cluster)
            
        elif (type_matter == "cerebellum"):
            cluster_df = pd.DataFrame(percentage_change_all, index = number_cerebellum[:,0], columns = cluster)
            
        else: 
            cluster_df = pd.DataFrame(percentage_change_all, index = atlas_name[:,0], columns = cluster)
        
        all_clusters_df.append(cluster_df)   
        
    return all_clusters_df


def cluster_behave_to_df(clusters, file_path):
    
    """
    Parameters
    ----------
    clusters : List of list 
        List containing the lists of the different clusters.
    file_path : String 
        File path of the concerned metric.

    Returns
    -------
    all_clusters_df : Dataframe
        Table of a behavioural data for the concerned atlases and the concerned patients (from a specific cluster).
    """
    
    all_clusters_df = []            
    
    for cluster in clusters :
        percentage_change_all = np.zeros((5, len(cluster)))
        
        for patient_nb, i in zip(cluster, range(len(cluster))):
            worksheet = pd.read_excel(file_path, sheet_name=patient_nb)
            worksheet = worksheet.to_numpy()
            
            percentage_change_all[:,i] = worksheet[:,1]
            
            cluster_df = pd.DataFrame(percentage_change_all, index = worksheet[:,0], columns = cluster)
        
        all_clusters_df.append(cluster_df)   
        
    return all_clusters_df


def get_means_atlas(df,seuil):
    
    """
    Parameters
    ----------
    df : Dataframe
        Tabular regarding a cluster and the areas contained in one type of matter.
    seuil : Int
        Threshold.

    Returns
    -------
    mean_atlas_corr : TYPE
        Percentage of change of atlas having it higher than seuil and smaller than -seuil.
    names_corr : TYPE
        Names of corresponding atlases.
    var_atlas_corr : TYPE
        Variance of atlas having it higher than seuil and smaller than -seuil.
    """
    
    mean_atlas = np.zeros(len(df.index))
    var_atlas = np.zeros(len(df.index))
    mean_atlas_corr = []
    var_atlas_corr = []
    names_corr = []
    
    for atlas_name,i in zip(df.index,range(len(df.index))) :
        mean_atlas[i] = np.mean(df.loc[atlas_name,:].to_numpy())
        var_atlas[i] = np.var(df.loc[atlas_name,:].to_numpy())
    
    for j in range(len(mean_atlas)):
        if(mean_atlas[j] >= seuil or mean_atlas[j] <= -seuil):
            mean_atlas_corr = np.append(mean_atlas_corr, mean_atlas[j])
            var_atlas_corr = np.append(var_atlas_corr, var_atlas[j])
            names_corr = np.append(names_corr, df.index[j])
            
    mean_atlas_corr = np.array(mean_atlas_corr)
    var_atlas_corr = np.array(var_atlas_corr)
    names_corr = np.array(names_corr)
    
    return mean_atlas_corr, names_corr, var_atlas_corr


def get_means_behave(df):
    
    """
    Parameters
    ----------
    df : Dataframe
        Tabular regarding a cluster and the areas contained in one type of matter.
    seuil : Int
        Threshold.

    Returns
    -------
    mean_atlas_corr : TYPE
        Percentage of change of atlas having it higher than seuil and smaller than -seuil.
    names_corr : TYPE
        Names of corresponding atlases.
    var_atlas_corr : TYPE
        Variance of atlas having it higher than seuil and smaller than -seuil.
    """
    
    mean_atlas = np.zeros(len(df.index))
    var_atlas = np.zeros(len(df.index))
    mean_atlas_corr = []
    var_atlas_corr = []
    names_corr = []
    
    for behave_name, i in zip(df.index, range(len(df.index))) :
        mean_atlas[i] = np.mean(df.loc[behave_name,:].to_numpy())
        var_atlas[i] = np.var(df.loc[behave_name,:].to_numpy())
    
    for j in range(len(mean_atlas)):
        mean_atlas_corr = np.append(mean_atlas_corr, mean_atlas[j])
        var_atlas_corr = np.append(var_atlas_corr, var_atlas[j])
        names_corr = np.append(names_corr, df.index[j])
    
    mean_atlas_corr = np.array(mean_atlas_corr)
    var_atlas_corr = np.array(var_atlas_corr)
    names_corr = np.array(names_corr)
    
    return mean_atlas_corr, names_corr, var_atlas_corr


def get_means_atlas_forbox(df, seuil):
    
    """
    Parameters
    ----------
    df : Dataframe
        Matrix of the corresponding Excel file.
    seuil : Int
        Threshold.

    Returns
    -------
    signi_df1 : Dataframe
        Atlas for which the mean of percentage change over the cluster is higher than seuil or smaller than -seuil.
    """
    
    all_signi = []
    name_all = []
    for atlas_name,i in zip(df.index,range(len(df.index))) :
        meann = np.mean(df.loc[atlas_name,:].to_numpy())
        if(meann>seuil or meann<-seuil):
            all_signi.append(df.loc[atlas_name,:].to_numpy())
            name_all.append(atlas_name)


    signi_df1 = pd.DataFrame(all_signi, index = name_all, columns = df.columns)            
    return signi_df1            


def get_results_mean_region_DTI(metric_name, type_matter, clusters, seuils, display, save):
    
    """
    Parameters
    ----------
    metric_name : List of strings
        Containing the metric names.
    type_matter : List of strings
        Containing the type of matter to be invesigated.
    clusters : List of string
        List representing the clusters.
    seuils : Int
        Threshold above which you wish to display the zones.

    Returns
    -------
    None. Plots
    """
    
    for matter,seuil in zip(type_matter, seuils):

        all_clusters_df1 = cluster_to_df(clusters, perso_path + "Mean_ROI_FA.xlsx", matter)
        all_clusters_df2 = cluster_to_df(clusters, perso_path + "Mean_ROI_MD.xlsx", matter)
        all_clusters_df3 = cluster_to_df(clusters, perso_path + "Mean_ROI_AD.xlsx", matter)
        all_clusters_df4 = cluster_to_df(clusters, perso_path + "Mean_ROI_RD.xlsx", matter)
        all_cluster_df = [all_clusters_df1, all_clusters_df2, all_clusters_df3, all_clusters_df4]
        
        color = "blue"
        
        for metric, name in zip(all_cluster_df, metric_name):
            for cluster, i in zip(metric, range(len(metric))): 
                #------------ HISTO 1 : MEANS -------------
                mean_atlas_corr, names_corr, var_atlas_corr = get_means_atlas(cluster,seuil)
                histo_hori(mean_atlas_corr, names_corr, color, "[DTI] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter,
                                                               "[DTI] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                #------------ HISTO 2 : BOXPLOT -------------
                signi_df = get_means_atlas_forbox(cluster, seuil)
                boxplot_dti(signi_df, "[DTI] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter,
                                      "[DTI] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                
                
def get_results_mean_region_NODDI(metric_name, type_matter, clusters, seuils, display, save):
    
    """
    Parameters
    ----------
    metric_name : List of strings
        Containing the metric names.
    type_matter : List of strings
        Containing the type of matter to be invesigated.
    clusters : List of string
        List representing the clusters.
    seuils : Int
        Threshold above which you wish to display the zones.

    Returns
    -------
    None. Plots
    """
    
    for matter,seuil in zip(type_matter,seuils):
        all_clusters_df1 = cluster_to_df(clusters, perso_path + "Mean_ROI_noddi_fintra.xlsx", matter)
        all_clusters_df2 = cluster_to_df(clusters, perso_path + "Mean_ROI_noddi_fextra.xlsx", matter)
        all_clusters_df3 = cluster_to_df(clusters, perso_path + "Mean_ROI_noddi_fiso.xlsx", matter)
        all_clusters_df4 = cluster_to_df(clusters, perso_path + "Mean_ROI_noddi_odi.xlsx", matter)
        all_cluster_df = [all_clusters_df1, all_clusters_df2, all_clusters_df3, all_clusters_df4]
        
        color = "blue"
        
        for metric, name in zip(all_cluster_df, metric_name):
            for cluster, i in zip(metric, range(len(metric))): 
                #------------ HISTO 1 : MEANS -------------
                mean_atlas_corr, names_corr, var_atlas_corr = get_means_atlas(cluster,seuil)
                histo_hori(mean_atlas_corr, names_corr, color, "[NODDI] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter,
                                                               "[NODDI] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                #------------ HISTO 2 : BOXPLOT -------------
                signi_df = get_means_atlas_forbox(cluster, seuil)
                boxplot_dti(signi_df, "[NODDI] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter,
                                      "[NODDI] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)

def get_results_mean_region_DIAMOND(metric_name, type_matter, clusters, seuils, display, save):
    
    """
    Parameters
    ----------
    metric_name : List of strings
        Containing the metric names.
    type_matter : List of strings
        Containing the type of matter to be invesigated.
    clusters : List of string
        List representing the clusters.
    seuils : Int
        Threshold above which you wish to display the zones.

    Returns
    -------
    None. Plots
    """
    
    for matter,seuil in zip(type_matter,seuils):
        all_clusters_df1 = cluster_to_df(clusters, perso_path + "Mean_ROI_wFA.xlsx", matter)
        all_clusters_df2 = cluster_to_df(clusters, perso_path + "Mean_ROI_wMD.xlsx", matter)
        all_clusters_df3 = cluster_to_df(clusters, perso_path + "Mean_ROI_wAD.xlsx", matter)
        all_clusters_df4 = cluster_to_df(clusters, perso_path + "Mean_ROI_wRD.xlsx", matter)
        all_cluster_df = [all_clusters_df1, all_clusters_df2, all_clusters_df3, all_clusters_df4]
        
        color = "blue"
        
        for metric, name in zip(all_cluster_df, metric_name):
            for cluster, i in zip(metric, range(len(metric))): 
                #------------ HISTO 1 : MEANS -------------
                mean_atlas_corr, names_corr, var_atlas_corr = get_means_atlas(cluster,seuil)
                histo_hori(mean_atlas_corr, names_corr, color, "[DIAMOND] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter,
                                                               "[DIAMOND] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                #------------ HISTO 2 : BOXPLOT -------------
                signi_df = get_means_atlas_forbox(cluster, seuil)
                boxplot_dti(signi_df, "[DIAMOND] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter,
                                      "[DIAMOND] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                
                
def get_results_mean_region_MF(metric_name, type_matter, clusters, seuils, display, save):
    
    """
    Parameters
    ----------
    metric_name : List of strings
        Containing the metric names.
    type_matter : List of strings
        Containing the type of matter to be invesigated.
    clusters : List of string
        List representing the clusters.
    seuils : Int
        Threshold above which you wish to display the zones.

    Returns
    -------
    None. Plots
    """
    
    for matter, seuil in zip(type_matter, seuils):
        all_clusters_df1 = cluster_to_df(clusters, perso_path + "Mean_ROI_mf_fvf_f0.xlsx", matter)
        all_clusters_df2 = cluster_to_df(clusters, perso_path + "Mean_ROI_mf_fvf_f1.xlsx", matter)
        all_clusters_df3 = cluster_to_df(clusters, perso_path + "Mean_ROI_mf_fvf_tot.xlsx", matter)
        all_cluster_df = [all_clusters_df1, all_clusters_df2, all_clusters_df3]
        
        color = "blue"
        
        for metric, name in zip(all_cluster_df, metric_name):
            for cluster, i in zip(metric, range(len(metric))): 
                #------------ HISTO 1 : MEANS -------------
                mean_atlas_corr, names_corr, var_atlas_corr = get_means_atlas(cluster,seuil)
                histo_hori(mean_atlas_corr, names_corr, color, "[MF] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter,
                                                               "[MF] - Histogram for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                #------------ HISTO 2 : BOXPLOT -------------
                signi_df = get_means_atlas_forbox(cluster, seuil)
                boxplot_dti(signi_df, "[MF] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter,
                                      "[MF] - Boxplot for cluster n°" + str(i) + " - " + name + "_" + matter, display, save)
                

def get_results_mean_region_behave(clusters, seuil, display, save):
    
    """
    Parameters
    ----------
    clusters : List of string
        List representing the clusters.
    seuils : Int
        Threshold above which you wish to display the zones.
    display : Boolean
        To show the plot.
    save : Boolean
        To save the plot.

    Returns
    ------- 
    None. Plots
    """
    
    all_cluster_df = cluster_behave_to_df(clusters, perso_path + 'Behavioural_data.xlsx')
    
    color = "blue"
    
    for cluster, i in zip(all_cluster_df, range(len(all_cluster_df))): 
        #------------ HISTO 1 : MEANS -------------
        mean_atlas_corr, names_corr, var_atlas_corr = get_means_atlas(cluster,seuil)
        histo_hori(mean_atlas_corr, names_corr, color, "[Behavioral data] - Histogram for cluster n°" + str(i),
                                                       "[Behavioral data] - Histogram for cluster n°" + str(i), display, save)
        #------------ HISTO 2 : BOXPLOT -------------
        signi_df = get_means_atlas_forbox(cluster, seuil)
        boxplot_dti(signi_df, "[Behavioral data] - Boxplot for cluster n°" + str(i),
                              "[Behavioral data] - Boxplot for cluster n°" + str(i), display, save)


# =============================================================================
# APPEL FCT
# =============================================================================
patient_numbers = ["02","04","05","08","09","11","12","13","14","15","17","18","19","20","21","22","24","26","27","28","30","31","32","33","34","35","36","37","39","40","41","42","43","45","46"]

all_metric_DTI = get_all_metric([perso_path + "Mean_ROI_FA.xlsx",
                                 perso_path + "Mean_ROI_MD.xlsx",
                                 perso_path + "Mean_ROI_AD.xlsx",
                                 perso_path + "Mean_ROI_RD.xlsx"], patient_numbers, False)

all_metric_NODDI = get_all_metric([perso_path + "Mean_ROI_noddi_fintra.xlsx",
                                   perso_path + "Mean_ROI_noddi_fextra.xlsx",
                                   perso_path + "Mean_ROI_noddi_fiso.xlsx",
                                   perso_path + "Mean_ROI_noddi_odi.xlsx"], patient_numbers, True)

all_metric_DIAMOND1 = get_all_metric([perso_path +"Mean_ROI_diamond_fractions_ftot.xlsx",
                                      perso_path +"Mean_ROI_diamond_fractions_csf.xlsx"], patient_numbers, True)

all_metric_DIAMOND2 = get_all_metric([perso_path +"Mean_ROI_wFA.xlsx",
                                      perso_path +"Mean_ROI_wMD.xlsx",
                                      perso_path +"Mean_ROI_wAD.xlsx",
                                      perso_path +"Mean_ROI_wRD.xlsx"], patient_numbers, True)
    
all_metric_MF = get_all_metric([perso_path + "Mean_ROI_mf_frac_csf.xlsx",
                                perso_path + "Mean_ROI_mf_frac_ftot.xlsx",
                                perso_path + "Mean_ROI_mf_fvf_tot.xlsx",
                                perso_path + "Mean_ROI_mf_wfvf.xlsx"], patient_numbers, True)

all_metric_DIAMOND = np.append(all_metric_DIAMOND2, all_metric_DIAMOND1, axis=0)
all_metric_DTI_NODDI = np.append(all_metric_DTI, all_metric_NODDI, axis=0)
all_metric_DTI_NODDI_DIAMOND = np.append(all_metric_DTI_NODDI, all_metric_DIAMOND2, axis=0)
all_metric_DTI_NODDI_DIAMOND_MF = np.append(all_metric_DTI_NODDI_DIAMOND, all_metric_MF, axis=0)

ncluster = 7

ypred_DTI_NODDI_DIAMOND_MF = get_kmeans(all_metric_DTI_NODDI_DIAMOND_MF, ncluster, ["FA", "MD", "AD"], False, True, False)
clusters_DTI_NODDI_DIAMOND_MF = get_cluster(ypred_DTI_NODDI_DIAMOND_MF, patient_numbers, ncluster)


# =============================================================================
# RESULTS OF CLUSTERING
# =============================================================================
cluster0 = ['05','26','35','36','37','40','41']
cluster1 = ['02', '04', '08', '09', '11', '12', '14', '15', '18', '20', '21', '22', '24', '27', '28', '30', '34', '39', '42', '45']
cluster2 = ['13', '17', '19', '31', '32', '33', '43', '46']        
clusters = [cluster0, cluster1, cluster2]


# =============================================================================
# METRIC NAMES
# =============================================================================
metric_name_DTI = ["FA", "MD", "AD", "RD"]
metric_name_NODDI = ["fintra","fextra", "fiso", "odi"]
metric_name_DIAMOND1 = ["wFA", "wMD", "wAD", "wRD"]
metric_name_DIAMOND2= ["frac_ftot","frac_csf"]
metric_name_DIAMOND = ["wFA", "wMD", "wAD", "wRD", "frac_ftot","frac_csf"]
metric_name_MF = ["frac_csf", "frac_ftot", "fvf_tot", "wfvf"]


# =============================================================================
# TYPES OF MATTERS
# =============================================================================
type_matter1 = ["wm", "gm", "lobes", "subcortical", "cerebellum"]
type_matter2 = ["wm", "subcortical", "cerebellum"]

# ypred_DTI = get_kmeans(all_metric_DTI, ncluster, ["FA", "MD", "AD"], False, True, False)
# clusters_DTI = get_cluster(ypred_DTI, patient_numbers, ncluster)
# get_results_mean_region_DTI(metric_name_DTI, type_matter1, clusters_DTI, [8,8,8,8], True, False)

# ypred_NODDI = get_kmeans(all_metric_NODDI, ncluster, ["fintra", "fextra", "fiso"], False, True, False)
# clusters_NODDI = get_cluster(ypred_NODDI, patient_numbers, ncluster)
# get_results_mean_region_NODDI(metric_name_NODDI, type_matter2, clusters_NODDI, [8,8,8,8], True, False)

# ypred_DIAMOND = get_kmeans(all_metric_DIAMOND, ncluster, ["wFA", "wMD", "wAD"], False, True, False)
# clusters_DIAMOND = get_cluster(ypred_DIAMOND, patient_numbers, ncluster)
# get_results_mean_region_DIAMOND(metric_name_DIAMOND, type_matter2, clusters_DIAMOND, [8,8,8,8], True, False)


# =============================================================================
# EXCEL RESULTING FROM T-TEST
# =============================================================================
T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease = get_results_ttest(metric_name_DTI, type_matter1, clusters, "DTI")    
get_excel_ttest_DTI(T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease)

T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease = get_results_ttest(metric_name_NODDI, type_matter2, clusters, "NODDI")    
get_excel_ttest_MULTICOMP("NODDI", T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease)

T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease = get_results_ttest(metric_name_DIAMOND1, type_matter2, clusters, "DIAMOND1")    
get_excel_ttest_MULTICOMP("DIAMOND1", T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease)

T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease = get_results_ttest(metric_name_DIAMOND2, type_matter2, clusters, "DIAMOND2")    
get_excel_ttest_MULTICOMP("DIAMOND2", T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease)

T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_gm_increase, T1_bis_gm_decrease, T2_bis_gm_increase, T2_bis_gm_decrease, T1_bis_lobes_increase, T1_bis_lobes_decrease, T2_bis_lobes_increase, T2_bis_lobes_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease = get_results_ttest(metric_name_MF, type_matter2, clusters, "MF")    
get_excel_ttest_MULTICOMP("MF", T1_bis_wm_increase, T1_bis_wm_decrease, T2_bis_wm_increase, T2_bis_wm_decrease, T1_bis_subcortical_increase, T1_bis_subcortical_decrease, T2_bis_subcortical_increase, T2_bis_subcortical_decrease, T1_bis_cerebellum_increase, T1_bis_cerebellum_decrease, T2_bis_cerebellum_increase, T2_bis_cerebellum_decrease)


# =============================================================================
# PLOTS
# =============================================================================
cluster0b = [2, 18, 25, 26, 27, 29, 30]
cluster1b = [0, 1, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 20, 24, 28, 31, 33]
cluster2b = [7, 10, 12, 21, 22, 23, 32, 34]        
clustersb = [cluster0b, cluster1b, cluster2b]

name_cluster = ["Cluster 1", "Cluster 2"]
colors = ["blue", "orange", "forestgreen"]

atlas_list = get_corr_atlas_list(get_atlas_list(onlywhite=True))    
atlas_name = np.array(atlas_list)[:,0]

metric1 = 34
cluster_plot(clustersb, name_cluster, colors, all_metric_DTI, 2*len(atlas_name)+metric1, "AD", metric1, "FA", 3*len(atlas_name)+metric1, "RD", 
             "Clustering according to the [" + atlas_name[metric1] + "] area", 
             "Clustering according to the [" + atlas_name[metric1] + "] area", True, False)




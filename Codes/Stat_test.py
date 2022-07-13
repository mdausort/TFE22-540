"""
Created on Thu Mar 24 14:18:48 2022

@author: Fauston
"""

import numpy as np
import pandas as pd
from scipy import stats


# =============================================================================
# T-TEST FUNCTION
# =============================================================================
def get_ttest(T1, T2, altern):
    
    """
    Parameters
    ----------
    T1 : Dataframe
        Matrix of means at T1.
    T2 : Dataframe
        Matrix of means at T2.
    altern : String
        Type of T-test.

    Returns
    -------
    ttest_results_df : Dataframe
        Results of the t-test containing stats and p-values.
    significant : Matrix of int
        Summarizing only the significant results so the ones with a p-value < 0.05.
    T1_bis : List 
        List of significant mean (based on p-value < 0.05) at T1 and their corresponding atlas.
    T2_bis : List 
        List of significant mean (based on p-value < 0.05) at T2 and their corresponding atlas.
    """
    
    atlas_name = T1.index
    T1 = T1.to_numpy()
    T2 = T2.to_numpy()
    T1_bis = []
    T2_bis = []
    ttest_results = np.zeros((T1.shape[0],2)) 
    for i in range(T1.shape[0]):
        tstat, pvalue = stats.ttest_rel(T1[i,:],T2[i,:],alternative = altern)
        
        if(pvalue<=0.05):
            T1_bis.append([atlas_name[i],T1[i,:]])
            T2_bis.append([atlas_name[i],T2[i,:]])
        
        
        ttest_results[i,0] = tstat
        ttest_results[i,1] = pvalue
        

    ttest_results_df = pd.DataFrame(ttest_results, columns = ["tstat", "pvalue"]) 
    significant = ttest_results[ttest_results[:,1] <= 0.05] 
    
    return ttest_results_df, significant, T1_bis, T2_bis


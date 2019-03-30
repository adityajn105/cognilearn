import pandas as pd
import numpy as np

def prepareDeciles(df,probability_col='probability',decile_columns='deciles',inplace=True):
    """
    Get deciles from probability values
    
    Arguments:
    df = A pandas dataframe with atleast one probability columns
    probability_col = name of probability column
    decile_columns = used only if inplace=True; name of decile columns
    inplace = append directly in df
    
    Returns:
    Deciles
    
    By:
    Cognizant-Aetna Team
    """
    _,bins = pd.qcut(df[probability_col],10,retbins=True,duplicates='drop')
    bins[0] -= 0.001
    bins[-1] += 0.001
    bins_labels = ['%d'%(9-x[0]) for x in enumerate(zip(bins[:-1],bins[1:]))]
    bins_labels[0] = bins_labels[0].replace('(','[')
    if inplace:
        df[decile_columns]=pd.cut(df[probability_col],bins=bins,labels=bins_labels)
    else:
        return pd.cut(df[probability_col],bins=bins,labels=bins_labels)
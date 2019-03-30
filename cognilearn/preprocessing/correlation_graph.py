import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlation_graph(X,var_list=[],size=(11,9)):
    """
    Generate a seaborn heat map to show correlation between variables
    
    Arguments:
    X - pandas.DataFrame with candidate features
    var_list -  list of features to calculate coorelation; if empty then show for all
    size - size of figure
        
    Returns: 
    A coorealtion Heatmap
    
    By:
    Cognizant-Aetna Team
    
    """
    if len(var_list)==0: var_list= list(X.columns)
    corr =X[var_list].corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=size)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
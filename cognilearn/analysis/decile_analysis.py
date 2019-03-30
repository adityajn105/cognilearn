import pandas as pd
import numpy as np

def get_deciles_analysis(df,score="prob",target="actual"):
    """
    *Deprecated use decile_analysis instead*
    Get decile analysis; see distibution of events(ones) and non-events(zeros) on different deciles
    
    Arguments:
    df = A pandas dataframe with atleast two columns one with calculated probabilities using model and another with  actual label
    score = name of probability column
    target = name of actual columns
    
    Returns:
    Decile analysis dataframe
    
    By:
    Cognizant-Aetna Team
    """
    df1 = df[[score,target]].dropna()
    _,bins = pd.qcut(df1[score],10,retbins=True,duplicates='drop')
    bins[0] -= 0.001
    bins[-1] += 0.001
    bins_labels = ['%d.(%0.2f,%0.2f]'%(9-x[0],x[1][0],x[1][1]) for x in enumerate(zip(bins[:-1],bins[1:]))]
    bins_labels[0] = bins_labels[0].replace('(','[')
    df1['Decile']=pd.cut(df1[score],bins=bins,labels=bins_labels)
    df1['Population']=1
    df1['Zeros']=1-df1[target]
    df1['Ones']=df1[target]
    summary=df1.groupby(['Decile'])[['Ones','Zeros','Population']].sum()
    summary=summary.sort_index(ascending=False)
    summary['TargetRate']=summary['Ones']/summary['Population']
    summary['CumulativeTargetRate']=summary['Ones'].cumsum()/summary['Population'].cumsum()
    summary['TargetsCaptured']=summary['Ones'].cumsum()/summary['Ones'].sum()
    return summary

def decile_analysis(estimator,X,Y):
    """
    Get decile analysis; see distibution of events(ones) and non-events(zeros) on different deciles
    
    Arguments:
    estimator = model with which probabilities will be calculated
    X = X variables for scoring
    Y = target labels
    
    Returns:
    Decile analysis dataframe
    
    By:
    Cognizant-Aetna Team
    """
    return get_deciles_analysis(pd.DataFrame({"prob":estimator.predict_proba(X)[:,1],"actual":Y}))

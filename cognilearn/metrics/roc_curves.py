import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def roc_curves(model,X_val,Y_val,X_train=None,Y_train=None,fname="Validation",sname="Training",shape=(10,3)):
    """
    Function generates 2 ROC curves on for train and one for validation
    
    Arguments: 
    X_train - training data
    Y_train - Training labels
    X_val - Validation data
    Y_val - Validation labels
    fname - name of first ROC
    sname - name of second ROC
    shape - can assign shape of figures
    
    Returns:
    one or two Roc curves
    
    By:
    Cognizant-Aetna Team
    """
    cols=2
    if type(X_train)==type(None): cols=1;shape=(5,3)
    figure,ax = plt.subplots(figsize=shape,nrows=1,ncols=cols)
    if type(X_train)==type(None): ax = [ax]
    from sklearn.metrics import roc_curve, roc_auc_score
    Y_score_val = model.predict_proba(X_val)
    fpr,tpr,thresh = roc_curve(Y_val,Y_score_val[:,1],pos_label=0)
    ax[0].plot(tpr,fpr)
    ax[0].plot([1,0],[1,0])
    ax[0].set_xlabel('True Positve Rate');ax[0].set_ylabel('False Positive Rate')
    ax[0].set_title('{} | AUC SCORE : {:.4f}'.format(fname,roc_auc_score(Y_val,Y_score_val[:,1])))
    if cols==2:
        Y_score_train = model.predict_proba(X_train)
        fpr,tpr,thresh = roc_curve(Y_train,Y_score_train[:,1],pos_label=0)
        ax[1].plot(tpr,fpr)
        ax[1].plot([1,0],[1,0])
        ax[1].set_xlabel('True Positve Rate');ax[1].set_ylabel('False Positive Rate')
        ax[1].set_title('{} | AUC SCORE : {:.4f}'.format(sname,roc_auc_score(Y_train,Y_score_train[:,1])))

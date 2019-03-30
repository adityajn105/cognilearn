import numpy as np
import matplotlib.pyplot as plt
from .sensitivity import sens
from .specificity import spec
from .accuracy import accuracy

def specificity_vs_sensitivity(estimator,X_val,Y_val,X_train=None,Y_train=None,
                             fname="Validation",sname="Training",
                             tp=100,thrange=(0,1),shape=(15,5)):
    """
    Plot Spensitivity, Specificity and Accuracy of a model(binary classfier) at tp number of threshold between 0 to 100
    
    Arguments:
    estimator - model object
    X_val - X variables for plot 1
    Y_val - target variable for plot 1
    X_train - X variables for plot 2 ( if None then no plot 2)
    Y_train - target variable for plot 2
    fname - name of first plot
    sname - name of second plot
    tp - number of points between 0 to 1 to calculate values
    thrange - range between tp points are divided and metrices are calcualted
    shape - shape of plot (if there are 2 plots, space will be shared by two plots)
    
    Returns:
    1 or 2 sensitivity, specificity, accuracy plots
    
    By: 
    Cognizant-Aetna Team
    """
    thress =np.linspace(thrange[0],thrange[1],tp)
    vsensi = np.array([ sens(estimator,X_val,Y_val,thres) for thres in thress])
    vspeci = np.array([ spec(estimator,X_val,Y_val,thres) for thres in thress])
    vacc = np.array([accuracy(estimator,X_val,Y_val,thres) for thres in thress])
    cols=2
    if type(X_train)==type(None): cols=1;shape={8,5}
    fig,ax = plt.subplots(figsize=shape,nrows=1,ncols=cols)
    if type(X_train)==type(None): ax = [ax]
    ax[0].plot(thress,vsensi,c='b');ax[0].plot(thress,vspeci,c='g');ax[0].plot(thress,vacc,c='k')
    ind = abs(vspeci-vsensi) == abs(vspeci-vsensi).min()
    ax[0].annotate(
        "Thresh : {:.4f}\nSpecificity : {:.4f}\nSensitivity : {:.4f}\nAccuracy: {:.4f}".format(
            thress[ind][0],vspeci[ind][0],vsensi[ind][0],vacc[ind][0]),
        (thress[ind][0]+.01,vspeci[ind][0]),
        xytext=(.5,.5),arrowprops=dict(facecolor='gray',width=.1,headwidth=5,headlength=7)
    )
    ax[0].set_xlabel('Threshold');ax[0].set_ylabel('Score');ax[0].set_title(fname)
    if type(X_train)!=type(None):
        tsensi = np.array([ sens(estimator,X_train,Y_train,thres) for thres in thress])
        tspeci = np.array([ spec(estimator,X_train,Y_train,thres) for thres in thress])
        tacc = np.array([accuracy(estimator,X_train,Y_train,thres) for thres in thress])
        ax[1].plot(thress,tsensi,c='b');ax[1].plot(thress,tspeci,c='g');ax[1].plot(thress,tacc,c='k')
        ind = abs(tspeci-tsensi) == abs(tspeci-tsensi).min()
        ax[1].annotate(
            "Thresh : {:.4f}\nSpecificity : {:.4f}\nSensitivity : {:.4f}\nAccuracy: {:.4f}".format(
                thress[ind][0],tspeci[ind][0],tsensi[ind][0],tacc[ind][0]),
            (thress[ind][0]+.01,tspeci[ind][0]),
            xytext=(.5,.5),arrowprops=dict(facecolor='gray',width=.1,headwidth=5,headlength=7)
        )
        ax[1].set_xlabel('Threshold');ax[1].set_ylabel('Score');ax[1].set_title(sname)


from sklearn.metrics import confusion_matrix

def confusion_matrix_modified(estimator,X,Y,thres=0.5):
    """
    Calculate confusion matrix of a model(binary classfier) at specific threshold
    
    Arguments:
    estimator - model object
    X - variables (DataFrame, numpy array)
    Y - target variables
    thres - threshold at which you need to calculate
    
    Returns:
    confusion matrix at particular threshold
    
    By:
    Cognizant-Aetna Team
    """
    return confusion_matrix(Y,1*(estimator.predict_proba(X)[:,1] > thres))
        
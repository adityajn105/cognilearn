from sklearn.metrics import accuracy_score
def accuracy(estimator,X,Y,thres=0.5):
    """
    Calculate Accuracy of a model(binary classfier) at particular threshold
    Arguments:
    estimator - model object
    X - variables ( dataframe, numpy array)
    Y - target variables
    thresh - threshold
    
    Returns:
    Accuracy at particular threshold
    
    By - Cognizant-Aetna Team
    """
    return accuracy_score(Y,1*(estimator.predict_proba(X)[:,1] > thres))
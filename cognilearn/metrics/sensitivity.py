from sklearn.metrics import confusion_matrix

def sens(estimator,X,Y,thres=0.5):
    """
    Calculate sensitivity of a model(binary classfier) at specific threshold
    
    Arguments:
    estimator - model object
    X - variables (DataFrame, numpy array)
    Y - target variables
    thres - threshold at which you need to calculate
    
    Returns:
    Sensitivity at particular threshold
    
    By:
    Cognizant-Aetna Team
    """
    cnf = confusion_matrix(Y,1*(estimator.predict_proba(X)[:,1] > thres))
    return cnf[1,1]/sum(cnf[1,:])

sensitivity = sens
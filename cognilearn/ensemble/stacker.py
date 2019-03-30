import numpy as np

class Stacker():
    def __init__(self,models,weights=None):
        """
        A stacker is a ensemble method using pretrained models and giving different importance to each of them

        Arguments:
        model : list of models
        weights : list of weights to be given to different model

        Returns:
        A Stacked Model

        By:
        Cognizant-Aetna Team
        """
        self._total = len(models)
        if weights==None:
            self.weights = [1/self._total]*self._total
        else:
            self.weights = weights
        self.models = models
    
    def predict_proba(self,X):
        """
        Predict weighted propensity score usign all models

        Arguments:
        X : X variables

        Returns:
        propensity score

        By:
        Cognizant-Aetna Team
        """
        proba = self.weights[0]*self.models[0].predict_proba(X)
        for i in range(1,self._total):
            proba += self.weights[i]*self.models[i].predict_proba(X)
        return proba/sum(self.weights)
    
    def predict(self,X,threshold=0.5):
        """
        Predict labels using weighted models at specifict threshold

        Argument:
        X :  X variables

        Returns:
        y_pred

        By:
        Cognizant-Aetna Team
        """
        return 1*(self.predict_proba(X)[:,1]>threshold)
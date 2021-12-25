import random
import numpy as np

class CustomModel(object):
    """
    Custom model, we can load parameters in __init__ method
    """

    def __init__(self):
        """
        kind of constructor in python
        """
        print("Custom Model Initializing")

    def predict(self, X, feature_names):
        """
        This is the method routes the endpoint here like http://127.0.0.1:port/predict
        :param X: feature's values
        :param feature_names: names of columns
        :return: prediction
        """

        print("Prediction Endpoint Called")

        return np.array(random.random()) #(must be list or np array


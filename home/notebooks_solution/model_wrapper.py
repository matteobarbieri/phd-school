import numpy as np

class TrainedModelWrapper:

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Assumes X has shape (n, p), where n is the number of samples and p the number of features
        """
        raise Exception("NotImplemented")
    
    def predictOne(self, x: np.ndarray) -> float | int:
        """
        Assumes the input is a one-dimensional array (a vector).
        Its shape should be something like (p,)
        """
        return self.predict(x[np.newaxis, :])[0]

class TrainedSklearnModelWrapper(TrainedModelWrapper):

    def __init__(self, model):
        """
        This is the class' **constructor**. It is called every time you _instantiate_ a new
        object of this class, that is when you write something like
        my_instance = TrainedSklearnModelWrapper(...).

        This specific constructor accepts exactly **one** parameter, which is "saved" in
        a variable so that it is available from within that instance through using `self`.
        These are called _properties_.

        tl;dr: from now on, you can access the model from within other function of this class
        using `self.model`
        """
        self.model = model

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Assumes X has shape (n, p), where n is the number of samples and p the number of features
        """

        ### TODO ###
        # Hint: you will likely want to use the `.predict()` function of the model you saved
        # Hint: you can access previously stored properties using `self.`
        return self.model.predict(X)
        ### END ###

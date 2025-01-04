import numpy as np

def smart_classify(
        resized: np.ndarray, wrapped_model, threshold=75) -> str:
    """
    Classifies a digit in a given 28x28 numpy array using a neural network model.
        The function first checks if the cell is empty by counting the number of non-zero pixels.
        If the cell is not empty, it uses a neural network model to classify the digit.
        Args:
            resized (np.ndarray): A 28x28 numpy array representing the image of the digit.
            wrapped_model: The neural network model used for classification.
            threshold (int, optional): The minimum number of non-zero pixels required to consider the cell non-empty. Defaults to 75.
        Returns:
            str: The classified digit as a string, or a space character if the cell is empty or the confidence is below the threshold.
    """

    # Identify blank cells
    if (resized != resized.min()).sum() < threshold:
        return " "

    digit = wrapped_model.predictOne(resized)

    if digit != 0:
        return str(digit)
    else:
        return " "

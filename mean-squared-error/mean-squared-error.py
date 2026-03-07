import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred,y_true = np.array(y_pred),np.array(y_true)
    n=len(y_pred)
    return np.sum(np.square(y_pred-y_true))/n

import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    axis = -1 
    z = x - np.max(x, axis=axis, keepdims=True)

    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=axis, keepdims=True)
    
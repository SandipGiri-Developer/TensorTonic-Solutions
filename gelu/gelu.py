import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x=np.array(x) 
    v_erf = np.vectorize(math.erf)
    gel = 1+v_erf(x/math.sqrt(2))
    
    return x/2*gel
   

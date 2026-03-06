import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    ans = []
    for i in x:
        if i<=0:
            ans.append(np.dot(alpha,np.exp(i)-1))
        else:
            ans.append(i)
    return ans        
import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    x = np.array(x,dtype=float)
    elu = []
    for i in x:
        if i>0:
            elu.append(i)
        else:
            elu.append(np.dot(alpha,(np.exp(i)-1)))

    return np.dot(lam,elu)


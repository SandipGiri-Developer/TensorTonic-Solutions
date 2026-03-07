def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    m,n=len(X),len(X[0])
    ans=[]
    ma = float('-inf')
    for i in range(0,m,pool_size):
        t = []
        for z in range(0,n,pool_size):
            for j in range(i,i+pool_size):
                for k in range(z,z+pool_size):
                    if X[j][k]>ma:
                        ma=X[j][k]
            t.append(ma)
            ma = float('-inf')
        ans.append(t)   
    return ans   
            
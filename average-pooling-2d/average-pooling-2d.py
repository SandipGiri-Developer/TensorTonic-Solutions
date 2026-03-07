def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    m,n=len(X),len(X[0])
    ans=[]
    ma = 0
    for i in range(0,m,pool_size):
        t = []
        for z in range(0,n,pool_size):
            for j in range(i,i+pool_size):
                for k in range(z,z+pool_size):
                    
                    ma+=X[j][k]
            
            t.append(ma/(pool_size**2))
            ma = 0
        ans.append(t)   
    return ans   
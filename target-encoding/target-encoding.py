def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    m = {}
    for i in range(0,len(categories)):
        m.setdefault(categories[i],[]).append(targets[i])

    mean = {}
    for x in m:
        mean.setdefault(x,sum(m[x])/len(m[x]))
    ans = []
    for i in range(len(targets)):
        ans.append(mean[categories[i]])
    return ans    
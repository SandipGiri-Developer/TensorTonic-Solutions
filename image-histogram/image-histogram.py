def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    grid = [0]*256
    for x in image:
        for i in x:
            grid[i]+=1
    return grid        
    
import numpy as np
import cv2 
def convolve(image):
    rows, columns = image.shape

    #Kernels:
    
    """
    Gx = np.matrix([
        [1,2,1],
        [2,4,2],
        [1,2,1]
    ], dtype=np.float32) / 16
    """
    
    """
    Gx = np.array([
    [1,  4,  6,  4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1,  4,  6,  4, 1]
    ], dtype=np.float32) / 256
    """

    Gx = np.matrix([
    [0,    0,    1,    2,    1,    0,    0],
    [0,    3,   13,   22,   13,    3,    0],
    [1,   13,   59,   97,   59,   13,    1],
    [2,   22,   97,  159,   97,   22,    2],
    [1,   13,   59,   97,   59,   13,    1],
    [0,    3,   13,   22,   13,    3,    0],
    [0,    0,    1,    2,    1,    0,    0]
    ], dtype=np.float32) / 1003
    filteredimage = np.zeros((rows, columns), dtype = np.uint8)

    
    print("Filtering image")    
    for i in range(rows):
        for j in range(columns):
            weight = 0
            startX = j - 2 #a difference of 1
            startY = i - 2 #a difference of 1

            #Gx
            for k in range(7): #rows kernel
                for m in range(7): #columns kernel
                    if(not(startY+k < 0 or startY+k >= rows or startX+m < 0 or startX+m >= columns)): #bounding
                        weight += image[startY+k, startX+m] * Gx[k,m]

            filteredimage[i,j] = weight
    

    """
    print("first version", filteredimage)
    totalsum = np.sum(filteredimage)
    for i in range(rows):
        for j in range(columns):
            filteredimage[i,j] = filteredimage[i,j]/totalsum

    """

    #print("FIltered image", filteredimage)
    filteredimage = np.clip(filteredimage, 0, 255).astype(np.uint8)        

    return filteredimage

    import cv2
import numpy as np

def gaussian_filter(image, ksize=5, sigma=1.0):
    """
    Applies a Gaussian filter to an image.

    Parameters:
        image (numpy.ndarray): Input image (grayscale or color).
        ksize (int): Kernel size (must be odd: 3,5,7,...).
        sigma (float): Standard deviation of the Gaussian.

    Returns:
        numpy.ndarray: Blurred image.
    """
    # Ensure kernel size is odd
    if ksize % 2 == 0:
        raise ValueError("Kernel size must be odd")

    filtered = cv2.GaussianBlur(image, (ksize, ksize), sigma)
    return filtered

import numpy as np


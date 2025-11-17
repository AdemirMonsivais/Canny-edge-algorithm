import cv2 as cv
import numpy as np
import math

#using sobel operators
#the image is in grayscale
def get_magnitudes(image):
    row, column = image.shape
    print(f"row: {row} column: {column}")

    #Kernels:
    Gx = np.matrix([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ])

    Gy = np.matrix([
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]
    ])   


    outputX = np.zeros((row,column), dtype = np.float64) #initialize matrix output
    outputY = np.zeros((row, column), dtype = np.float64)


    print("Covolving kernel with the image...")    
    for i in range(row):
        for j in range(column):
            weight = 0
            startX = j - 1 #a difference of 1
            startY = i - 1 #a difference of 1

            #Gx
            for k in range(3): #rows kernel
                for m in range(3): #columns kernel
                    if(not(startY+k < 0 or startY+k >= row or startX+m < 0 or startX+m >= column)): #bounding
                        weight += image[startY+k, startX+m] * Gx[k,m]

            #print("///////////////////////////")
            outputX[i,j] = weight

            weight = 0

            #Gy
            for m in range(3): #columns kernel
                for k in range(3): #rows kernel
                    if(not(startY+k < 0 or startY+k >= row or startX+m < 0 or startX+m >= column)): #bounding
                        weight += image[startY+k, startX+m] * Gy[k,m]

            outputY[i,j] = weight

            weight = 0

    #magnitudes = np.zeros((row,column), dtype = np.float64)
    
    """
    #Compute magnitude and threshold:
    print("Computing magnitude and threshold...")
    threshold = 0
    for i in range(row):
        for j in range(column):
            magnitudes[i,j] = (outputX[i,j]**2 + outputY[i,j]**2)**0.5
            threshold += magnitudes[i,j]

    
    threshold = int(threshold/(row*column))

    magnitudes = magnitudes.astype(np.int64)

    print("setting image... ")

    #threshold = 100
    for i in range(row):
        for j in range(column):
            if magnitudes[i,j] > threshold:
                #print(f"{magnitudes[i,j]}   {threshold}")
                magnitudes[i,j] = 0 #255
            else: 
                magnitudes[i,j] = 255 #0

    """
    return outputX, outputY
        
def get_gradient_features(image):
    rows, columns = image.shape

    magnitude_x, magnitude_y = get_magnitudes(image) #getting magnitudes

    gradient_magnitude = np.zeros((rows, columns), dtype = np.float64)          #initialize matrix called gradient_magnitude
    gradient_orientation = np.zeros((rows, columns), dtype = np.float64)        #initialize matrix called gradient_orientation

    #Compute gradient magnitude and gradient orientation

    for i in range(rows):
        for j in range(columns):
            gradient_magnitude[i,j] = (magnitude_x[i,j]**2 + magnitude_y[i,j]**2)**0.5 ##gRADIENT MAGNITUDE
            gradient_orientation[i,j] = math.atan2(magnitude_y[i,j], magnitude_x[i,j]) 
                 ##GRADIENT ORIENTATION

    gradient_magnitude = gradient_magnitude.astype(dtype = np.int64)        #**parse matrix from float to integers ¿¿unsinged??
    gradient_orientation = gradient_orientation.astype(dtype = np.int64)        #**parse matrix from float to integers ¿¿unsinged??
    
    return gradient_magnitude, gradient_orientation

def get_threshold(gradient_magnitude):
    rows, columns = gradient_magnitude.shape

    threshold = 0
    for i in range(rows):
        for j in range(columns):
            threshold += gradient_magnitude[i,j]

    return int(threshold/(rows*columns))


def detect_edges(gradient_magnitude, threshold):
    rows, columns = gradient_magnitude.shape

    for i in range(rows):
        for j in range(columns):
            if gradient_magnitude[i,j] > threshold:
                #print(f"{magnitudes[i,j]}   {threshold}")
                gradient_magnitude[i,j] = gradient_magnitude[i,j] #255
            else: 
                gradient_magnitude[i,j] = 0 #0

    return gradient_magnitude


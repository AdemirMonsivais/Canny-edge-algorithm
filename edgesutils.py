from utils import displayImage
import numpy as np
import cv2

def thin_edges(gradient_magnitude, gradient_orientation, threshold):#only works for degrees format
    rows, columns = gradient_magnitude.shape


    
    for i in range(rows):
        for j in range(columns):
            degree = gradient_orientation[i,j]

            if gradient_magnitude[i,j] < threshold:
                gradient_magnitude[i,j] = 0
            else: 

                if degree >= 0 and degree < 30: #right direction
                    deltax = 1
                    deltay = 0
                elif degree >= 30 and degree < 60:
                    deltax = 1
                    deltay = -1
                elif degree >= 60 and degree < 120:
                    deltax = 0
                    deltay = 1
                elif degree >= 120 and degree < 150:
                    deltax = -1
                    deltay = -1
                elif degree >= 150 and degree < 180:
                    deltax = -1
                    deltay = 0
                elif degree < 0 and degree <= 30:
                    deltax = 1
                    deltay = 0
                elif degree < 30 and degree <= 60:
                    deltax = 1
                    deltay = 1
                elif degree < 60 and degree <= 120:
                    deltax = 0
                    deltay = -1
                elif degree < 120 and degree <= 150:
                    deltax = -1
                    deltay = 1
                elif degree < 150 and degree <= 180:
                    deltax = -1
                    deltay = 0

                if i+deltay >= 0 and i+deltay < rows and j+deltax >=0 and j+deltax<columns:
                    a = gradient_magnitude[i+deltay,j+deltax]
                else: a = -10000
                
                if i-deltay >= 0 and i-deltay < rows and j-deltax >=0 and j-deltax<columns:
                    b = gradient_magnitude[i-deltay,j-deltax] #the opposite direction (flip signs)
                else: b = -10000

                current = gradient_magnitude[i,j]

                if a < current and b < current:
                    gradient_magnitude[i,j] = current
                else: 
                    if i+deltay >= 0 and i+deltay < rows and j+deltax >=0 and j+deltax<columns:
                        gradient_magnitude[i+deltay,j+deltax] = 0
                    if i-deltay >= 0 and i-deltay < rows and j-deltax >=0 and j-deltax<columns:
                        gradient_magnitude[i-deltay,j-deltax] = 0

    return gradient_magnitude

def get_thresholds(gradient_magnitude, percentile=80, ratio=0.4):
    magnitudes_array = np.sort(gradient_magnitude.flatten())
    high_threshold = np.percentile(magnitudes_array, percentile)
    low_threshold = high_threshold * ratio
    return high_threshold, low_threshold



def sharp_edges(gradient_magnitude):
    rows, columns = gradient_magnitude.shape

    print(f"sharpedges: geradient magnitudes: {gradient_magnitude}")

    #dummy variables for the moment
    high_threshold, low_threshold = get_thresholds2(gradient_magnitude)


    #high_threshold = 255
    #low_threshold = high_threshold*(1/3)

    image = np.zeros((rows, columns), dtype = np.uint8) #intialized final image.

    for i in range(rows):
        for j in range(columns):
            magnitude = gradient_magnitude[i,j]

            if magnitude != 0:
                #Double Threshold:
                if magnitude >= high_threshold:
                    magnitude = 255
                elif magnitude >= low_threshold and magnitude < high_threshold:
                    if is_strong_edge(gradient_magnitude, high_threshold, i, j):
                        magnitude = 255
                    else: magnitude = 0
                else: magnitude = 0

            image[i,j] = magnitude

    return image

def is_strong_edge(gradient_magnitude, high_threshold, i, j):
    rows, columns = gradient_magnitude.shape

    startX = j - 1 #a difference of 1
    startY = i - 1 #a difference of 1

    k = 0
    m = 0
    strong_edge = False

    while k < 3 and strong_edge == False:
        while m < 3 and strong_edge == False:
            if not(startY+k < 0 or startY+k >= rows or startX+m < 0 or startX+m >= columns): #bounding
                if gradient_magnitude[startY+k, startX+m] >= high_threshold:
                    strong_edge = True

            m += 1
        k += 1

    return strong_edge


'''
def tracking_edges(image):
    rows, columns = image.shape

    for i in range(rows):
        for j in range(columns):
            startX = j - 1 #a difference of 1
            startY = i - 1 #a difference of 1

            k = 0
            m = 0
            weak_edge = False
            while k < 3 and image[i,j] != 255:
                while m < 3 and image[i,j] != 255:
                    if(not(startY+k < 0 or startY+k >= rows or startX+m < 0 or startX+m >= columns)): #bounding
                        if image[startY+k, startX+m] == 255:
                           image[i,j] == 255
                           weak_edge = True
                    m += 1

                if(weak_edge):
                    image[i,j] = 0

                k += 1
    
    return image
'''
    


def get_thresholds2(gradient_magnitude, low_ratio=0.05, high_ratio=0.15):
    nonzero = gradient_magnitude[gradient_magnitude > 0]
    if nonzero.size == 0:
        return 0, 0

    high_threshold = np.percentile(nonzero, 100 * (1 - high_ratio))
    low_threshold = high_threshold * low_ratio / high_ratio
    
    return high_threshold, low_threshold
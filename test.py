import numpy as np
import cv2 as cv

import utils
import gaussianfilter
import sobeloperator
import math
import edgesutils
import filter


img = cv.imread("src/images/input/antilope.jpg")

img = utils.resize(img)

#edges = cv.Canny(img, low_threshold = 80, high_threshold = 160)
#utils.displayImage(edges)

kernel = np.array([0.25,0.5,0.25])

grayimage = utils.grayscale(img)

filteredimage = filter.gaussian_filter(grayimage,ksize = 5, sigma = 1)
#fimg = filter.convolve(fimg)
#utils.displayImage(fimg, "filtered image using gaussian blur")
#filteredimage = gaussianfilter.convolve(grayimage, kernel)
#filteredimage = gaussianfilter.convolve(filteredimage, kernel)

#utils.displayImage(img)

utils.displayImage(filteredimage, "filtered")

#sobel operations

#matrix = np.zeros([5,5])
#utils.displayImage(matrix)

#img = utils.grayscale(img)
#utils.displayImage(img)

gradient_magnitude, gradient_orientation = sobeloperator.get_gradient_features(filteredimage)

threshold = sobeloperator.get_threshold(gradient_magnitude)

newimage = sobeloperator.detect_edges(gradient_magnitude, threshold)


gradient_orientation = np.degrees(gradient_orientation)

gradient_orientation = gradient_orientation.astype(dtype = np.int64)
print(gradient_orientation)


#preimage = sobeloperator.detect_edges(gradient_magnitude, threshold)
#preimage = preimage.astype(dtype = np.uint8)
#utils.displayImage(preimage, "image using sobel kernels")

newimage = edgesutils.thin_edges(gradient_magnitude, gradient_orientation, threshold)
newimage = newimage.astype(np.uint8)

#utils.displayImage(newimage)

print(f"in main gradient magnitude: {newimage}")
finalimage = edgesutils.sharp_edges(newimage)

#finalimage = edgesutils.contrast(finalimage)

#print(f"after contrasting: {finalimage}")

utils.displayImage(finalimage, "After sharping", False, "antilope.jpg")

print(f"after sharping: {finalimage}")

#finalimage = edgesutils.tracking_edges(finalimage)

#utils.displayImage(finalimage, "final image,", True, "finalimage.png")
#utils.displayImage(newimage, "image after thin the edges")


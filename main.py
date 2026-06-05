import numpy as np
import cv2 as cv

import canny_tools.utils as utils
import canny_tools.sobeloperator as sobeloperator
import canny_tools.edgesutils as edgesutils
import canny_tools.filter as filter

PATH = "/home/ade/proyectos/archivo_proyectos/canny/src/images/input/panda-rojo.png"

img = cv.imread(PATH)
img = utils.resize(img)

utils.displayImage(img)

grayimage = utils.grayscale(img)
filteredimage = filter.gaussian_filter(grayimage,ksize = 7, sigma = 2)

utils.displayImage(filteredimage, "Imagen filtrada usango un filtro Gaussiano", True, "imagenfiltradas.jpeg")

gradient_magnitude, gradient_orientation = sobeloperator.get_gradient_features(filteredimage)

threshold = sobeloperator.get_threshold(gradient_magnitude)
newimage = sobeloperator.detect_edges(gradient_magnitude, threshold)

boldimage = sobeloperator.print_edges(gradient_magnitude, threshold)
boldimage = boldimage.astype(np.uint8)
#utils.displayImage(boldimage)

gradient_orientation = np.degrees(gradient_orientation)

gradient_orientation = gradient_orientation.astype(dtype = np.int64)


newimage = edgesutils.thin_edges(gradient_magnitude, gradient_orientation, threshold)
newimage = newimage.astype(np.uint8)
#utils.displayImage(newimage, "Imagen después de haber aplicado Supresión No Máxima")
newimage = sobeloperator.print_edges(gradient_magnitude, threshold)

finalimage = edgesutils.sharp_edges(newimage)
utils.displayImage(finalimage, "Imagen Final")


#utils.displayImage(newimage, "Imagen después de aplicar el detector de bordes Sobel")





import cv2 as cv
import numpy as np

def resize(image):
    # max size
    max_size = 720  

    h, w = image.shape[:2]

    scale = max_size / max(h, w)

    new_w = int(w * scale)
    new_h = int(h * scale)
    resized = cv.resize(image, (new_w, new_h), interpolation=cv.INTER_AREA)
    return resized


def grayscale(img):
    b = img[:, :, 0] * 0.114
    g = img[:, :, 1] * 0.587
    r = img[:, :, 2] * 0.299

    gray = b + g + r

    return gray.astype(np.uint8)

def displayImage(image, winname = "image output", saveimage = False, nameoutput = ""):
    cv.imshow(winname, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    if saveimage and not nameoutput == "":
        cv.imwrite("src/images/output" + nameoutput, image)

def contrast(image):
    rows, columns = image.shape

    for i in range(rows):
        for j in range(columns):
            if(image[i,j] == 255):
                image[i,j] = 0
            else: image[i,j] = 255
    return image
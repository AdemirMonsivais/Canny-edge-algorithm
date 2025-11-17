import numpy as np

def convolve(img, kernel):
    #Get properties 
    row, column = img.shape

    diff = int(len(kernel)/2)

    output = np.zeros((row,column)) #initialize

    #convolve horizontally
    for i in range(row):
        for j in range(column):
            weight = 0
            start = j - diff #I set an auxiliar variable to make possible the additions and multiplications for each pixels (fit pixel's index)
            for k in range(len(kernel)):
                if not(start+k < 0 or start+k >= column):
                    weight += img[i,start+k]*kernel[k]
            output[i,j] = weight

    #convolve vertically
    for j in range(column):
        for i in range(row):
            weight = 0
            start = i - diff
            for k in range(len(kernel)):
                if not(start+k < 0 or start+k >= row):
                    weight += output[start+k,j]*kernel[k]
            output[i,j] = weight

    output = output.astype(np.uint8)

    return output


def filtrar(img, kernel):
    #Get properties 
    filas, columnas = img.shape

    #Para determinar donde empiezan las operaciones
    diff = int(len(kernel)/2) 

    output = np.zeros((filas,columnas)) #inicializar

    #convolucionar horizontalmente
    for i in range(filas):
        for j in range(columnas):
            weight = 0
            inicio_x = j - diff #Calcule el inicio gracias a la differencia
            for k in range(len(kernel)):
                if not(inicio_x+k < 0 or inicio_x+k >= columnas): 
                    weight += img[i,inicio_x+k]*kernel[k]
            output[i,j] = weight

    #convolucionar verticalmente
    for j in range(columnas):
        for i in range(filas):
            weight = 0
            inicio_x = i - diff #Calcule el inicio gracias a la differencia
            for k in range(len(kernel)):
                if not(inicio_x+k < 0 or inicio_x+k >= filas):
                    weight += output[inicio_x+k,j]*kernel[k]
            output[i,j] = weight

    output = output.astype(np.uint8) 

    return output #imagen filtrada
    
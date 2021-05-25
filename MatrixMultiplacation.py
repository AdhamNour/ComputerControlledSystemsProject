import math

def matrixMultiplication(x, y):
    x1new = x[0][0]*y[0]+x[0][1]*y[1]
    x2new = x[1][0]*y[0]+x[1][1]*y[1]
    return [x1new, x2new]
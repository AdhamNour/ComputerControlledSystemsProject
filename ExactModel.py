import math;
from matrixaddition import matrixAddition
from MatrixMultiplacation import matrixMultiplication
def getExactModel(Tsim,Tsampling):
    w= math.exp(-2.1*Tsampling)*math.cos(math.sqrt(4.59)*Tsampling)
    a = (1/(math.sqrt(4.59)))*math.exp(-2.1*Tsampling)*math.sin(math.sqrt(4.59)*Tsampling)
    
    phi = [[w+2.1*a,a],[-9*a,w-2.1*a]]
    theta=[((4/9)+(4/9)*w+(0.6/9)*a),(w+1.9*a-1)]
    
        
    x=[[0],[0]]
    n=int(Tsim/Tsampling)
    timeAxis=[0]
    for i in range(n):
        x1k=x[0][i]
        x2k=x[1][i]
        (x1k1,x2k1) = matrixAddition(theta,matrixMultiplication(phi,[x1k,x2k]))
        x[0].append(x1k1)
        x[1].append(x2k1)
        timeAxis.append((i+1)*Tsampling)
    return (timeAxis,x[0])

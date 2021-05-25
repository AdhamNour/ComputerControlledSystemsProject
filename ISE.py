import math
from AnalyticalPoint import getPointInAnalyticalModel

def ISE(yapprox,Tsampling):
    n = len(yapprox)
    summedArea=0
    summedAreaVector=[]
    for i in range(n):
        error = getPointInAnalyticalModel(i*Tsampling)-yapprox[i]
        error2 = math.pow(error,2)
        summedAreaVector.append(summedArea)
        summedArea = summedArea + error2*Tsampling
    return summedAreaVector
import math;
def getExactModel(Tsim,Tsampling):
    w= math.exp(-2.1*Tsampling)*math.cos(math.sqrt(4.59)*Tsampling)
    a = (1/(math.sqrt(4.59)))*math.exp(-2.1*Tsampling)*math.sin(math.sqrt(4.59)*Tsampling)
    x=[[0],[0]]
    n=int(Tsim/Tsampling)
    timeAxis=[0]
    for i in range(n):
        x1k=x[0][i]
        x2k=x[1][i]
        
        x1k1=(x1k+(4/9))*w+(2.1*x1k+x2k+(0.6/9))*a+(4/9)
        x2k1=(x2k+1)*w+(-9*x1k-2.1*x2k+(17.1/9))*a-1
        x[0].append(x1k1)
        x[1].append(x2k1)
        timeAxis.append((i+1)*Tsampling)
    return (timeAxis,x[0])

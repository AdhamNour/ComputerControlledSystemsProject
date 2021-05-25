import matplotlib.pyplot as plt
import math
from AnalyticModel import getAnalyticModel
from ApproxModel import getApproxModel
from ISE import ISE

Tsamples =[0.001,0.01,0.1,0.5,1]

for i in Tsamples:
    plt.figure()
    (x,y) = getAnalyticModel(10)
    plt.subplot(221)
    plt.plot(x, y)
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.title("The Analytical response of the System")

    (xapprox,yapprox) = getApproxModel(10,i)
    plt.subplot(222)
    plt.plot(xapprox, yapprox)
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.title("The Approx response of the System")

    errors = ISE(yapprox,i)
    plt.subplot(212)
    plt.plot(xapprox, errors)
    plt.xlabel("time")
    plt.ylabel("error")
    plt.title("The error between the approx and analytical responces")

plt.show()

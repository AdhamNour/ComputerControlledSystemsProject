import matplotlib.pyplot as plt
import math
import numpy as np

from AnalyticModel import getAnalyticModel
from ApproxModel import getApproxModel
from ExactModel import getExactModel
from ISE import ISE

Tsamples =[]

for i in range(7):
    Tsamples.append(math.pow(10,-1*i))


for i in Tsamples:
    plt.figure()
    (x,y) = getAnalyticModel()
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

for i in Tsamples:
    plt.figure()
    plt.suptitle(i)
    (x,y) = getAnalyticModel()
    plt.subplot(221)
    plt.plot(x, y)
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.title("The Analytical response of the System")

    (xapprox,yapprox) = getExactModel(10,i)
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


# A= np.array([[0,1], [-9,-4.2]])
# invA=np.linalg.inv(A)

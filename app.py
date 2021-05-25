import matplotlib.pyplot as plt
import math
from AnalyticModel import getAnalyticModel
from ApproxModel import getApproxModel

plt.figure()
(x,y) = getAnalyticModel(10)
plt.subplot(212)
plt.plot(x, y)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("The Analytical response of the System")

(xapprox,yapprox) = getApproxModel(10,0.1)
plt.subplot(221)
plt.plot(xapprox, yapprox)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("The Approx response of the System")

plt.show()

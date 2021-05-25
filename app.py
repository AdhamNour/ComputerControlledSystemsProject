import matplotlib.pyplot as plt
from AnalyticModel import getAnalyticModel
from ApproxModel import getApproxModel

(x,y) = getApproxModel(10,0.01)

plt.plot(x, y)
plt.show()
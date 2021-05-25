import matplotlib.pyplot as plt
from AnalyticModel import getAnalyticModel

(x,y) = getAnalyticModel(10)

plt.plot(x, y)
plt.show()
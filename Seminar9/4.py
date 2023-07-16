import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
x= np.array([ 10, 8, 9, 11, 14, 6, 4, 12, 7, 5 ])
y = np.array([7.46, 6.77, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x2 = x.reshape((10, 1))
y2= y.reshape((10, 1))
x3 = np.hstack([np.ones((10, 1)), x2])
b = np.dot(np.linalg.inv(np.dot(x3.T, x3)), x3.T@ y2)
print(b)
print((np.corrcoef(x,y)[0, 1])**2)
plt.scatter(x, y)
plt.plot(x, b[0] + b[1] * x)
plt.show
y_pred = b[0] + b[1]*x
print(y_pred)
resid = y - y_pred
stats.shapiro(resid)
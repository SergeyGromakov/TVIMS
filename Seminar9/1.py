# Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# линейной регрессии.


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
# x1 = np.array([30, 30, 40, 40])
# y1 = np.array([37, 47, 50, 60])
# b1 = (np.mean(x1*y1)-np.mean(x1)*np.mean(y1))/(np.mean(x1**2)-np.mean(x1)**2)
# print(b1)
# b0 = np.mean(y1)-b1*np.mean(x1)
# print(b0)
# r= np.corrcoef(x1, y1)[0, 1]
# print(r)
# plt.scatter(x1, y1)
# plt.plot(x1, b0 + b1*x1)
# plt.show

# x1 = np.array([30, 30, 40, 40, 20, 20, 50, 50])
# y1 = np.array([37, 47, 50, 60, 25, 35, 62, 72])
# b1 = (np.mean(x1*y1)-np.mean(x1)*np.mean(y1))/(np.mean(x1**2)-np.mean(x1)**2)
# print(b1)
# b0 = np.mean(y1)-b1*np.mean(x1)
# print(b0)
# r= np.corrcoef(x1, y1)[0, 1]
# print(r)
# plt.scatter(x1, y1)
# plt.plot(x1, b0 + b1*x1)
# plt.show

x1 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
y1 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])
b1 = (np.mean(x1*y1)-np.mean(x1)*np.mean(y1))/(np.mean(x1**2)-np.mean(x1)**2)
print(b1)
b0 = np.mean(y1)-b1*np.mean(x1)
print(b0)
r= np.corrcoef(x1, y1)[0, 1]
print(r)
plt.scatter(x1, y1)
plt.plot(x1, b0 + b1*x1)
plt.show

x2 = x1.reshape((12, 1))
y2= y1.reshape((12, 1))
x3 = np.hstack([np.ones((12, 1)), x2])
b = np.dot(np.linalg.inv(np.dot(x3.T, x3)), x3.T@ y2)
print (b)
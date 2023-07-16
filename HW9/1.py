# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): 
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), 
# а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
b1 = (np.mean(zp*ks)-np.mean(zp)*np.mean(ks))/(np.mean(zp**2)-np.mean(zp)**2)
print(b1)
b0 = np.mean(ks)-b1*np.mean(zp)
print(b0)
r= np.corrcoef(zp, ks)[0, 1]
print(r)
plt.scatter(zp, ks)
plt.plot(zp, b0 + b1*zp)
plt.xlabel('Зарплата')
plt.ylabel('Кредитный скоринг')
plt.show


x2 = zp.reshape((10, 1))
y2= ks.reshape((10, 1))
b = np.dot(np.linalg.inv(np.dot(x2.T, x2)), x2.T@ y2)
print (b)
plt.scatter(zp, ks)
plt.plot(zp, b[0] * zp)
plt.show
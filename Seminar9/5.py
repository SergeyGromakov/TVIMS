# Оценить статистическую значимость полученной модели линейной регрессии

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
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
pred = b0 + b1*x1
print(stats.f.ppf(0.95, 1, 10))
ssf= np.sum((pred-np.mean(y1))**2)
sso = np.sum((y1-pred)**2)
msf = ssf/1
mso = sso/10
f = msf/mso
print(f)
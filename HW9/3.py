# Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно 
# производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение 
# другого во время одной итерации).

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
def mse (B0, B1, zp = zp, ks = ks, n = 10):
    return np.sum((B0 + B1 * zp - ks)**2)/n

alpha = 5e-5
B1 = 0.1
B0 = 0.1
n = len(zp)
for i in range (1000000):
    B0 -= alpha * (2/n) * np.sum((B0 + B1 * zp - ks))
    B1 -= alpha * (2/n) * np.sum((B0 + B1 * zp - ks) * zp)
    if i % 100000 == 0:
        print('Итерация = {i}, B0 = {B0}, B1 = {B1}, mse = {mse}'.format (i = i, B0 = B0, B1 = B1, mse = mse(B0, B1)))

#  Ответ Итерация = 600000, B0 = 444.17724836347435, B1 = 2.6205396843827113, mse = 6470.41420117967
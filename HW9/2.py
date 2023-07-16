# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
def mse (B1, zp = zp, ks = ks, n = len(zp)):
    return np.sum((B1 * zp - ks)**2)/n

alpha = 1e-6
B1 = 0.1
n = len(zp)
for i in range (1000):
    B1 -= alpha * (2/n) * np.sum((B1 * zp - ks) * zp)
    if i % 100 == 0:
        print('Итерация = {i}, B1 = {B1}, mse = {mse}'.format (i = i, B1 = B1, mse = mse(B1)))
# После 700й итерации отклонение перестает уменьшаться, ответ:
# Итерация = 700, B1 = 5.889820402076462, mse = 56516.85841571941
# Провести двусторонний тест и ответить на вопрос, есть ли статистически значимые
# различия между средними 2х нормально распределенных генеральных совокупностей,
# представленных следующими независимыми выборками:
#  a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
#  b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])
# Уровень статистической значимости принять за 5%
# 1 . Используйте функцию в Python:
# 2. Имея p-value из функции рассчитать наблюдаемое значение критерия.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])
print(stats.ttest_ind(a, b))
print(np.corrcoef(a,b))
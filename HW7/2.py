# 2 ) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление 
# до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?

# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150,  130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

# Поскольку у нас 3 выборки значений по одним и тем же людям, то используем критерий Фридмана, альфа = 0,05

import numpy as np
import scipy.stats as stats
x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150,  130, 135])
x3 = np.array([130, 130, 120, 130, 125])
print(stats.friedmanchisquare(x1, x2, x3)) 

# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)
# тк pvalue меньше alpha принимаем альтернативную гипотезу и понимаем, что есть статистически значимые различия, 
# т.е. можно предположить, что препарат действует 
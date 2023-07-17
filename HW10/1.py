# Провести дисперсионный анализ для определения того, есть ли различия среднего роста 
# среди взрослых футболистов, хоккеистов и штангистов. Даны значения роста в трех группах случайно выбранных 
# спортсменов: Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170. 

import numpy as np
import scipy.stats as stats
footbalists = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockeyists = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
print(stats.shapiro(footbalists))
print(stats.shapiro(hockeyists))
print(stats.shapiro(weightlifters))

# ShapiroResult(statistic=0.9775082468986511, pvalue=0.9495404362678528)
# ShapiroResult(statistic=0.9579196572303772, pvalue=0.7763139009475708)
# ShapiroResult(statistic=0.9386808276176453, pvalue=0.5051165223121643)
# Поскольку все pvalue больше 0,05, то делаем вывод, что верна нулевая гипотеза, т.е. веса в 3 выборках распределены 
# нормально

print (stats.bartlett(footbalists, hockeyists, weightlifters))
# BartlettResult(statistic=0.4640521043406442, pvalue=0.7929254656083131)
# pvalue больше alpha, а значит это зона принятия нулевой гипотезы, то есть дисперсии однородны
# У нас соблюдены условия для проведения однофакторного дисперсионного анализа(фактор - вид спорта, показатель - рост).

print(stats.f_oneway(footbalists, hockeyists, weightlifters))

# F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698693) - pvalue ы зоне принятия альтернативной гипотезы, 
# что означает, что в росте спортсменов в 3х видах спорта есть статистически значимые различия 

print(stats.tukey_hsd(footbalists, hockeyists, weightlifters))

# Comparison  Statistic  p-value  Lower CI  Upper CI
#  (0 - 1)      0.458     0.979    -5.357     6.273
#  (0 - 2)      6.398     0.022     0.837    11.958
#  (1 - 0)     -0.458     0.979    -6.273     5.357
#  (1 - 2)      5.939     0.028     0.561    11.318
#  (2 - 0)     -6.398     0.022   -11.958    -0.837
#  (2 - 1)     -5.939     0.028   -11.318    -0.561

# Post Hoc Test говорит нам о том, что у футболистов и хоккеистов рост статистичнски одинаковый, но он отличается от роста
#  штангистов.
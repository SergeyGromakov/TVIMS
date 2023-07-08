# Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, 
# равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
import scipy.stats as stats
print(stats.norm.ppf(0.975))
z = 1.959963984540054
print(f'С вероятностью 95% среднее значение генеральной совокупности будет лежать в интервале\
      [{174.2 - z*np.sqrt(25/27)}, {174.2 + z*np.sqrt(25/27)}]')
# Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга 
# (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. 
# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy 
# Полученные значения должны быть равны. Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных 
# отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import matplotlib.pyplot as plt
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
print(f'смещенна ковариация равна {np.mean(zp*ks)-np.mean(zp)*np.mean(ks)}')
print(np.cov(zp, ks, ddof=0))
print(f'корелляция равна {(np.mean(zp*ks)-np.mean(zp)*np.mean(ks))/(np.std(zp, ddof=0)*np.std(ks, ddof=0))}')
print(np.corrcoef(zp, ks))
plt.scatter(zp, ks)
plt.show

# использовал смещенную ковариацию, т.к. наша формула ручная M(x*y)-M(X)*M(Y) выдает именно смещенное значение, 
# и в этом случае мы используем и смещенные сигмы
# коэффициент и график говорят о сильной прямой линейной зависимости - выше з/пл - выше кредитный рейтинг
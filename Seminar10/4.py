import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
before = np.array([92.8 , 95.6, 92.1, 100.6, 96.2, 92.1, 96.7, 97.6, 97.0, 93.9])
after = np.array([87.1, 84.1, 81.3, 77.0, 86.0, 82.9, 83.0, 85.5, 85.2, 84.6])
stats.ttest_rel(before, after)
stats.ttest_rel(before, after, alternative = 'greater')
stats.ttest_rel(before, after, alternative = 'less')
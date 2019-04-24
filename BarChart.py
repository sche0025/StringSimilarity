# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import matplotlib.pyplot as plt
import numpy as np

N = 2
GED = (4.58, 35.34)
LED = (0.02, 22.21)
N_Gram = (9.98,21.23)

ind = np.arange(N)
width = 0.30
plt.bar(ind, GED, width, label='GED')
plt.bar(ind + width, LED, width,
    label='LED')
plt.bar(ind + 2*width, N_Gram, width,
    label='N-Gram')

plt.ylabel('Percentage')
plt.title('Statistics for performance')

plt.xticks(ind + width / 1.2, ('      Precision', '        Recall'))
plt.legend(loc='best')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

print np.random.binomial(1, 0.5, 10)
plt.hist(np.random.binomial(100, 0.5, 10000), bins=1000)
plt.show()

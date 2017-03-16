import numpy as np
import matplotlib.pyplot as plt

heights_file = file('/Users/ctang/Desktop/heights.txt')
heights = [float(height_str) for height_str in heights_file]
plt.hist(np.array(heights), bins=45)
plt.show()

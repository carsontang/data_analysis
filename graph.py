import matplotlib.pyplot as plt
import scipy
import scipy.stats
import numpy as np
dist_names = ['norm', 'expon']
file = open("/Users/ctang/dev/cs109/time_between_msgs.csv")
timebtwn = np.array([float(l) for l in file])
x = np.linspace(min(timebtwn), max(timebtwn), len(timebtwn))


plt.hist(timebtwn, bins=100)

for dist_name in dist_names:
	dist = getattr(scipy.stats, dist_name)
	param = dist.fit(timebtwn)
	print param
#	mu = param[0]
	sigma = param[1]
	pdf_fitted = dist.pdf(x, loc=param[-2], scale=param[-1])
	plt.plot(pdf_fitted, label=dist_name)
plt.legend(loc='upper right')
plt.show()

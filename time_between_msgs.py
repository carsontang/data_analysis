from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

file = open("/Users/ctang/dev/cs109/time_between_msgs.csv")
timebtwn = np.array([float(l) for l in file])
mu = np.mean(timebtwn)
lmbda = 1/mu

print mu
# I want to find t s.t. P(T > t) = 0.01

count, b, ignored = plt.hist(timebtwn, bins=100)
# x = np.linspace(min(b), max(b), 10000)
x = np.linspace(0.0, 107028.0, 10000)
pdf = (lmbda * np.exp(-lmbda * x))
# plt.plot(x, pdf, linewidth=2, color='r')
plt.show()

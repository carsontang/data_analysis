import numpy as np
import matplotlib.pyplot as plt

prices_file = open("/Users/ctang/Desktop/prices.csv")
prices = np.array([float(l) for l in prices_file])
print np.mean(prices)
prices = prices / np.min(prices)
mu = np.mean(np.log(prices))
sigma = np.std(np.log(prices))
s = np.random.lognormal(mu, sigma, 1000)
count, b, ignored = plt.hist(s, 100, normed=True, align='mid')
# count, b, ignored = plt.hist(prices, bins=100, range=(10,3500))
x = np.linspace(min(b), max(b), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.show()

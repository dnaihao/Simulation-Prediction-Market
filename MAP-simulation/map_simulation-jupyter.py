#%%
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

#%% [markdown]
# Import csv file as a pandas DataFrame
#%%
def import_csv(path, column):
    res = pd.read_csv(path)
    res = res[column]
    return list(res)

#%% [markdown]
# Initialize parameters
#%%
m = 49      # The mean of the prior distribution
v = 1       # The variance of the prior distribution
mu = m      # Prior mean: set to be `m`
sigma = v   # Prior variance: set to be `v`

#%% [markdown]
# Draw pdf according to prior
#%%
t = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
probability = stats.norm.pdf(t, mu, sigma)
plt.plot(t, probability)

#%% [markdown]
# Generate data point; assume data are drawn from a normal distribution of known mean and variance (70, 1)
#%%
data = np.random.normal(70, 1, 1000)

#%% [markdown]
# Calculate posterior mean
#%%
mu = ((v ** 2) * (np.sum(data)) + (sigma ** 2) * m) / (len(data) * (v ** 2) + sigma ** 2)

#%% [markdown]
# Draw pdf according to posterior
#%%
t = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
probability = stats.norm.pdf(t, mu, sigma)
plt.plot(t, probability)

#%% [markdown]
# Validate distribution of data points with histogram
#%%
plt.hist(data, bins=100, density=True)

#%%
plt.show()

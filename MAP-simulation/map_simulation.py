import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import math


def import_csv(path, column):
    """
    Import csv file as a pandas DataFrame
    """
    res = pd.read_csv(path)
    res = res[column]
    return list(res)


def main():
    # Initialize parameters
    # Here we only discuss normal distribution of unknown mean and known variance.
    # For a normal distribution:
    # - Conjugate prior for mean:       normal
    # - Conjugate prior for variance:   Inverse Gamma (too complicated?)
    #
    # FYI, see references/Stanford-MAP.pdf
    #
    # (Really? The following implementation is not the case... Variance is still updated)

    m = 50              # The mean of the prior distribution
    v = 10              # The variance of the prior distribution
    mu = m              # Prior mean: set to be `m`
    sigma = 1           # Variance is fixed; say 1

    # Draw pdf according to prior
    t = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    probability = stats.norm.pdf(t, mu, sigma)
    plt.plot(t, probability)

    # Generate data point
    # Assume data are drawn from a normal distribution of known mean and variance (60, 1)
    data = np.random.normal(50, 1, 10)

    # Calculate posterior mean
    # 
    # FYI, see references/Density Estimation (ML, MAP, Bayesian).pdf
    # This reference must have some calculation errors, but the method is worth discussing!
    #
    # >>> FIXME: The following updating method CONTAINS the calculation errors! 
    m = ((v ** 2) * (np.sum(data)) + (v ** 2) * (sigma ** 2) * m) / (len(data) * (v ** 2) + sigma ** 2)
    v = math.sqrt(((v ** 2) * (sigma ** 2)) / (len(data) * (v ** 2) + sigma ** 2))
    mu = m
    sigma = math.sqrt(sigma ** 2 + v ** 2)


    # Draw pdf according to posterior
    t = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    probability = stats.norm.pdf(t, mu, sigma)
    plt.plot(t, probability)

    # Show legend 
    plt.legend(('prior', 'posterior'))

    # Validate distribution of data points with histogram
    # plt.hist(data, bins=100, density=True)

    # Show figure
    plt.show()
    

if __name__ == "__main__":
    main()
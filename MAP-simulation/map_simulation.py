import pandas as pd
import matplotlib.pyplot as plt
import math

def import_csv(path, column):
    """Import csv file as a pandas DataFrame"""
    res = pd.read_csv(path)
    res = res[column]
    return list(res)


def prior_pdf(theta, mean, variance):
    """Calculate probability density for normal distribution
    :param float theta: value
    :param float mean: mean of prior distribution
    :param float variance: variance of prior distribution
    """
    return 1/(math.sqrt(2*math.pi*variance)) \
                * math.exp(-((theta-mean)**2)/(2*variance))

def main():
    data = import_csv("../Data/Bike-Sharing-Dataset/hour.csv", "registered")
    m = 49 # The mean of the prior distribution
    v = 1 # The variance of the prior distribution
    mean = 50 # Prior mean
    var = 1 # Prior variance
    prior = prior_pdf(mean, m, 1)
    probability = [prior_pdf(x, mean, var) for x in data]
    import pdb; pdb.set_trace()
    plt.plot(data, probability)
    plt.show()


if __name__ == "__main__":
    main()

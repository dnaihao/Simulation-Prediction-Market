#!/usr/bin/env python3
from math import log

class MarketMaker():
    """
    market maker (two securities)
    """

    def __init__(self):
        self.size = None                        # number of collected datapoint:
                                                # reliability of collected information (list)
        self.mean = None                        # aggregated belief == current market price (list)
        self.security_amount = None             # number of securities market maker has (list)
        self.outstanding_security_amount = 0    # number of securities market maker sold so far (list)

    @staticmethod
    def sufficient_statistic(x):
        """
        phi(x) Gaussian distribution
        :param x:
        :return:
        """
        return [x, x**2]

    def set_param(self, random = False, security_amount = 1000):
        """
        configure initial parameters
        :param random: whether size and mean should be set randomly
        :return:
        """
        self.security_amount = security_amount
        if random:
            pass
        else:
            pass

    def cost_func(self):
        """
        cost function == log partition func
        :return:
        """
        return -(self.outstanding_security_amount[0]**2/(4*self.outstanding_security_amount[1]))\
        -0.5*log(-2*self.outstanding_security_amount[1])

    def current_market_price(self):
        """
        take derivative of the cost func, hardcode it here
        :return: list of two securities' prices
        """
        pass

    def sell(self):
        """
        corresponding to agent's buy, update security amount, outstanding security amount
        :return:
        """
        pass

    def buy(self):
        """
        corresponding to agent's sell, update security amount, outstanding security amount
        :return:
        """
        pass

    def update_param(self, agent_size, agent_mean):
        """
        update belief based on agents' parameter
        :param: agent_size: agent_mean:
        :return:
        """
        # update mean
        self.mean = (self.size * self.mean + agent_size * agent_mean)/(self.size + agent_size)
        # update size
        self.size += agent_size

    def validate_param(self):
        """
        validate whether current prices equals to aggregated means
        :return: bool value
        """
        return self.mean == self.current_market_price()
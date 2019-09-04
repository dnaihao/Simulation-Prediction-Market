#!/usr/bin/env python3

from math import log, exp


class MarketMaker:
    """
    market maker (one security for Bernoulli and Gaussian)
    """

    def __init__(self, distribution):
        self.num_trade = 0
        self.distribution = distribution
        # the impact of the initial market price on prediction result is unknown
        self.outstanding_security_amount = 0
        if distribution == "Bernoulli":
            self.current_market_price = 0.5
        elif distribution == "Gaussian":
            self.current_market_price = 0


    @staticmethod
    def sufficient_statistic(x):
        """sufficient statistics for Bernoulli is x,
        sufficient statistics for Gaussian with known variance is x"""
        return x


    # TODO: determine what the equilibrium criteria is
    def market_equilibrium(self, last_market_price, difference=0.01):
        """
        Determine whether the market prices have reached equilibrium
        """
        if abs(self.current_market_price - last_market_price) <= difference and\
        self.num_trade > 1000:
            return True
        else:
            return False


    def calc_current_market_price(self, eta):
        """
        calculate current market price
        :param: eta: number of securities on the market
        :return: current market price
        """
        if self.distribution == "Bernoulli":
            p = exp(eta)/(1 + exp(eta))
        elif self.distribution == "Gaussian":
            p = eta
        return p


    def update_param(self, delta):
        """
        update number of trades
        :param: delta
        :return:
        """
        self.num_trade += 1
        # update outstanding shares
        self.outstanding_security_amount += delta
        # update current price from the perspective of market maker
        # should be the same with the current agent's posterior (IMPORTANT)
        self.current_market_price = \
        self.calc_current_market_price(self.outstanding_security_amount)

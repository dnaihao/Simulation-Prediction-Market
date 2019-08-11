#!/usr/bin/env python3
from math import log, exp


class MarketMaker:
    """
    market maker (two securities)
    """

    def __init__(self):
        self.num_trade = 0
        self.outstanding_security_amount = 0                    # number of securities in the market (list)
        self.current_market_price = 0.5                         # with current delta, theta_2 is always negative

    @staticmethod
    def sufficient_statistic(x):
        """
        phi(x) Bernoulli distribution
        :param x:
        :return:
        """
        return x

    def cost_func(self):
        """
        cost function == log partition func
        :return:
        """
        return log(1 + exp(self.outstanding_security_amount))

    @staticmethod
    def calc_current_market_price(eta):
        """
        calculate current market price
        :param: eta:
        :return: current market price
        """
        p = exp(eta)/(1 + exp(eta))
        return p

    def update_param(self, delta):
        """
        update number of trades
        :param: delta
        :return:
        """
        self.num_trade += 1
        self.outstanding_security_amount += delta           # update outstanding shares

        # update current price from the perspective of market maker
        # should be the same with the current agent's posterior
        self.current_market_price = self.calc_current_market_price(self.outstanding_security_amount)

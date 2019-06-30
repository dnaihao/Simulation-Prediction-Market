#!/usr/bin/env python3
from math import log


class MarketMaker:
    """
    market maker (two securities)
    """

    def __init__(self):
        self.num_trade = 0
        self.outstanding_security_amount = [1/100, -1/20000]    # number of securities in the market (list)
        self.current_market_price = [100, 20000]                # with current delta, theta_2 is always negative

    @staticmethod
    def sufficient_statistic(x):
        """
        phi(x) Gaussian distribution
        :param x:
        :return:
        """
        return [x, x**2]

    def cost_func(self):
        """
        cost function == log partition func
        :return:
        """
        return -(self.outstanding_security_amount[0]**2/(4 * self.outstanding_security_amount[1])) \
            - 0.5 * log(-2 * self.outstanding_security_amount[1])

    @staticmethod
    def calc_current_market_price(theta_1, theta_2):
        """
        calculate current market price
        :param: theta_1:
        :param: theta_2:
        :return: current market price
        """
        p_1 = -theta_1/(2 * theta_2)
        p_2 = (theta_1 ** 2) /(4 * (theta_2 ** 2)) -1 / (2 * theta_2)
        return p_1, p_2

    def update_param(self, delta_1, delta_2):
        """
        update number of trades
        :param: delta_1:
        :param: delta_2:
        :return:
        """
        self.num_trade += 1
        self.outstanding_security_amount[0] += delta_1      # delta>0: agent buys, market maker sells
        self.outstanding_security_amount[1] += delta_2      # delta<0: agent sells, market maker buys
        self.current_market_price[0], self.current_market_price[1] \
            = self.calc_current_market_price(self.outstanding_security_amount[0]
                                             , self.outstanding_security_amount[1])

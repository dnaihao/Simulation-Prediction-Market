#!/usr/bin/env python3

from math import log


class BayesianAgent:
    """
    bayesian agent
    """

    def __init__(self, update_size=10):
        self.security_amount = 0         # one security amounts
        # m
        self.update_size = update_size
        # niu in our notation
        self.datapoints = None
        # niu*Chi in our notation
        self.total = None

    @staticmethod
    def u(x):
        """
        sufficient statistic function for Bernoulli
        :param x:
        :return:
        """
        return x

    def update_param(self, data, trade_num, current_market_price):
        """

        :param data: the data observed by the agent before his entrance to the market
        :param trade_num: current trade number published by market maker
        :param current_market_price:
        :return:
        """
        # niu = nm
        self.datapoints = trade_num * self.update_size + self.update_size

        sum_of_data = sum([self.u(x) for x in data])
        # niu * Chi
        self.total = sum_of_data + trade_num * self.update_size *current_market_price

    @staticmethod
    def calculate_outstanding_shares(current_market_price):
        """
        Calculate the number of outstanding shares using the current market price
        by:
            P(eta) = e ** eta / (1 + e **eta)
        :return: eta: outstanding shares in market currently
        """
        # base not specified, get the natural log
        return log(current_market_price / (1 - current_market_price))

    # def calculate_belief(self):
    #     """
    #      Calculate belief of agent based on market price by
    #      (n * niu + m * miu) / (n + m)
    #      , which is the updated mean
    #     :return: belief
    #     """
    #     return self.mean

    def calculate_shares_to_buy(self, current_market_price):
        """
        Calculate the number of shares agents should purchase to move the current market price to his or her expectation
        :param  current_market_price:
        :return:
        """
        # eta: outstanding shares in market currently
        eta = self.calculate_outstanding_shares(current_market_price)
        # print("private signal: {}, belief_1: {}".format(self.mean, belief_1))
        # print()
        delta = log(self.total/(self.datapoints - self.total)) - eta
        return delta

    def update_security(self, delta):
        """
        Update the number of securities an agent has based on whether he or she buys or sells securities
        :return:
        """
        # A positive delta stands for a buy, a negative delta stands for a sell
        self.security_amount += delta



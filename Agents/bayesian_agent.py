#!/usr/bin/env python3

from statistics import mean
from math import sqrt


class BayesianAgent:
    """
    bayesian agent
    """

    def __init__(self, data, update_size=10):
        self.size = len(data)            # size of dataset: reliability of his private signal
        self.mean = mean(data)           # private signal: random assigned
        # self.decision = False            # sell(False) or buy(True) security
        self.security_amount = 0         # two security amounts
        self.update_size = update_size
        # self.budget = None: might be used in future

    def update_param(self, data):
        """
        update private signal based on observed samples
        :param data: the data observed by the agent after entering the market
                     length of the data should be self.update_size
        :return:
        """
        self.mean = (self.mean * self.size + self.update_size * mean(data))/(self.update_size + self.size)
        self.size += self.update_size

    @staticmethod
    def calculate_outstanding_shares(current_market_price):
        """
        Calculate the number of outstanding shares using the current market price
        by:
            P(theta) = -1/theta
        :return: theta
        """
        return -1/current_market_price

    def calculate_belief(self):
        """
         Calculate belief of agent based on market price by
         (n * niu + m * miu) / (n + m)
         , which is the updated mean
        :return: belief
        """
        return self.mean

    def calculate_shares_to_buy(self, current_market_price):
        """
        Calculate the number of shares agents should purchase to move the current market price to his or her expectation
        :param  current_market_price: list of prices
        :return:
        """
        theta = self.calculate_outstanding_shares(current_market_price)
        belief = self.calculate_belief()
        # print("private signal: {}, belief_1: {}".format(self.mean, belief_1))
        # print()
        delta = -1/belief - theta
        return delta

    def update_security(self, delta):
        """
        Update the number of securities an agent has based on whether he or she buys or sells securities
        :return:
        """
        # A positive delta stands for a buy, a negative delta stands for a sell
        self.security_amount += delta



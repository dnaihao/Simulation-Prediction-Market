#!/usr/bin/env python3

from statistics import mean
from math import sqrt


class BayesianAgent:
    """
    bayesian agent
    """

    def __init__(self, data, update_size=10):
        self.size = len(data)           # size of dataset: reliability of his private signal (list)
        self.mean = mean(data)        # private signal: random assigned (list)
        self.sqr_mean = mean([x**2 for x in data])
        self.decision = [False, False]            # sell(False) or buy(True) security (list of bool)
        self.security_amount = [0, 0]     # two security amounts (list)
        self.update_size = update_size
        # self.budget = None: might be used in future

    def update_param(self, data):
        """
        update private signal based on observed samples
        :param data: the data observed by the agent after entering the market
                     length of the data should be self.update_size
        :return:
        """
        # print("data: {}".format(data))
        # print("data mean: {}".format(mean(data)))
        self.mean = (self.mean * self.size + self.update_size * mean(data))/(self.update_size + self.size)
        sqr_data_mean = mean([x**2 for x in data])
        self.sqr_mean = (self.sqr_mean * self.size + self.update_size * sqr_data_mean)/(self.update_size + self.size)
        self.size += self.update_size

    @staticmethod
    def calculate_outstanding_shares(current_market_price):
        """
        Calculate the number of outstanding shares using the current market price
        :return: theta_1, theta_2
        """
        p_1, p_2 = current_market_price[0], current_market_price[1]
        theta_1 = p_1/(p_2-p_1**2)
        theta_2 = 0.5/(p_1**2-p_2)
        return theta_1, theta_2

    def calculate_belief(self, num_trades, current_market_price, security_type="X"):
        """
         Calculate belief of agent based on market price
        :param security_type: takes two values, "X" or "X_sqr"
        :param num_trades: n
        :param current_market_price: niu
        :return: belief
        """
        if security_type == "X":
            return (num_trades * current_market_price + self.mean) / (num_trades + 1)
        elif security_type == "X_sqr":
            return (num_trades * current_market_price + self.sqr_mean) / (num_trades + 1)

    def calculate_shares_to_buy(self, num_trades, current_market_price):
        """
        Calculate the number of shares agents should purchase to move the current market price to his or her expectation
        :param  num_trades: the number of trades the market maker has seen in market
        :param  current_market_price: list of prices
        :param  security_type: 0 is X security, 1 is X**2 security
        :return:
        """
        theta_1, theta_2 = self.calculate_outstanding_shares(current_market_price)
        belief_1 = self.calculate_belief(num_trades, current_market_price[0], "X")
        # print("private signal: {}, belief_1: {}".format(self.mean, belief_1))
        # print()
        belief_2 = self.calculate_belief(num_trades, current_market_price[1], "X_sqr")
        delta_1 = belief_1 / (belief_2 - belief_1**2) - theta_1
        delta_2 = - theta_2 - 1/(2 * (belief_2 - belief_1**2))
        return delta_1, delta_2

    def update_security(self, delta_1, delta_2):
        """
        Update the number of securities an agent has based on whether he or she buys or sells securities
        :return:
        """
        # A positive delta stands for a buy, a negative delta stands for a sell
        self.security_amount[0] += delta_1
        self.security_amount[1] += delta_2



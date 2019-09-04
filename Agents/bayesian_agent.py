#!/usr/bin/env python3

from math import log


class BayesianAgent:
    """
    bayesian agent
    We are making a very simple assumption here.
    We don't check if the agent has securities to trade in the first place :/
    """

    def __init__(self, distribution):
        """
        distribution: the type of distribution (either Bernoulli or Gaussian)
        """
        self.distribution = distribution

    @staticmethod
    def u(x):
        """
        sufficient statistic function for Bernoulli and Gaussian
        :param x:
        :return:
        """
        return x

    def calculate_outstanding_shares(self, current_market_price):
        """
        Calculate the number of outstanding shares using the current market price
        by:
            (Bernoulli) P(eta) = e ** eta / (1 + e **eta)
            (Gaussian) P(eta) = eta
        :return: eta: outstanding shares in market currently
        """
        if self.distribution == "Bernoulli":
            # TODO: what to do when current_market_price is 1 ???
            return log(current_market_price / (1 - current_market_price))
        elif self.distribution == "Gaussian":
            return current_market_price


    def calculate_shares_to_buy(self, data, posted_num_trade,\
    current_market_price):
        """
        Calculate the number of shares agents should purchase to move the\
        current market price to his or her expectation
        :param  data: the data the agent sees
                posted_num_trade: the number of trades that is posted by
                MarketMaker
                current_market_price: current market price
        :return: number of shares the agent buys, the price after the
         transaction
        """
        eta = self.calculate_outstanding_shares(current_market_price)
        posterior = self.agent_posterior(data, posted_num_trade,\
        current_market_price)
        return (self.calculate_outstanding_shares(posterior) - eta), posterior


    def agent_posterior(self, data, posted_num_trade, current_market_price):
        """
        The agent takes a look at the current market price, and adjusts his or
        her belief
        miu = (n*chi+miu)/(n+1)
        :return: posterior: the updated posterior
        """
        prior = sum([BayesianAgent.u(x) for x in data])/len(data)
        posterior = (posted_num_trade * current_market_price + prior)/\
        (posted_num_trade + 1)
        return posterior

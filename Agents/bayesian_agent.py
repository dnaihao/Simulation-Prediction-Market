#!/usr/bin/env python3


class BayesianAgent():
    """
    bayesian agent
    """

    def __init__(self):
        self.size = None                # size of dataset: reliability of his private belief (list)
        self.mean = None                # private belief: random assigned (list)
        self.decision = None              # sell or buy security (list of bool)
        self.security_amount = None     # two security amounts (list)
        # self.budget = None: might be used in future

    # def set_random_param(self):
    #     """
    #     randomly assign size and mean
    #     :return:
    #     """
    #     pass
    #
    # def set_fixed_param(self):
    #     """
    #     manually assign size and mean
    #     :return:
    #     """
    #     pass
    #     TODO: change it as format in market maker
    def set_param(self, random = False):
        pass

    def compare_belief_current_price(self, current_market_price):
        """
        compare agent's private belief with current market price
        :param current_market_price:
        :return:
        """
        pass

    def sell(self):
        """
        decide which of the two security to sell,
         sell security, update security amount
        :return:
        """
        pass

    def buy(self):
        """
        decide which of the two security to buy,
         buy security, update security amount
        :return:
        """
        pass

    def update_param(self, current_market_price):
        """
        update private beliefs based on current market price
        :param current_market_price:
        :return:
        """
        pass

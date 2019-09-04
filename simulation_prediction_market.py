#!/usr/bin/env python3
"""

Simulation Prediction Market Main Executable

"""

import argparse
import pandas as pd
import numpy as np
from Agents.bayesian_agent import BayesianAgent
from Market_Maker.market_maker import MarketMaker


def parse_command_line():
    """
    argument parser
    :return: args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dataset", type=str, help="specify path to the dataset"
    )
    parser.add_argument(
        "column_name", type=str, help="specify column name in the dataframe to\
        make a prediction on"
    )
    parser.add_argument(
        "-d", "--distribution", type=str, help="specify either Bernoulli\
        or Gaussian distribution", choices=["Gaussian", "Bernoulli"]
    )
    args = parser.parse_args()

    return args


def import_data(path, column_name):
    """
    import real data from csv file
    :param: path: str, data path
    :return: processed_list: list, list of actual data
    """
    res = pd.read_csv(path)
    processed_list = res[column_name].tolist()
    return processed_list

def main():
    args = parse_command_line()
    data_path = args.dataset

    # the number of datapoints agent observes at a time
    # same across all agents
    num_observed_sample = 4

    # import data
    data = import_data(data_path, args.column_name)
    real_outcome = sum(data) / len(data)

    # initialize market maker
    mk = MarketMaker(distribution=args.distribution)

    ############### Agents enter with Poisson distribution ###############
    # enter_times = np.random.poisson(7.5, max_iteration)
    # lambda*max_iteration ~= size of dataset
    # enter_times = list(np.cumsum(enter_times) + num_observed_sample)
    ######################################################################

    # The agent are now all the same
    # They observe different data points though
    try:
        agent = BayesianAgent(distribution=args.distribution)
    except TypeError:
        return

    enter_time = 0
    # The number of agents in this market is not pre-ordained
    # The trade will stop once the market reached equilibrium
    while True:
        last_market_price = mk.current_market_price
        observed_data = data[enter_time: enter_time + num_observed_sample]
        enter_time += num_observed_sample
        # Out of data to observe
        if enter_time > len(data):
            break
        shares_to_buy, _ = agent.calculate_shares_to_buy(observed_data,\
         mk.num_trade, mk.current_market_price)
        mk.update_param(shares_to_buy)
        # TODO: equilibrium is necessary in real life market, not a must here
        if mk.market_equilibrium(last_market_price):
            break

    # Payoff logic
    # For Bernoulli distribution the payoff is quite straight forward
    # payoff = [agent.security_amount * real_outcome for agent in agents]

    print("Current market price is {}, while the real outcome is {}".\
    format(mk.current_market_price, real_outcome))


if __name__ == '__main__':
    main()

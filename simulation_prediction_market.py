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
        "-v", "--verbose", action="store_true", help="verbose showing simulation process"
    )
    parser.add_argument(
        "-n", "--agent_number", type=int, help="specify agent number"
    )
    parser.add_argument(
        "-i", "--max_iteration", type=int, help="specify maximum iteration"
    )
    args = parser.parse_args()
    return args


def import_data(path):
    """
    import real data from csv file
    :param: path: data path
    :return:
    """
    res = pd.read_csv(path)
    res = res.drop(columns=["Height", "Gender"])
    return list(res["Weight"])


def main():
    args = parse_command_line()
    agent_number = args.agent_number
    max_iteration = args.max_iteration
    data_path = "./Data/weight-height.csv"

    # real final result
    real_outcome = None
    num_observed_sample = 200

    # import data
    data = import_data(data_path)

    # initialize agents
    agents = []
    for i in range(agent_number):
        agent = BayesianAgent(update_size=num_observed_sample)
        agents.append(agent)

    # initialize market maker
    mk = MarketMaker()

    enter_times = np.random.poisson(7.5, max_iteration)     # lambda*max_iteration ~= size of dataset
    enter_times = list(np.cumsum(enter_times) + num_observed_sample)

    #################### for debug ####################
    # print("enter time: {}".format(enter_times))
    ###################################################

    # Pass in the data which the agents need to update their beliefs
    # The number of data points passed in to agent should be num_observed_sample
    for i in range(max_iteration):
        agent_idx = i % agent_number
        curr_agent = agents[agent_idx]
        enter_time = enter_times[i]
        observed_data = data[-num_observed_sample + enter_time :enter_time]
        
        #################### for debug ####################
        # if len(observed_data) < 2:
        #     print(i)
        #     print(observed_data)
        #     import ipdb; ipdb.set_trace()
        ###################################################
        curr_agent.update_param(observed_data, mk.num_trade, mk.current_market_price)
        delta = curr_agent.calculate_shares_to_buy(mk.current_market_price)
        curr_agent.update_security(delta)
        mk.update_param(delta)

    # Payoff logic
    payoff = [agent.security_amount * real_outcome for agent in agents]

    print("Current market price is {}, while the real outcome is {}".format(mk.current_market_price, real_outcome))
    print("The payoff for each agent is {}".format(payoff))
    

if __name__ == '__main__':
    main()

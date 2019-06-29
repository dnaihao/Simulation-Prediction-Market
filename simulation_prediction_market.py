#!/usr/bin/env python3
"""

Simulation Prediction Market Main Executable

"""

import argparse
from Agents.bayesian_agent import BayesianAgent
from Market_Maker.market_maker import MarketMaker


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="verbose showing simulation process"
    )
    pass


def main():
    args = parse_command_line()
    agent_number = args.agent_number
    max_iteration = args.max_iteration

    # initialize agents
    agents = []
    for i in range(agent_number):
        agent = BayesianAgent()
        agent.set_param(random = True)
        agents.append(agent)

    # initialize market maker
    maker = MarketMaker()
    maker.set_param(random = True)
    # TODO: simulate the whole trading process using while loop,
    #  either reach max iteration or market price converges


if __name__ == '__main__':
    main()
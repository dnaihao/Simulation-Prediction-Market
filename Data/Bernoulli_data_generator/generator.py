#!/usr/bin/env python3

"""

    The Heart Disease Death Rate: 1 in every 4 deaths

"""
import random
import csv

LENGTH = 10000
MIN = 0
MAX = 1
P = 0.25


def generate_death_list():
    """
    generate random list, and write it to a csv file
    """
    boundary = (MAX - MIN) * P
    deaths = []

    for i in range(LENGTH):
        choice = random.uniform(MIN, MAX)
        if choice > boundary:
            deaths.append(0)
        else:
            deaths.append(1)

    with open('../US_heart_disease_death.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for death in deaths:
            file_writer.writerow('{}'.format(death))


if __name__ == '__main__':
    generate_death_list()
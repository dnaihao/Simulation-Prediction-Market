#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
"""

Simulation Prediction Market Main Executable

"""

import argparse



def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="verbose showing simulation process"
    )


def main():
    args = parse_command_line()




if __name__ == '__main__':
    main()
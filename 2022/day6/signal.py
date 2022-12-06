import os
import sys
import numpy


def run_day6_part1():
    with open(os.path.join(sys.path[0], "day6\\input"), "r") as infile:
        signal = infile.readline()

        chars = [signal[0], signal[1], signal[2], signal[3]]
        for char_index in range(len(signal)):
            chars[char_index % 4] = signal[char_index]
            if len(numpy.unique(chars)) == 4:
                return char_index+1

    return -1


def run_day6_part2():
    return


import os
import sys
import numpy


def run_day6(num_distinct):
    with open(os.path.join(sys.path[0], "day6\\input"), "r") as infile:
        signal = infile.readline()

        chars = [signal[i] for i in range(num_distinct)]
        for char_index in range(num_distinct, len(signal)):
            chars[char_index % num_distinct] = signal[char_index]
            if len(numpy.unique(chars)) == num_distinct:
                return char_index+1

    return -1


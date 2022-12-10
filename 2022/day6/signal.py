import os
import sys
import numpy


def run(num_distinct):
    with open(os.path.join(sys.path[0], "input"), "r") as infile:
        signal = infile.readline()

        chars = [signal[i] for i in range(num_distinct)]
        for char_index in range(num_distinct, len(signal)):
            chars[char_index % num_distinct] = signal[char_index]
            if len(numpy.unique(chars)) == num_distinct:
                print(char_index+1)

    print("whoops")


if __name__ == '__main__':
    run(14)

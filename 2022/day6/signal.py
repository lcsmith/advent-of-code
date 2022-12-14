import numpy


def run(num_distinct):
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    signal = lines[0]

    chars = [signal[i] for i in range(num_distinct)]
    for char_index in range(num_distinct, len(signal)):
        chars[char_index % num_distinct] = signal[char_index]
        if len(numpy.unique(chars)) == num_distinct:
            print(char_index+1)


if __name__ == '__main__':
    run(14)

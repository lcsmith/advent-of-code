import math
from collections import defaultdict


def run(num_generations):
    stones = parse_input()

    stone_frequencies = defaultdict(int)
    for idx in range(len(stones)):
        stone_frequencies[stones[idx]] += 1

    for blinks in range(num_generations):
        stone_frequencies = blink_all_stone_frequencies(stone_frequencies)
    total_stones = 0
    for stone in stone_frequencies:
        total_stones += stone_frequencies[stone]

    print(total_stones)


def blink_all_stone_frequencies(stone_frequencies):
    new_frequencies = defaultdict(int)
    for stone in stone_frequencies:
        for new_stone in blink_single_stone(stone):
            new_frequencies[new_stone] += stone_frequencies[stone]
    return new_frequencies


def blink_single_stone(number):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if number == 0:
        return [1]

    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    # The left half of the digits are engraved on the new left stone,
    #   and the right half of the digits are engraved on the new right stone.
    # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    digits = int(math.log10(number)) + 1
    if digits % 2 == 0:
        half_digits_mask = pow(10, digits / 2)
        return [int(number / half_digits_mask), int(number % half_digits_mask)]

    # If none of the other rules apply, the stone is replaced by a new stone;
    #   the old stone's number multiplied by 2024 is engraved on the new stone.
    return [number * 2024]



def parse_input():
    with open('input') as infile:
        single_line = infile.read().strip()
    return [int(x) for x in single_line.split(" ")]


if __name__ == '__main__':
    run(25)
    run(75)
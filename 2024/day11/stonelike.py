import math


def run():
    stones = parse_input()

    # I know there's no way this will work in part 2, but let's do naive first.
    for blinks in range(25):
        stones = blink_all_stones(stones)
    print(len(stones))

def blink_all_stones(stones):
    blinked_list_of_lists = [blink_single_stone(stone)for stone in stones]
    return [item for sublist in blinked_list_of_lists for item in sublist]


def blink_single_stone(number):
    #If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if number == 0:
        return [1]

    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    digits = int(math.log10(number)) + 1
    if digits % 2 == 0:
        half_digits_mask = pow(10, digits / 2)
        return [int(number / half_digits_mask), int(number % half_digits_mask)]

    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    return [number * 2024]



def parse_input():
    with open('input') as infile:
        single_line = infile.read().strip()
    return [int(x) for x in single_line.split(" ")]


if __name__ == '__main__':
    run()
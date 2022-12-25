

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    numbers = []
    for line in lines:
        number = convert_from_snafu(line)
        numbers.append(number)

    to_snafu = sum(numbers)
    snafu = convert_to_snafu(to_snafu)
    print(to_snafu)
    print(snafu)
    print(convert_from_snafu(snafu))


def convert_from_snafu(snafu):
    number = 0
    place = 1
    for index in range(len(snafu)-1, -1, -1):
        match snafu[index]:
            case '-':
                digit = -1
            case '=':
                digit = -2
            case _:
                digit = int(snafu[index])
        number += place * digit
        place *= 5
    return number


def convert_to_snafu(number):
    if number == 0:
        return "0"
    snafu = ""
    place, first_digit = get_first_snafu_place(number)
    snafu += get_snafu_char(first_digit)
    midway_number = number - first_digit * pow(5, place)
    while midway_number != 0:
        place -= 1
        next_digit = get_subsequent_snafu_digit(midway_number, place)
        snafu += get_snafu_char(next_digit)
        midway_number = midway_number - next_digit * pow(5, place)
    while place > 0:
        snafu += '0'
        place -= 1
    return snafu


def get_subsequent_snafu_digit(midway_number, next_place):
    place, digit = get_first_snafu_place(abs(midway_number))
    if place < next_place:
        return 0
    if midway_number > 0:
        return digit
    return -1 * digit


def get_first_snafu_place(number):
    place = 0
    max_for_one = 1
    max_possible = 2
    while max_possible < number:
        place += 1
        max_possible += 2 * pow(5, place)
        max_for_one = max_possible - pow(5, place)
    if number > max_for_one:
        return place, 2
    return place, 1


def get_snafu_char(digit):
    match digit:
        case -1:
            return '-'
        case -2:
            return '='
        case _:
            return str(digit)


if __name__ == '__main__':
    run()

from ast import literal_eval
from functools import cmp_to_key


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    good_orders = []
    first_divider = [[2]]
    second_divider = [[6]]
    all_messages = [first_divider, second_divider]
    for pair_index in range(0, len(lines), 3):
        first = literal_eval(lines[pair_index])
        second = literal_eval(lines[pair_index+1])
        if are_ordered(first, second):
            good_orders.append(pair_index/3 + 1)

        all_messages.append(first)
        all_messages.append(second)
    print(sum(good_orders))
    all_messages.sort(key=cmp_to_key(ordering_comparator))
    print((all_messages.index(first_divider)+1) * (all_messages.index(second_divider)+1))


def ordering_comparator(first, second):
    if are_ordered(first, second):
        return -1
    else:
        return 1


def are_ordered(first, second):
    if isinstance(first, int) and isinstance(second, int):
        if first == second:
            return None
        return first < second

    if isinstance(first, list) and isinstance(second, list):
        for index in range(len(first)):
            if index >= len(second):
                return False
            ordering = are_ordered(first[index], second[index])
            if ordering is not None:
                return ordering
        if len(first) < len(second):
            return True

    if isinstance(first, int) and isinstance(second, list):
        return are_ordered([first], second)
    if isinstance(first, list) and isinstance(second, int):
        return are_ordered(first, [second])


if __name__ == '__main__':
    run()

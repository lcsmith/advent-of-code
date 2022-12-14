from ast import literal_eval


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    good_orders = []
    for pair_index in range(0, len(lines), 3):
        first = literal_eval(lines[pair_index])
        second = literal_eval(lines[pair_index+1])
        if are_ordered(first, second):
            good_orders.append(pair_index/3 + 1)
    print(sum(good_orders))


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

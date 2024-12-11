from collections import defaultdict
from functools import cmp_to_key


def run():
    order_rules, updates = parse_input()

    valid_middle_sums = 0
    invalid_middle_sums = 0
    for update in updates:
        is_valid = True
        for first_idx in range(0, len(update)):
            for second_idx in range(first_idx+1, len(update)):
                if update[first_idx] in order_rules[update[second_idx]]:
                    is_valid = False

        if is_valid:
            middle_idx = int(len(update) / 2)
            valid_middle_sums += int(update[middle_idx])
        else:
            sorted_update = sorted(update, key=cmp_to_key(lambda first, second: 1 if first in order_rules[second] else -1))
            middle_idx = int(len(sorted_update) / 2)
            invalid_middle_sums += int(sorted_update[middle_idx])

    print(valid_middle_sums)
    print(invalid_middle_sums)

def parse_input():
    order_rules = defaultdict(set)
    updates = []
    is_parsing_orders = True
    with open('input') as infile:
        for line in infile:
            stripped_line = line.strip()
            if stripped_line == "":
                is_parsing_orders = False
            elif is_parsing_orders:
                ordering = stripped_line.split("|")
                order_rules[ordering[0]].add(ordering[1])
            else:
                updates.append([x for x in stripped_line.split(",")])

    return order_rules, updates


if __name__ == '__main__':
    run()

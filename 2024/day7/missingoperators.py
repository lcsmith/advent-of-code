import itertools
from collections import namedtuple


OperationLine = namedtuple('OperationLine', ['expected_result', 'operands'])

def run(include_concat):
    parsed_lines = parse_input()

    possible_operators = [lambda x,y: x+y, lambda x,y: x*y]
    if include_concat:
        possible_operators.append(lambda x,y: int(f'{x}{y}'))

    total_sum = 0
    for (expected_result, operands) in parsed_lines:
        if is_possible(expected_result, operands, possible_operators):
            total_sum += expected_result

    print(total_sum)


def is_possible(expected_result, operands, possible_operators):
    results = [int(operands[0])]
    for operand_idx in range (1, len(operands)):
        results = [op(val, int(operands[operand_idx])) for (val, op) in itertools.product(results, possible_operators)]
        results = [x for x in results if x <= expected_result]
    return any([x == expected_result for x in results])


def parse_input():
    with open('input') as infile:
        lines = [line.strip().split(' ') for line in infile]

    return [OperationLine(int(line[0].strip(':')), line[1:]) for line in lines]


if __name__ == '__main__':
    run(False)
    run(True)

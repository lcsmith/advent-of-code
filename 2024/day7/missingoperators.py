import itertools
import operator
from collections import namedtuple

OperationLine = namedtuple('OperationLine', ['expected_result', 'operands'])

def run():
    parsed_lines = parse_input()

    total_sum = 0
    for (expected_result, operands) in parsed_lines:
        if is_possible(expected_result, operands):
            total_sum += expected_result

    print(total_sum)

def is_possible(expected_result, operands):
    possible_operators = [operator.add, operator.mul]

    results = [int(operands[0])]
    for operand_idx in range (1, len(operands)):
        results = [op(val, int(operands[operand_idx])) for (val, op) in itertools.product(results, possible_operators)]
    return any([x == expected_result for x in results])

# Implemented before I re-read the part about ignoring order of operations...
def is_possible_respect_oo(expected_result, operands):
    possible_operators = ['+', '*']

    expressions = [operands[0]]
    for operand_idx in range (1, len(operands)):
        expressions = [exp + op + operands[operand_idx] for (exp, op) in itertools.product(expressions, possible_operators)]
    return any([eval(x) == expected_result for x in expressions])

def parse_input():
    with open('input') as infile:
        lines = [line.strip().split(' ') for line in infile]

    return [OperationLine(int(line[0].strip(':')), line[1:]) for line in lines]

if __name__ == '__main__':
    run()

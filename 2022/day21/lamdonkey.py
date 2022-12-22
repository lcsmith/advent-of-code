import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
    '==': operator.eq,
}


def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    monkeys = {}
    for line in lines:
        instructions = line.split()
        monkey = instructions[0][:-1]
        if monkey == "root":
            monkeys[monkey] = lambda first_operand = instructions[1], op_string = instructions[2], second_operand = instructions[3]:\
                print(str(monkeys[first_operand]()) + "\n" + str(monkeys[second_operand]()))
        elif monkey == "humn":
            monkeys[monkey] = lambda: 3441198826073
        elif len(instructions) == 2:
            value = int(instructions[1])
            monkeys[monkey] = lambda x=value: x
        else:
            monkeys[monkey] = \
                lambda first_operand = instructions[1], op_string = instructions[2], second_operand = instructions[3]:\
                eval_lambdas(monkeys[first_operand], op_string, monkeys[second_operand])
    print(monkeys["root"]())


# shoutout to stack exchange, thanks kings
def eval_lambdas(lambda1, oper, lambda2):
    return ops[oper](lambda1(), lambda2())


if __name__ == '__main__':
    run()

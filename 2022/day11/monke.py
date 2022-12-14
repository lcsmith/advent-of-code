import math


def run():
    is_part2 = True
    monkeys = parse_monkeys()

    worry_modulation = math.prod(map(lambda m: m.test_divisor, monkeys.values()))
    for game_round in range(10000):
        for monkey in monkeys.values():
            for item in monkey.items:
                item = monkey.operation(item)
                if is_part2:
                    item = item % worry_modulation
                else:
                    item = math.floor(item / 3)
                if (item % monkey.test_divisor) == 0:
                    monkeys[monkey.true_throw].items.append(item)
                else:
                    monkeys[monkey.false_throw].items.append(item)
            monkey.inspections += len(monkey.items)
            monkey.items.clear()

    monkey_list = list(monkeys.values())
    monkey_list.sort(key=lambda m: m.inspections, reverse=True)
    print(monkey_list[0].inspections * monkey_list[1].inspections)


def parse_monkeys():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    monkeys = {}
    current_monkey = None
    for line in lines:
        words = line.split()
        if not words:
            continue
        if words[0] == "Monkey":
            current_monkey = Monkey()
            monkeys[int(words[1][0])] = current_monkey
        elif words[0] == "Starting":
            for item_it in range(2, len(words)):
                current_monkey.items.append(int(words[item_it].replace(",", "")))
        elif words[0] == "Operation:":
            if line == "Operation: new = old * old":
                current_monkey.operation = lambda x: x * x
            elif words[4] == "*":
                current_monkey.operation = lambda x, operand = int(words[5]): x * operand
            elif words[4] == "+":
                current_monkey.operation = lambda x, operand = int(words[5]): x + operand
        elif words[0] == "Test:":
            current_monkey.test_divisor = int(words[3])
        elif words[:2] == ["If", "true:"]:
            current_monkey.true_throw = int(words[5])
        elif words[:2] == ["If", "false:"]:
            current_monkey.false_throw = int(words[5])
    return monkeys


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.test_divisor = None
        self.true_throw = None
        self.false_throw = None
        self.inspections = 0


if __name__ == '__main__':
    run()

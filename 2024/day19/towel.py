

def run():
    towels, patterns = parse_input()

    print(sum([1 for pattern in patterns if does_pattern_match(towels, pattern)]))


def does_pattern_match(towels, pattern):
    next_states = {pattern}
    while any(next_states):
        current_state = next_states.pop()
        for towel in towels:
            if current_state.startswith(towel):
                consumed_state = current_state[len(towel):]
                if consumed_state == "":
                    return True
                next_states.add(consumed_state)
    return False



def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return towels, patterns


if __name__ == '__main__':
    run()
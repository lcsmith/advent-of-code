from collections import OrderedDict


def run():
    towels, patterns = parse_input()

    pattern_match_counts = [get_pattern_match_count(towels, pattern) for pattern in patterns]
    print(sum([1 for x in pattern_match_counts if x > 0]))
    print(sum(pattern_match_counts))


def get_pattern_match_count(towels, pattern):
    next_states = OrderedDict()
    next_states[pattern] = 1
    match_count = 0
    while any(next_states):
        (current_state, num_paths_in) = next_states.popitem(last = False)
        for towel in towels:
            if current_state.startswith(towel):
                consumed_state = current_state[len(towel):]
                if consumed_state == "":
                    match_count += num_paths_in
                else:
                    if consumed_state not in next_states:
                        next_states[consumed_state] = num_paths_in
                    else:
                        next_states[consumed_state] += num_paths_in
    return match_count


def parse_input():
    with open('input') as infile:
        lines = [line.strip() for line in infile]
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return towels, patterns


if __name__ == '__main__':
    run()
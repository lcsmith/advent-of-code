

def run():
    monkey_seeds = parse_input()
    print(monkey_seeds)

    num_generations = 2000
    for x in range(num_generations):
        monkey_seeds = [evolve_secret(secret) for secret in monkey_seeds]
    print(sum(monkey_seeds))


def evolve_secret(secret_number):
    magic_mod = 1 << 24
    first_shift = secret_number << 6
    secret_number = (first_shift ^ secret_number) % magic_mod

    second_shift = secret_number >> 5
    secret_number = (second_shift ^ secret_number) % magic_mod

    third_shift = secret_number << 11
    secret_number = (third_shift ^ secret_number) % magic_mod

    return secret_number


def parse_input():
    with open('input') as infile:
        return [int(line.strip()) for line in infile]


if __name__ == '__main__':
    run()
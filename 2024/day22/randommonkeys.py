from collections import defaultdict


def run():
    monkey_seeds = parse_input()

    num_generations = 2000
    price_history = [monkey_seeds]
    for x in range(num_generations):
        monkey_seeds = [evolve_secret(secret) for secret in monkey_seeds]
        price_history.append([secret % 10 for secret in monkey_seeds])

    print(sum(monkey_seeds))

    sequence_values = defaultdict(int)
    for monkey_idx in range(len(monkey_seeds)):
        seen_sequences = set()
        for price_idx in range(4, num_generations+1):
            price = price_history[price_idx][monkey_idx]
            sequence = (
                    price_history[price_idx-3][monkey_idx] - price_history[price_idx-4][monkey_idx],
                    price_history[price_idx-2][monkey_idx] - price_history[price_idx-3][monkey_idx],
                    price_history[price_idx-1][monkey_idx] - price_history[price_idx-2][monkey_idx],
                    price_history[price_idx-0][monkey_idx] - price_history[price_idx-1][monkey_idx])
            if sequence not in seen_sequences:
                sequence_values[sequence] += price
                seen_sequences.add(sequence)

    print(max([sequence_values[key] for key in sequence_values]))


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
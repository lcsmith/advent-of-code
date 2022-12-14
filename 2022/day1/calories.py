

def run(num_elves):
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    best_calories = [0]*num_elves
    current_calories = 0

    for line in lines:
        if not line:
            if current_calories > best_calories[0]:
                best_calories[0] = current_calories
                best_calories.sort()
            current_calories = 0
        else:
            current_calories += int(line)

    print(sum(best_calories))


if __name__ == '__main__':
    run(3)

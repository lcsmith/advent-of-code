

def run_part1():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    total_score = 0
    for line in lines:
        plan = line.split()
        opponent = convert_opponent(plan[0])
        thrown = convert_thrown(plan[1])
        total_score += convert_thrown(plan[1])
        total_score += score_outcome(opponent, thrown)

    print(total_score)


def run_part2():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    total_score = 0
    for line in lines:
        plan = line.split()
        opponent = convert_opponent(plan[0])
        thrown = convert_expectation(opponent, plan[1])
        total_score += thrown
        total_score += score_outcome(opponent, thrown)

    print(total_score)


def convert_thrown(thrown):
    match thrown:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


def convert_expectation(opponent, plan):
    match plan:
        case "X":
            return ((opponent - 2) % 3) + 1
        case "Y":
            return opponent
        case "Z":
            return (opponent % 3) + 1


def convert_opponent(opponent):
    match opponent:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3


def score_outcome(opponent, thrown):
    if thrown == opponent:
        return 3
    if thrown == (opponent % 3) + 1:
        return 6
    return 0


if __name__ == '__main__':
    run_part2()

from day1.elf_calories import run_day1
from day2.rps import run_day2_part2, run_day2_part1
from day3.rucksack import run_day3_part1, run_day3_part2


def run(day, part):
    match day, part:
        case 1, 1:
            return run_day1(1)
        case 1, 2:
            return run_day1(3)
        case 2, 1:
            return run_day2_part1()
        case 2, 2:
            return run_day2_part2()
        case 3, 1:
            return run_day3_part1()
        case 3, 2:
            return run_day3_part2()


if __name__ == '__main__':
    print(run(3, 2))

from day1.elf_calories import run_day1
from day2.rps import run_day2_part2, run_day2_part1


def run(day, part):
    match day, part:
        case 1, 1:
            run_day1(1)
        case 1, 2:
            run_day1(3)
        case 2, 1:
            run_day2_part1()
        case 2, 2:
            run_day2_part2()


if __name__ == '__main__':
    run(2, 2)



def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    cycle = 1
    register = 1
    registers = []
    strengths = []
    for line in lines:
        strengths.append(cycle*register)
        registers.append(register)
        cycle += 1
        if line != "noop":
            strengths.append(cycle*register)
            registers.append(register)
            cycle += 1
            instruction = line.split()
            register += int(instruction[1])

    print(strengths[19]+strengths[59]+strengths[99]+strengths[139]+strengths[179]+strengths[219])

    raster = ""
    for cycle in range(len(registers)):
        if registers[cycle]-1 <= (cycle % 40) <= registers[cycle]+1:
            raster = raster + "#"
        else:
            raster = raster + "."
        if cycle % 40 == 39:
            raster = raster + "\n"
    print(raster)


if __name__ == '__main__':
    run()

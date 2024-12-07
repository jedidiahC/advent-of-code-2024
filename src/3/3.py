import re

def solve_part_one():
    sum = 0
    with open("3.in", "r") as input_file:
        for line in input_file:
            matches = re.findall("mul\(([0-9]+,[0-9]+)\)", line)
            for match in matches:
                [a, b] = match.split(",")
                sum += int(a) * int(b)

    print(sum)

def solve_part_two():
    sum = 0
    with open("3.in", "r") as input_file:
        input = ""
        for line in input_file:
            input += line

        input = input.replace('\n', '')
        dos = "".join(re.split("don't\(\).*?(?=do\(\)|$)", input))
        muls = re.findall("mul\(([0-9]+,[0-9]+)\)", dos)
        for mul in muls:
            [a, b] = mul.split(",")
            sum += int(a) * int(b)

    print(sum)

solve_part_one()
solve_part_two()


def solve(calculators):
    with open("7.in", "r") as input_file:
        sum = 0
        for line in input_file:
            [value, numbers_str] = line.split(": ")
            value = int(value)
            numbers = list(map(int, numbers_str.split(" ")))
            def evaluate(curr, operands):
                if len(operands) == 0:
                    return curr == value

                for calculate in calculators:
                    if evaluate(calculate(curr, operands[0]), operands[1:]):
                        return True

                return False

            if evaluate(numbers[0], numbers[1:]):
                sum += int(value)

        print(sum)

calculators = [
    lambda a, b: a + b,
    lambda a, b: a * b,
    lambda a, b: int(f"{a}{b}")
]

solve(calculators[:-1])
solve(calculators)

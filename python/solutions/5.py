
def solve_part_one():
    with open("5.in") as input_file:
        rules = {}
        for line in input_file:
            if line == '\n':
                break

            [before, after] = list(map(int,line.split("|")))
            if before not in rules:
                rules[before] = { after }
            else:
                rules[before].add(after)

        res = 0
        incorrect_updates = []
        for update in input_file:
            values = list(map(int, update.split(",")))

            encountered = set()
            is_correct = True
            for value in values:
                encountered.add(value)
                if value not in rules:
                    continue

                if len(rules[value].intersection(encountered)):
                    incorrect_updates.append(values)
                    is_correct = False
                    break

            if is_correct:
                res += values[int(len(values) / 2)]

        print(res)
        return (rules, incorrect_updates)


def solve_part_two(rules, incorrect_updates):
    res = 0
    for values in incorrect_updates:
        encountered = set()

        index = 0
        while index < len(values):
            value = values[index]
            encountered.add(value)

            if value not in rules:
                index += 1
                continue

            while len(encountered.intersection(rules[value])) > 0:
                values[index], values[index - 1] = values[index - 1], values[index]
                encountered.remove(values[index])
                index -= 1

            index += 1

        res += values[int(len(values) / 2)]

    print(res)

(rules, incorrect_updates) = solve_part_one()
solve_part_two(rules, incorrect_updates)

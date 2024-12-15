import re


def get_tokens_required(button_a, button_b, prize):
    a_cost, b_cost = 3, 1

    [a_x, a_y] = button_a
    [b_x, b_y] = button_b

    augmented_matrix = [
        [a_x, b_x, prize[0]],
        [a_y, b_y, prize[1]],
    ]

    augmented_matrix[1][0] = 0
    augmented_matrix[1][1] = b_y - (b_x / a_x) * a_y
    augmented_matrix[1][2] = prize[1] - (prize[0] / a_x) * a_y

    augmented_matrix[1][2] /= augmented_matrix[1][1]
    augmented_matrix[1][1] = 1

    augmented_matrix[0][2] -= augmented_matrix[1][2] * augmented_matrix[0][1]
    augmented_matrix[0][1] = 0

    augmented_matrix[0][2] /= augmented_matrix[0][0]
    augmented_matrix[0][0] = 1

    a = round(augmented_matrix[0][2])
    b = round(augmented_matrix[1][2])

    if abs(augmented_matrix[0][2] - a) > 0.01 or abs(augmented_matrix[1][2] - b) > 0.01:
        return 0

    return a * a_cost + b * b_cost


def solve():

    with open("../input/13.in", "r", encoding="utf-8") as input_file:
        regex_txt = r'\d+'

        machine_input = input_file.readlines()
        index = 0
        part_one = 0
        part_two = 0
        while index < len(machine_input):
            button_a = list(map(int, re.findall(
                regex_txt, machine_input[index])))
            button_b = list(map(int, re.findall(
                regex_txt, machine_input[index + 1])))
            prize = list(map(int, re.findall(
                regex_txt, machine_input[index + 2])))
            part_one += get_tokens_required(button_a, button_b, prize)
            correction = 10000000000000
            part_two += get_tokens_required(
                button_a, button_b, [prize[0] + correction, prize[1] + correction])

            index += 4

        print(part_one)
        print(part_two)


solve()

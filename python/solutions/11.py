def get_stones(stone, blinks, memo):
    if blinks == 0:
        return 1

    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    count = 0
    if stone == 0: # Zero.
        count += get_stones(1, blinks - 1, memo)
    elif len(str(stone)) % 2 == 0: # Even digits.
        stone_str = str(stone)
        stone_one = int(stone_str[:int(len(stone_str) / 2)])
        stone_two = int(stone_str[int(len(stone_str) / 2) :])

        count += get_stones(stone_one, blinks - 1, memo)
        count += get_stones(stone_two, blinks - 1, memo)
    else: # Odd digits not 0.
        count += get_stones(stone * 2024, blinks - 1, memo)

    memo[(stone, blinks)] = count
    return count

def solve(blinks):
    with open("../input/11.in", "r") as input_file:
        stones = list(map(int, input_file.read().split(" ")))

    count = 0
    memo = {}
    for stone in stones:
        count += get_stones(stone, blinks, memo)
    print(count)

solve(25)
solve(75)

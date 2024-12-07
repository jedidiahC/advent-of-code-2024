def isXmas(grid, y, x):
    count = 0
    for dX in range(-1, 2):
        for dY in range(-1, 2):
            if dX == 0 and dY == 0:
                continue

            search = "XMAS"
            while len(search) > 0:
                nX = x + dX * (4 - len(search))
                nY = y + dY * (4 - len(search))

                if (nX < 0 or nX >= len(grid[0])):
                    break

                if (nY < 0 or nY >= len(grid)):
                    break

                if (grid[nY][nX] != search[0]):
                    break

                search = search[1:]

            if (len(search) == 0):
                count += 1

    return count

def is_x_mas(grid, y, x):
    if (x <= 0 or x >= len(grid[0]) - 1):
        return False

    if (y <= 0 or y >= len(grid) - 1):
        return False

    return set([grid[y - 1][x - 1], grid[y + 1][x + 1]]) == set(["M", "S"]) and set([grid[y + 1][x - 1], grid[y - 1][x + 1]]) == set(["M", "S"])


def solve_part_one():
    with open("4.in", "r") as input_file:
        grid = []
        for row in input_file:
            grid.append([c for c in row])

        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'X':
                    res += isXmas(grid, y, x)
        print(res)

def solve_part_two():
    with open("4.in", "r") as input_file:
        grid = []
        for row in input_file:
            grid.append([c for c in row])

        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'A':
                    res += 1 if is_x_mas(grid, y, x) else 0
        print(res)

solve_part_one()
solve_part_two()

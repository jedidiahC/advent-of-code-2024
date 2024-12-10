def get_neighbors(pos, grid, target_height):
    neighbor_positions = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    neighbors = []
    for neighbour_pos in neighbor_positions:
        (y, x) = neighbour_pos
        is_next_pos = (y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]) and int(grid[y][x]) == target_height)
        if is_next_pos:
            neighbors.append(neighbour_pos)

    return neighbors

def get_score_and_ratings(trailhead, grid):
    nines_set = set()
    score = traverse(trailhead, 0, nines_set, grid)
    return len(nines_set), score

def traverse(curr_pos, curr_height, nines_set, grid):
    if curr_height == 9:
        nines_set.add(curr_pos)
        return 1

    neighbors = get_neighbors(curr_pos, grid, curr_height + 1)
    paths = 0
    for neighbor in neighbors:
        paths += traverse(neighbor, curr_height + 1, nines_set, grid)

    return paths

def solve():
    with open("../input/10.in", "r") as input_file:
        grid = [row[:-1] for row in input_file]

    score = 0
    ratings = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '0':
                (curr_score, curr_ratings) = get_score_and_ratings((y, x), grid)
                score += curr_score
                ratings += curr_ratings

    print(score, ratings)

solve()

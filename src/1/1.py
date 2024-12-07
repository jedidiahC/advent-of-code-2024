
def solve_part_one():
    with open("1.in", "r") as day_one_file:
        left, right = [], []
        for line in day_one_file:
            a, b = line.split("   ")[:2]
            a, b = int(a), int(b)
            left.append(a)
            right.append(b)

        left.sort()
        right.sort()

        dist = 0
        for idx in range(len(left)):
            dist += abs(left[idx] - right[idx])

        print(dist)

def solve_part_two():
    occurrences = {}

    with open("1.in", "r") as day_one_file:
        left, right = [], []
        for line in day_one_file:
            a, b = line.split("   ")[:2]
            a, b = int(a), int(b)
            left.append(a)
            right.append(b)

        occurrences = {}
        for x in right:
            if x not in occurrences:
                occurrences[x] = 0

            occurrences[x] += 1

        similarity_score = 0
        for x in left:
            if x not in occurrences:
                continue

            similarity_score += x * occurrences[x]

        print(similarity_score)

solve_part_one()
solve_part_two()

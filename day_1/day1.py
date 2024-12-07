def read() -> (list[int], list[int]):
    with open("input.txt", 'r') as file:
        data: list[str] = file.readlines()

    left_list: list[int] = []
    right_list: list[int] = []
    for line in data:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list

### PART I ###
def part1() -> int:
    left_list, right_list = read()
    left_list.sort()
    right_list.sort()

    return sum(abs(left - right) for left, right in zip(left_list, right_list))

### PART II ###
def part2() -> int:
    left_list, right_list = read()
    counts: dict[int, int] = {}

    for num in right_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return sum(num * counts[num] for num in left_list if num in counts)

if __name__ == "__main__":
    print(part1())
    print(part2())
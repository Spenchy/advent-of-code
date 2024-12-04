AUTHORIZED_DIFF = {1, 2, 3}

def read_input():
    with open("input_02.txt", mode="r") as file:
        for line in file:
            yield [int(i) for i in line.split()]

def compute_valid_levels(levels):
    list_order = levels[0] - levels[1]

    if list_order < 0:
        for i in range(len(levels) - 1):
            diff = levels[i+1] - levels[i]
            if diff not in AUTHORIZED_DIFF:
                return 0
    elif list_order > 0:
        for i in range(len(levels) - 1):
            diff = levels[i] - levels[i+1]
            if diff not in AUTHORIZED_DIFF:
                return 0
    else:
        return 0

    return 1

def part_two():
    pass

if __name__ == "__main__":
    result = 0
    for input in read_input():
        result += compute_valid_levels(input)

    print(result)

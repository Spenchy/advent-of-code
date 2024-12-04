import re

def read_input():
    with open("input_03.txt", mode="r") as file:
        for line in file:
            yield line


def part_one(instructions):
    found = re.findall(r"mul\((\d+),(\d+)\)", instructions)

    total = 0
    for i in found:
        total += int(i[0]) * int(i[1])

    return total

if __name__ == "__main__":
    result = 0
    for line in read_input():
        result += part_one(line)

    print(result)

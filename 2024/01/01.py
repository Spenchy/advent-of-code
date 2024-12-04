from collections import defaultdict


def part_one(list_1, list_2):
    # Sort lists
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    # Compute solution
    result = 0
    for item_1, item_2 in zip(sorted_list_1, sorted_list_2):
        result += abs(item_1 - item_2)

    print(result)

def part_two(list_1, list_2):
    # Create dict containing how much each number has been seen
    num = defaultdict(int)
    for i in list_1:
        num[i] += 1

    # Compute similarity score
    result = 0
    for i in list_2:
        result += i * num[i]

    print(result)

if __name__ == "__main__":
    # Reading lists from input
    # NB: could be improved by sorting while inserting
    list_1 = []
    list_2 = []
    with open("input_01.txt", mode="r") as file:
        for line in file:
            item_1, item_2 = line.split()
            list_1.append(int(item_1))
            list_2.append(int(item_2))

    # part_one(list_1, list_2)
    part_two(list_1, list_2)

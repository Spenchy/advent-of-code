from math import floor

def part_one(rotations):
    result = 0
    point = 50
    for rotation in rotations:
        if rotation[0] == "L":
            point = (point - int(rotation[1:])) % 100
        elif rotation[0] == "R":
            point = (point + int(rotation[1:])) % 100

        if point == 0:
            result += 1

    print(result)
    

def part_two(rotations):
    result = 0
    point = 50
    for rotation in rotations:
        print(rotation)
        num_zero = 0
        if rotation[0] == "L":
            ratio = (point - int(rotation[1:])) / 100
            if ratio <= 0:
                num_zero = floor(abs(ratio))
                if point != 0:
                    num_zero += 1
            point = (point - int(rotation[1:])) % 100

            print(ratio)
        elif rotation[0] == "R":
            num_zero = floor((point + int(rotation[1:])) / 100)
            point = (point + int(rotation[1:])) % 100

        print(point)
        print(num_zero)
        result += num_zero

    print(result)

if __name__ == "__main__":
    # Reading rotations from input
    rotations = []
    with open("input_01.txt", mode="r") as file:
        for line in file:
            rotations.append(line.strip("\n"))

    # part_one(rotations)
    part_two(rotations)

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
    
    pass

if __name__ == "__main__":
    # Reading lists from input
    rotations = []
    with open("input_01.txt", mode="r") as file:
        for line in file:
            rotations.append(line.strip("\n"))

    part_one(rotations)
    # part_two(rotations)

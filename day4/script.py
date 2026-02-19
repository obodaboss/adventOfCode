file = open("./day4/input.txt")

# Loop each line, construct a big 2d array of the map
grid = [] # 1st index is down (line), 2nd is along
for line in file:
    line = line.strip()
    # print(line)
    array = []

    for elem in line:
        array.append(elem)

    grid.append(array)

# Answer to the puzzle
movable_rolls = 0

# Loop each grid element, determine if there are < 4 neighbour rolls for each roll
for x in range(len(grid)):
    for y in range(len(grid[0])):
        elem = grid[x][y]

        # Only concerned with rolls
        if elem != "@":
            continue

        # Count how many rolls are nearby this one
        nearby_rolls = 0
        for i in range (-1, 2):
            for j in range (-1, 2):
                if i == 0 and j == 0:
                    continue
                x2 = x + i
                y2 = y + j
                if x2 < 0 or x2 >= len(grid):
                    continue
                if y2 < 0 or y2 >= len(grid[0]):
                    continue

                if grid[x2][y2] == "@":
                    nearby_rolls += 1

        if nearby_rolls < 4:
            movable_rolls += 1


print("Movable rolls: " + str(movable_rolls))
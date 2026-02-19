file = open("./day7/input.txt")

# Create a 2d array grid to represent the puzzle
grid = []
for line in file:
    line = line.strip()
    # print(line)

    line_array = []
    for char in line:
        line_array.append(char)
    grid.append(line_array)

split_count = 0

# Go down the grid and fill in where the beam goes
for row in range(len(grid)):

    # Skip top row, we don't do any processing here
    if row == 0:
        continue
    for col in range(len(grid[0])):
        tile = grid[row][col]
        tile_above = grid[row-1][col] # Don't process top row so this is always safe

        # Create initial laser
        if tile_above == "S":
            grid[row][col] = "|"

        # Skip further processing if tile above is not laser
        if tile_above != "|":
            continue
        # From here on the tile above is a laser

        # If tile is empty, make it laser
        if tile == ".":
            grid[row][col] = "|"

        # If tile is splitter, split the laser
        if tile == "^":
            if col-1 >= 0:
                grid[row][col-1] = "|"
            if col+1 < len(grid):
                grid[row][col+1] = "|"
            split_count += 1

    # If char above is a laser do:
    # A) if char is dot, turn to laser
    # B) if char is splitter, make both left and right lasers (and increment split count)


print("----------------------------")

# for row in grid:
#     for char in row:
#         print(char, end="")
#     print("")


print("Split count: " + str(split_count))
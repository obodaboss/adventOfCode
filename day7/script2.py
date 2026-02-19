def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end="-")
        print("")


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
            grid[row][col] = "1"

        # Skip further processing if tile above is not laser
        if not tile_above.isnumeric():
            continue
        # From here on the tile above is a laser

        # If tile is empty, make it laser
        if tile == ".":
            grid[row][col] = tile_above
        
        if tile.isnumeric():
            value = int(tile)
            grid[row][col] = str(value+int(tile_above))

        # If tile is splitter, split the laser
        if tile == "^":
            if grid[row][col-1] == ".":
                grid[row][col-1] = tile_above
            elif grid[row][col-1].isnumeric():
                value = int(grid[row][col-1])
                grid[row][col-1] = str(value+int(tile_above))

            if grid[row][col+1] == ".":
                grid[row][col+1] = tile_above
            elif grid[row][col+1].isnumeric():
                value = int(grid[row][col+1])
                grid[row][col+1] = str(value+int(tile_above))


# print_grid(grid)


# Sum results of bottom row
total = 0
for value in grid[-1]:
    if str(value).isnumeric():
        total += int(value)
print("Total: " + str(total))

# print("Split count: " + str(split_count))
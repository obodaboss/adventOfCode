def print_grid(grid):
    for row in grid:
        for char in row:
            print(char, end="")
        print("")

def process(grid):

    # Go down the grid and fill in where the beam goes
    for row in range(1, len(grid)): # (always skip first row)

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
                # Deep copy grid
                grid_1 = deepcopy(grid, row)
                grid_1[0][col-1] = "|" # Stripped used rows, so row index is always 0

                # print("--- Created Grid 1 ---")
                # print_grid(grid_1)

                split_count_1 = process(grid_1)

                # grid_2 = deepcopy(grid, row)
                grid_2 = grid[row:]
                grid_2[0][col+1] = "|"
                split_count_2 = process(grid_2)

                return split_count_1 + split_count_2
    return 1


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

result = process(grid)

print("----------------------------")

# for row in grid:
#     for char in row:
#         print(char, end="")
#     print("")


print("Result: " + str(result))
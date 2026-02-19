file = open("./day6/input.txt")

grid = []
for line in file:
    line = line.strip()
    print(line)

    grid.append(line.split())

print(grid)

# Loop col then row to sum numbers
total = 0
for col in range(len(grid[0])):
    operation = grid[-1][col]
    sub_total = 0
    if operation == "*": # Adjust sub-total for multiplying
        sub_total = 1
    for row in range(len(grid)-1): # -1 to skip last row with operators
        if operation == "+":
            sub_total += int(grid[row][col])
        elif operation == "*":
            sub_total *= int(grid[row][col])

    print("Subtotal: " + str(sub_total))
    total += sub_total

print("Total: " + str(total))
        
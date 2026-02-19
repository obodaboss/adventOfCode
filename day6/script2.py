file = open("./day6/input.txt")

grid = []
for line in file:
    line = line.replace("\n","")
    print(line)

    line_array = []
    for char in line:
        line_array.append(char)
    
    line_array.append(" ") # Add an extra column of whitespace at the end
    grid.append(line_array)


# print(grid)
# print("Num lines: " + str(len(grid)))
# for line in grid:
#     print("Num cols: " + str(len(line)))


"""
Work down each column 1 at a time:
 Construct a number from the digits read
 Record operator at the bottom of first line
 Keep a subtotal by applying operator to read values
 (subtotal initial value depends on operator, 0 or 1)
 When see col that's entirely whitespace (or last col) add
  subtotal to total
"""

# Track answer to puzzle
total = 0
operator = ""
sub_total = 0

# Loop each colun (2d array is perfect square)
for col in range(len(grid[0])):
    current_num = ""
    # Go down each character in the row top to bottom
    for row in range(len(grid)):
        tile = grid[row][col]
        if tile == "*":
            operator = tile
            sub_total = 1
        elif tile == "+":
            operator = tile
            sub_total = 0
        elif tile != " ":
            current_num += tile

    # If line was empty add subtotal to total, otherwise add current_num to subtotal
    if current_num:
        current_num = int(current_num)
        if operator == "*":
            sub_total *= current_num
        elif operator == "+":
            sub_total += current_num
        else:
            raise Exception("INVALD OPERATOR")
        
    else: # Reset if we reached a blank line
        print("Adding to total: " + str(sub_total))
        total += sub_total
        sub_total = 0
        operator = ""

print("Total: " + str(total))






# # Loop col then row to sum numbers
# total = 0
# for col in range(len(grid[0])):
#     operation = grid[-1][col]
#     sub_total = 0
#     if operation == "*": # Adjust sub-total for multiplying
#         sub_total = 1
#     for row in range(len(grid)-1): # -1 to skip last row with operators
#         if operation == "+":
#             sub_total += int(grid[row][col])
#         elif operation == "*":
#             sub_total *= int(grid[row][col])

#     print("Subtotal: " + str(sub_total))
#     total += sub_total

# print("Total: " + str(total))
        
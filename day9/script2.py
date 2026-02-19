from multiprocessing import Pool

coordinates_map = {}
def is_red(coordinates, x, y):
    global coordinates_map
    if x not in coordinates_map:
        return False
    if y not in coordinates_map[x]:
        return False
    return True

last_north = 0
last_south = 0
last_east = 0
last_west = 0
def is_green(coordinates, x, y):
    # To be green must either lie on a line, or have a line to N,S,E & W
    has_north = False
    has_south = False
    has_east = False
    has_west = False

    global last_north, last_south, last_east, last_west
    # Loop cached lines
    for i in (last_north, last_south, last_east, last_west):
        coord1 = coordinates[(i-1)%len(coordinates)] # First loop will be back of list & index 0
        coord2 = coordinates[i]

        # If they share X dimension - check East and West
        if coord1[0] == coord2[0]:
            x_coord = coord1[0] # (Same for both)
            big_y = max(coord1[1], coord2[1])
            small_y = min(coord1[1], coord2[1])

            # Check if point is within Y range
            if y >= small_y and y <= big_y:
                if x == x_coord: # If it lies on the line
                    return True
                if x < x_coord:
                    has_east = True
                    last_east = i
                    # print("East cache hit")
                else:
                    has_west = True
                    last_west = i
                    # print("West cache hit")

        # If share Y coordinate - check North and South
        else:
            y_coord = coord1[1] # (Same for both)
            big_x = max(coord1[0], coord2[0])
            small_x = min(coord1[0], coord2[0])

            # Check if point is within Y range
            if x >= small_x and x <= big_x:
                if y == y_coord: # If it lies on the line
                    return True
                if y < y_coord:
                    has_north = True
                    last_north = i
                    # print("North cache hit")
                else:
                    has_south = True
                    last_south = i
                    # print("South cache hit")
        
        if has_north and has_south and has_east and has_west:
            return True

    # Loop all lines
    for i in range(len(coordinates)):
        coord1 = coordinates[(i-1)%len(coordinates)] # First loop will be back of list & index 0
        coord2 = coordinates[i]

        # If they share X dimension - check East and West
        if coord1[0] == coord2[0]:
            x_coord = coord1[0] # (Same for both)
            big_y = max(coord1[1], coord2[1])
            small_y = min(coord1[1], coord2[1])

            # Check if point is within Y range
            if y >= small_y and y <= big_y:
                if x == x_coord: # If it lies on the line
                    return True
                if x < x_coord:
                    has_east = True
                    last_east = i
                else:
                    has_west = True
                    last_west = i

        # If share Y coordinate - check North and South
        else:
            y_coord = coord1[1] # (Same for both)
            big_x = max(coord1[0], coord2[0])
            small_x = min(coord1[0], coord2[0])

            # Check if point is within Y range
            if x >= small_x and x <= big_x:
                if y == y_coord: # If it lies on the line
                    return True
                if y < y_coord:
                    has_north = True
                    last_north = i
                else:
                    has_south = True
                    last_south = i
        
        if has_north and has_south and has_east and has_west:
            return True
    return False

# Iterate around each every tile in the perimiter
# If they are all green or red then pass, fail otherwise
def is_valid(coordinates, corner1, corner2):

    # Attempt to shortcut - check the opposite corners first
    opp_corner_1 = (corner1[0], corner2[1])
    opp_corner_2 = (corner2[0], corner1[1])
    if (not is_red(coordinates, opp_corner_1[0], opp_corner_1[1])) and (not is_green(coordinates, opp_corner_1[0], opp_corner_1[1])):
        return False
    if (not is_red(coordinates, opp_corner_2[0], opp_corner_2[1])) and (not is_green(coordinates, opp_corner_2[0], opp_corner_2[1])):
        return False
    print("Passed corner")


    # Wander along the x-axis
    """
    Problem is we have to repeat full is_green for each tile.
    In this x-axis walk east and west should be true for all unless we walk through the wall.
    And even north and south may not change much...
    Since we always call in repeated walks, cache the indexes that work for north, south, east and west
    """
    for current_y in (opp_corner_1[1], opp_corner_2[1]): # Repeat for each y-axis
        start_y = min(opp_corner_1[0], opp_corner_2[0])
        end_y  = max(opp_corner_1[0], opp_corner_2[0])
        for current_x in range(start_y, end_y+1):
            if (not is_red(coordinates, current_x, current_y)) and (not is_green(coordinates, current_x, current_y)):
                # print("Failed on X-axis wander: ", current_x, current_y)
                return False
            
    print("Walked X")
            
    # Wander along the y-axis
    for current_x in (opp_corner_1[0], opp_corner_2[0]): # Repeat for each x-axis
        start_y = min(opp_corner_1[1], opp_corner_2[1])
        end_y = max(opp_corner_1[1], opp_corner_2[1])
        for current_y in range(start_y, end_y+1):
            if (not is_red(coordinates, current_x, current_y)) and (not is_green(coordinates, current_x, current_y)):
                # print("Failed on Y-axis wander")
                return False
            
    print("Walked Y")
    return True

def map_is_valid(coordinates, corner1, corner2, size):
    if is_valid(coordinates, corner1, corner2):
        return size
    return 0



if __name__ == '__main__':
    file = open("./day9/input.txt")
    coordinates = {}

    i = 0
    for line in file:
        line = line.strip()
        numbers = line.split(",")
        coordinates[i] = (int(numbers[0]), int(numbers[1]))
        i += 1

    # Build cache map
    for i in range(len(coordinates)):
        coord = coordinates[i]
        x = coord[0]
        y = coord[1]
        if x not in coordinates_map:
            coordinates_map[x] = [y]
        else:
            coordinates_map[x].append(y)

    areas = {}
    for i in range(len(coordinates)):
        for j in range(i, len(coordinates)):
            if i == j:
                continue
            coord1 = coordinates[i]
            coord2 = coordinates[j]
            length = abs(coord1[0] - coord2[0]) +1
            width = abs(coord1[1] - coord2[1]) +1
            
            areas[(i,j)] = length * width

    sorted_areas = sorted(areas.items(), key=lambda kv: (-kv[1], kv[0]))
    print("Total possible solutions size: " + str(len(sorted_areas)))

    # mp_arguments = []
    # for area in sorted_areas:
    #     mp_arguments.append((coordinates, coordinates[area[0][0]], coordinates[area[0][1]], area[1]))


    # with Pool(8) as p:
    #     result = p.starmap(map_is_valid, mp_arguments, chunksize=100)

        # print(result)
        # print("Result: " + str(max(result)))

    # Search for valid solutions, starting with largest
    i = 0
    search_size = len(sorted_areas)
    for area in sorted_areas:
        i +=1
        coord1 = coordinates[area[0][0]]
        coord2 = coordinates[area[0][1]]
        print("Current search: (" + str(i) + "/" + str(search_size) + ")")
        print(coord1)
        print(coord2)
        print(area[1])
        print("---")
        if is_valid(coordinates, coord1, coord2):
            print("Found Result: " + str(area[1]))
            break
def get_set(key, sets):
    for set in sets:
        if key in set:
            return set


file = open("./day8/input.txt")

"""
How am I going to do this?

1) Make a big dict of the distances between all junctions
2) Make another big dict with distances between all points
3) Order that dict to get all the closest junction boxes (may need more than 1000)
4) Make a set of sets to hold all circuits

"""

# Construct dictionary 'coordinates' to hold all junction point coordinates, indexed from 0 up
coordinates = {}
i = 0
for line in file:
    line = line.strip()
    numbers = line.split(",")
    coordinates[i] = (int(numbers[0]), int(numbers[1]), int(numbers[2]))
    i += 1

# Construct a dict - distances - key is two indexes of junction boxes and value is euclidean distance
distances = {}
for i in range(len(coordinates)):
    for j in range(i, len(coordinates)):
        if i == j:
            continue
        box1 = coordinates[i]
        box2 = coordinates[j]
        distances[(i,j)] = (box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2

sorted_distances = sorted(distances.items(), key=lambda kv: (kv[1], kv[0]))

# for i in range(10):
#     print(sorted_distances[i])
#     print("\t" + str(coordinates[sorted_distances[i][0][0]]))
#     print("\t" + str(coordinates[sorted_distances[i][0][1]]))


# Create sets to hold connected boxes
connected_sets = []
unconnected_set = set()

# Add boxes are unconnected initially
for i in range(len(coordinates)):
    unconnected_set.add(i)

# NUM_CONNECTIONS = 1000 # How many nearset connections do we make
# for i in range(NUM_CONNECTIONS):
i = -1
while unconnected_set or len(connected_sets) != 1: # Keep going until they're all connected in one set
    i += 1
    (index1, index2) = sorted_distances[i][0] # Get indexes of the two boxes

    # If either box is unconnected, put it into its own set
    if index1 in unconnected_set:
        unconnected_set.remove(index1)
        new_set = {index1}
        connected_sets.append(new_set)
    if index2 in unconnected_set:
        unconnected_set.remove(index2)
        new_set = {index2}
        connected_sets.append(new_set)


    index1_set = get_set(index1, connected_sets)
    index2_set = get_set(index2, connected_sets)
    if index1_set != index2_set:
        connected_sets.remove(index1_set)
        connected_sets.remove(index2_set)
        connected_sets.append(index1_set.union(index2_set))

print(index1, index2)
print(coordinates[index1], coordinates[index2])
print(coordinates[index1][0] * coordinates[index2][0])

# connected_sets.sort(key= lambda kv : -len(kv))
# total = 1
# for i in range(3):
#     total *= len(connected_sets[i])
# print(total)
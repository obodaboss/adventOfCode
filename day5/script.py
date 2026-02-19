file = open("./day5/input.txt")

# Parse ranges
ranges = []
for line in file:
    line = line.strip()
    if not line:
        break
    # print(line)
    range = (int(line.split("-")[0]), int(line.split("-")[1]))
    # print(range)
    ranges.append(range)

print("Ranges: " + str(ranges))

# Parse available ids
ids = []
for line in file:
    line = line.strip()
    # print(line)
    ids.append(int(line))

print("IDs: " + str(ids))

# Count the number of valid IDs
validIds = 0
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            validIds += 1
            break

print("Total valid IDs: " + str(validIds))

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

# Holds ordered ranges, with all lower bounds unique
ordered_ranges = []

# Keep going until all ranges moved to ordered_ranges
while ranges:
    # Find the lowest lower bound
    lowest = -1
    l_range = ()
    for range in ranges:
        if range[0] < lowest or lowest == -1:
            lowest = range[0]
            l_range = range

    # Remove the lowest range from list of ranges
    ranges.remove(l_range)

    # Find any ranges with same lowest bound as our lowest, mark for delete and merge
    ranges_to_remove = []
    for range in ranges:
        if range[0] == l_range[0]:
            ranges_to_remove.append(range)
            # Update l_range upper bound to bigger of the two
            if range[1] > l_range[1]:
                l_range = (l_range[0], range[1])


    # Remove all ranges_to_remove from ranges
    for range in ranges_to_remove:
        ranges.remove(range)

    ordered_ranges.append(l_range)

print("Ordered ranges: " + str(ordered_ranges))


# Process ordered list of ranges
# Ranges ordered by lower bound, and all lower bounds unique
merged_ranges = [] # Stores merged ranges that do not overlap
for range in ordered_ranges:

    # For first range just add and continue
    if not merged_ranges:
        merged_ranges.append(range)
        continue

    """
    Our current range has lower bound greater than the last.
    1) If lower bound is greater than previous upper bound, they do not overlap, can simply add
    2) If lower bound is less than or equal, they do overlap - merge the two ranges into one
    We do not need to consider any ranges but the previous one, as they are separate or already merged to previous
    """

    previous = merged_ranges[-1]

    # Case 1: Current lower bound is greater than previous upper
    if range[0] > previous[1]:
        # Just add and continue
        merged_ranges.append(range)
        continue

    # Case 2: The two ranges have overlap
    # If current range doesn't extend past previous, just drop current and continue
    if previous[1] >= range[1]:
        continue
    # Otherwise merge the two and add merged range back in
    merged_ranges.remove(previous)
    merged_range = (previous[0], range[1])
    merged_ranges.append(merged_range)
    continue

# Print merged ranges
print("Merged ranges: " + str(merged_ranges))

# Now we have list of ranges with no overlap, just add upper-lower for all ranges and that is result
total = 0
for range in merged_ranges:
    total += (range[1] - range[0]) + 1

print("Total: " + str(total))

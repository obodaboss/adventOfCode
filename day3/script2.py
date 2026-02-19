file = open("./day3/input.txt")

total = 0

for line in file:
    line = line.strip()

    # The joltage value being build up for this line
    jolt = ""

    # Restricted index choices
    min_index = 0
    max_index = len(line)-11 # Must leave at least 11 characters initially

    for i in range(12): # Need to pick 11 numbers for joltage

        # Find the largest number within the min and max ranges
        target = 10
        index = -1
        while index == -1:
            target -= 1
            index = line[min_index:max_index].find(str(target))

        # Add our found value to the joltage
        jolt += str(target)

        # Adjust indexes for next run
        min_index += (1+index) # Lowest choice is current pick+1
        max_index += 1 # Max always increases by 1

    # Convert Joltage to int and add to total
    print("Joltage: " + jolt)
    total += int(jolt)








print("Total: " + str(total))

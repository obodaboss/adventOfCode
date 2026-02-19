file = open("./day3/input.txt")

total = 0

for line in file:
    line = line.strip()
    # print("Current line: " + line)

    # Always start by looking for a 9
    # If it isn't last number, we will use as first digit
    target = 10
    index = -1
    while index == -1 or index == len(line)-1:
        target -= 1
        index = line.find(str(target))

    # Find second digit - highest number after index of first digit
    target2 = 10
    index2 = -1
    line2=line[index+1:]
    while index2 == -1:
        target2 = target2-1
        index2 = line2.find(str(target2))

    highest = int( str(target) + str(target2))
    print("Highest: " + str(highest))
    total += highest

print("Total: " + str(total))




countZeroes = 0
dialValue = 50

file = open("./day1p1/input.txt")
for line in file:
    line=line.strip()
    print(line)
    value = int(line[1:])

    if dialValue == 0 and line[0] == 'L':
        countZeroes -= 1

    if line[0] == 'R':
        dialValue += value
    else:
        dialValue -= value
    
    print(dialValue)

    if dialValue >= 100:
        countZeroes += int(dialValue/100)
        print("Count change: " + str(int(dialValue/100)))
        dialValue -= 100 * int(dialValue/100)
        print("#" + str(dialValue))
    elif dialValue < 0:
        countZeroes += (int(-(dialValue+1)/100)+1)
        print("Count change: " + str((int(-(dialValue+1)/100)+1)))
        dialValue += 100 * (int(-(dialValue+1)/100)+1)
        print("#" + str(dialValue))

    if dialValue == 0 and line[0] == 'L':
        countZeroes += 1
        print("Count change: 1")

print("Final result: " + str(countZeroes))

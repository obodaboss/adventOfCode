# Takes in number, returns true if any pattern found, false otherwise
def findPattern(num):

    # Each length of pattern we need to check for
    # (not optimised, just check every length of pattern that could be)
    for i in range (1,int(len(str(num))/2)+1):
        if findPatternFreq(num, i):
            return True
    return False

# Takes in a number and expected patten length, return true if pattern of that length found
def findPatternFreq(num, freq):
    num = str(num)

    if len(num)%freq != 0:
        return False

    for i in range(0, freq):
        value = num[i]
        for j in range(0, (len(num)-freq)+1, freq):
            if num[j+i] != value:
                return False
            
    return True


file = open("./day2p1/input.txt")
line = file.readline().strip()
ranges = line.split(",")

total = 0
for inputRange in ranges:

    # Get ranges
    start = int(inputRange.split('-')[0])
    end = int(inputRange.split('-')[1])

    # Use start as the counter, move until it is greater than end
    while start <= end:
        
        if findPattern(start):
            # print("Found: " + str(start))
            total+=start
        
        start=start+1
        
print("Total: " + str(total))
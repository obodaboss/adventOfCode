file = open("./day11/input.txt")

# Build initial map
map = {}
for line in file:
    line = line.strip()
    # print(line)

    [input, outputs] = line.split(":")
    outputs = outputs.strip().split(" ")
    map[input] = outputs



def findPaths(start, end, map):

    # Deep copy map
    local_map = {}
    for input in map:
        temp = []
        for output in map[input]:
            temp.append(output)
        local_map[input] = temp

    # Create initial numbered list - end has 1 way to get to end
    numbered = {}
    numbered["out"] = 0 # Out has value 0 unless it is the specified end goal
    numbered[end] = 1

    # Iterate until no more changes
    changed = True
    while changed:
        # print("### ITERATE ###")
        changed = False

        # Replace all known locations in map outputs with numbers
        for input in local_map:
            outputs = local_map[input]
            for numberStr in numbered:
                if numberStr in outputs:
                    numberInt = numbered[numberStr]
                    outputs.remove(numberStr)
                    outputs.append(numberInt)
                    changed = True
            local_map[input] = outputs

        # Empty numbered, as all instances have been replaced
        numbered = {}

        # Find maps where all outputs are numbers, add to numbered with value = sum(numbers)
        for input in local_map:
            outputs = local_map[input]
            if all(isinstance(x, int) for x in outputs):
                numbered[input] = sum(outputs)
        
        # Check for solution
        if start in numbered.keys():
            print(start + " -> " + end + ": " + str(numbered[start]))
            return numbered[start]
        
        # Remove numbered from map - no use any more
        for numberStr in numbered:
            del local_map[numberStr]
        
    print(start + " -> " + end + ": NOT FOUND")
    return -1



# print(map)

# findPaths("svr", "out", map)

if findPaths("dac", "fft", map) > 0:
    print("Going dac -> fft")
    result = findPaths("svr", "dac", map) * findPaths("dac", "fft", map) * findPaths("fft", "out", map)
else:
    print("Going fft -> dac")
    result = findPaths("svr", "fft", map) * findPaths("fft", "dac", map) * findPaths("dac", "out", map)
print("Result: " + str(result))


        
# Can't go from fft to dac
# Can go from dac to fft


"""
Find all paths from svr -> dac -> fft -> out
Too many to brute force
"""
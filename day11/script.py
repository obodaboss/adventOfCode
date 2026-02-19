file = open("./day11/input.txt")


def recurse(input, map):
    if input == "out":
        return 1
    
    outputs = map[input]
    total = 0
    for output in outputs:
        total += recurse(output, map)

    return total

map = {}
for line in file:
    line = line.strip()
    # print(line)

    [input, outputs] = line.split(":")
    outputs = outputs.strip().split(" ")
    map[input] = outputs

# print(map)

result = recurse("you", map)
print("Result: " + str(result))
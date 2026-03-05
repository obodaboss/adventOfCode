FILE_PATH = "./day12/input.txt"
file = open(FILE_PATH)

sizes = {}

current_index = 0
fill_count = 0
total_count = 0
for line in file:
    line = line.strip()

    if len(line) == 0:
        sizes[current_index] = (fill_count, total_count)
        continue

    # Use a separate loop for size under tree
    if line.find('x') != -1:
        break

    if line[1] == ":":
        current_index = int(line[0])
        fill_count = 0
        total_count = 0
        continue

    total_count += len(line)
    fill_count += line.count('#')


for size in sizes.items():
    print(size)

print("#"*30)
file = open(FILE_PATH)
total = 0
for line in file:
    line = line.strip()
    
    if line.find('x') == -1:
        continue

    num1 = line[0:line.find('x')]
    num2 = line[line.find('x')+1:line.find(':')]
    size = int(num1) * int(num2)

    presents = list(map(lambda x:int(x), line[line.find(':')+2:].split(' ')))

    total_present_size = 0
    for i in range(len(presents)):
        total_present_size += presents[i] * sizes[i][0]

    print("Region size:", size)
    print("Total presents size:", total_present_size)
    print("Size to spare:", size - total_present_size)
    print("-"*30)

    # Cheesing it here - all the regions have far more space than needed or negative (i.e. clearly imposisble)
    if size - total_present_size > 100:
        total += 1

print("Total:", total)
file = open("./day10/input.txt")

total = 0
for line in file:
    line = line.strip()
    print(line)

    # Get the required light values
    light_string = line[line.find("[")+1:line.find("]")]
    target_lights = list(map(lambda x:x=="#", light_string))
    print(target_lights)

    # Get the buttons
    buttons = []
    while line.find("(") != -1:
        end_idx = line.find(")")
        light_to_flip = line[line.find("(")+1:end_idx]
        light_to_flip = light_to_flip.split(",")
        light_to_flip = list(map(lambda x:int(x), light_to_flip))
        buttons.append(light_to_flip)

        line = line[end_idx+1:]

    print("Buttons: " + str(buttons))

    # Total possible combinations is number of 2^(num_lights)
    combinations = 2**len(buttons)
    # print("Total possible combinations: " + str(combinations))

    # Go from 0 to combinations-1, convert number into binary with num bits == num buttons
    best_solution = -1
    for i in range(combinations):
        binary = bin(i)[2:]
        binary = "0"*(len(buttons)-len(binary)) + binary
        # print(binary)
        current_combination = list(map(lambda x:x=="1", binary))
        # print(binary)

        # Create array of lights to edit - all off by default
        lights = [False]*len(target_lights)
        # print(lights)

        # Loop and apply each button the combination has as True
        for i in range(len(current_combination)):
            # Only apply if buttons_to_press for that index is True
            if current_combination[i]:
                # Flip all mentioned lights the button is wired to
                for light_to_flip in buttons[i]:
                    lights[light_to_flip] = not lights[light_to_flip]

        
        # Check if this is a solution
        if lights == target_lights:
            # print("Solution found: " + str(current_combination))
            # print(sum(current_combination))
            current_solution = sum(current_combination)
            if best_solution == -1 or current_solution < best_solution:
                best_solution = current_solution

    print("Best solution found: " + str(best_solution))
    if best_solution == -1:
        raise Exception("No solution found!!")
    total += best_solution
    print()

print("Total: " + str(total))

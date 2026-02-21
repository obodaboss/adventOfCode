from ortools.sat.python import cp_model

file = open("./day10/input.txt")

total = 0
for line in file:
    line = line.strip()
    print(line)


    # Parse the buttons
    buttons = []
    while line.find("(") != -1:
        end_idx = line.find(")")
        light_to_flip = line[line.find("(")+1:end_idx]
        light_to_flip = light_to_flip.split(",")
        light_to_flip = list(map(lambda x:int(x), light_to_flip))
        buttons.append(light_to_flip)

        line = line[end_idx+1:]
    print("Buttons: " + str(buttons))


    # Parse target values
    line = line[line.find("{")+1:-1]
    targets = list(map(lambda x:int(x), line.split(",")))
    print("Targets: " + str(targets))

    # Create the initial model
    model = cp_model.CpModel()


    # Create a variable for each button found
    variables = {}
    for i in range(len(buttons)):
        min_value = 0
        max_value = min(map(lambda x:targets[x], buttons[i]))
        name = "b" + str(i)
        var = model.new_int_var(min_value, max_value, name)
        variables[i] = var


    # Create a constraint for all the target values
    for i in range(len(targets)):

        # Value all buttons must add up to
        value = targets[i]

        # Get indexes of buttons involved
        indexes = []
        for buttonIndex in range(len(buttons)):
            if i in buttons[buttonIndex]:
                indexes.append(buttonIndex)

        # Create the constraint
        x = list(map(lambda a:variables[a], indexes))
        model.add(sum(x) == value)


    # Add minimisation goal
    model.minimize(sum(variables.values()))
    
    # Solve it
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    # Inspect solution
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        sub_total = 0
        for var in variables:
            # print(f"{var} = {solver.value(variables[var])}")
            sub_total += solver.value(variables[var])
        print("Sub-total: " + str(sub_total))
        total += sub_total
    else:
        print("No solution found.")
    


print(f"Total: {total}")
print("End!")

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
        #print("Start value: " + str(start))

        # If start has an odd number of digits, increase it to have an even number of digits
        if len(str(start))%2 == 1:
            # print("Start value (" + str(start) + ") odd length, increasing")
            start = int("1" + "0"*len(str(start)))
            continue

        # If digit n/2 doesn't match digit 0, increase it so it will
        halfIndex = int(len(str(start))/2)
        change = False
        for index in range(0, halfIndex): # 0 to (n-1)

            #print("Checking index (" + str(index) + ") : Values(" + str(start)[index] + "," + str(start)[halfIndex+index] + ")")
            if str(start)[index] != str(start)[halfIndex+index]:
                #print("Indexes not equal")
                zeroes = halfIndex-(1+index)

                tempstart = start
                start += int(str((int(str(start)[index]) - int(str(start)[halfIndex+index]))%10) + "0"*zeroes)

                if len(str(start)) > halfIndex+index+1:
                    start -= int(str(start)[(halfIndex+index+1):])

                # Reset digits to right of halfIndex+index to 0
                # int(str(start)[(halfIndex+index+1):])


                #print("Adding: " + str(start-tempstart))
                change = True
                break
            # 123323
            # 199299
            # 200199
        
        if change:
            continue
        
        print("FOUND: " + str(start))
        total += start
        start=start+1
    
    #     if total > 0:
    #         break
    # if total > 1:
    #     break
        
print(total)
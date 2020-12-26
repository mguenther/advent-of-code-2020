def spoken_number_after(iterations, starting_numbers):
    memory = {}
    i = 1
    last_number = None

    for starting_number in starting_numbers:
        memory[starting_number] = (i, i) # last, earliest
        i += 1
        last_number = starting_number

    while i <= iterations:
        if last_number in memory:
            spoken_number = memory[last_number][0] - memory[last_number][1]
            if spoken_number in memory:
                memory[spoken_number] = (i, memory[spoken_number][0])
            else:
                memory[spoken_number] = (i, i)
            last_number = spoken_number
        else:
            spoken_number = 0
            last_number = spoken_number
            memory[last_number] = (i, i)
            
        i += 1

    return spoken_number

print(spoken_number_after(2020, [6,13,1,15,2,0]))
print(spoken_number_after(30000000, [6,13,1,15,2,0]))
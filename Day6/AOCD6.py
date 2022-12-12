file = open("Day6/AOCD6.txt", "r")
for row in file:
    count = 0
    value = ''
    for char in row:
        count += 1
        if len(value) < 4:
            value += char
        else:
            value = value[1:] + char
        if len(value) == 4:
                subroutine = value
                for letter in subroutine:
                    subroutine = subroutine[1:]
                    if letter in subroutine:
                        break
                if len(subroutine) == 0:
                    break
    print(count)


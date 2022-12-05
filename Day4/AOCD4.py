file = open("AOCD4.txt", "r")
counter = 0
for line in file:
    values = line.split(",")
    elf1 = [int(x) for x in values[0].split("-")]
    elf2 = [int(x) for x in values[1].split("-")]
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1] or elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        counter += 1
    
print(counter)
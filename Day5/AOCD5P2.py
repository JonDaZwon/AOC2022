file = open("Day5/AOCD5.txt", "r")
stacks = [[], [], [], [], [], [], [], [], []]
rowcount = 1
for row in file:
    rowcount += 1
    if row[0] == ' ' and row[1] == ' ' or row[0] == "[":
        splitRow = [ row[i:i+4] for i in range(0, len(row), 4)]
        i = 0
        for value in splitRow:
            if value[0] != ' ':
                stacks[i].insert(0,value[1])
            i += 1
    if row[0] == 'm':
        splitRow = row.split(" ")
        count = int(splitRow[1])
        fromIndex = int(splitRow[3]) - 1
        toIndex = int(splitRow[5]) - 1
        stacks[toIndex].extend(stacks[fromIndex][len(stacks[fromIndex])-count:])
        stacks[fromIndex] = stacks[fromIndex][0:len(stacks[fromIndex])-count]
topCrate = ''
for stack in stacks:
    if(len(stack) > 0):
        topCrate += stack.pop()
print(topCrate)
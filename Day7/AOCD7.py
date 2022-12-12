file = open("Day7/AOCD7.txt", "r")
sum = 0
activeFolders = {"/\n": 0}
rowcount = 0
for row in file:
    rowcount += 1
    data = row.split(" ")
    if data[0] == "$":
        if data[1] == "cd":
            if data[2] == "..\n":
                key = next(reversed(activeFolders.keys()))
                if activeFolders[key] <= 100000:
                    sum += activeFolders[key]
                del activeFolders[key]
            elif data[2] == "/\n":
                activeFolders = {"/\n": activeFolders["/\n"]}
            else:
                activeFolders[next(reversed(activeFolders.keys())) + "/" + str(data[2])] = 0
    elif data[0] == "dir":
        pass
    else:
        for key, value in activeFolders.items():
            activeFolders.update({key: value + int(data[0])})

for key, value in activeFolders.items():
    if value <= 100000:
        sum += value
print(sum)
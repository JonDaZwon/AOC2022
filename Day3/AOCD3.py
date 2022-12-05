file = open("AOCD3.txt", "r")
total = 0
for line in file:
    length = len(line)
    if length%2 != 0:
        length -= 1
    split = int(length/2)
    secondHalf = line[split:length]
    for character in line:
        if character in secondHalf:
            addition = ord(character)
            if (addition > 90):
                total += addition - 96
                break
            else:
                total += addition - 38
                break

print(total)
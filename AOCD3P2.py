file = open("AOCD3.txt", "r")
total = 0
sack1 = ""
sack2 = ""
sack3 = ""
for line in file:
    if sack1 == "":
        sack1 = line
    elif sack2 == "":
        sack2 = line
    elif sack3 == "":
        sack3 = line
        for character in sack1:
            if character in sack2:
                if character in sack3:
                    addition = ord(character)
                    if (addition > 90):
                        total += addition - 96
                        break
                    else:
                        total += addition - 38
                        break
    else:
        sack1 = line
        sack2 = ""
        sack3 = ""

print(total)
file = open("AOCD2.txt", "r")
totalScore = 0
for line in file:
    match line[0]:
        case "A":
            match line[2]:
                case "X":
                    totalScore += 3
                case "Y":
                    totalScore += 4
                case "Z":
                    totalScore += 8
        case "B":
            match line[2]:
                case "X":
                    totalScore += 1
                case "Y":
                    totalScore += 5
                case "Z":
                    totalScore += 9
        case "C":
            match line[2]:
                case "X":
                    totalScore += 2
                case "Y":
                    totalScore += 6
                case "Z":
                    totalScore += 7

print(totalScore)

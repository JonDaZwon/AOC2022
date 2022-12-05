file = open("AOCD2.txt", "r")
totalScore = 0
for line in file:
    match line[0]:
        case "A":
            match line[2]:
                case "X":
                    totalScore += 4
                case "Y":
                    totalScore += 8
                case "Z":
                    totalScore += 3
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
                    totalScore += 7
                case "Y":
                    totalScore += 2
                case "Z":
                    totalScore += 6

print(totalScore)

file = open("AOCD1.txt", "r")
topCalorieCount = 0
topElfNumber = 0
currentElfCalorieCount = 0
currentElfNumber = 0
for line in file:
    if line == "\n":
        if currentElfCalorieCount > topCalorieCount:
            topCalorieCount = currentElfCalorieCount
            topElfNumber = currentElfNumber
        currentElfNumber += 1
        currentElfCalorieCount = 0
    else:
        currentElfCalorieCount += int(line)

print(f"Top Elf: {topElfNumber} Total Calories: {topCalorieCount}.")

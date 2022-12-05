file = open("AOCD1.txt", "r")
calorieCounts = []
currentElfCalorieCount = 0
for line in file:
    if line == "\n":
        calorieCounts.append(currentElfCalorieCount)
        currentElfCalorieCount = 0
    else:
        currentElfCalorieCount += int(line)

calorieCounts.sort(reverse=True)
sumOfTop3 = calorieCounts[0] + calorieCounts[1] + calorieCounts[2]
print(f"Total Calories: {sumOfTop3}.")

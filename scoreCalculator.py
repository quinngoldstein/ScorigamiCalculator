# Filename:    scoreCalculator.py
# Author:      Quinn Goldstein
# Version:     Version 1
# Description: This Python program calculates what would be needed to achieve a certain Scorigami in American football.
#              For more information, see nflscorigami.com.

score = input("Enter an NFL score: ")
touchdowns = 0
onePoints = 0
twoPoints = 0
fieldGoals = 0
safeties = 0
# Further complex handling of safety scoring may be added in future versions of this application.

score = int(score)
originalScore = score

# Hard code special case
if score == 1:
    print("A score of 1 would require the near impossible 1 point safety.")
    exit()

# Determine touchdowns first, since most common form of scoring
while score >= 7:
    score -= 7
    touchdowns += 1
    onePoints += 1

# Determine field goals, two point conversions
if score % 3 == 0:
    fieldGoals = score / 3
elif score % 3 == 1:
    if score == 1:
        twoPoints += 1
        onePoints -= 1
    else:
        while score > 3:
            score -= 3
            fieldGoals += 1
        twoPoints += 1
        onePoints -= 1
else:
    if originalScore > 9:
        twoPoints += 2
        onePoints -= 2
        while score > 3:
            score -= 3
            fieldGoals += 1
    elif originalScore == 9:
        fieldGoals = 3
    elif originalScore == 5:
        safeties = 1
        fieldGoals = 1
    elif originalScore == 2:
        safeties = 1

# Print statistics
print("\nObtaining score of " + str(originalScore) + " requires:")
print("Touchdowns (6 points):            " + str(touchdowns))
print ("\nAfter touchdown scores:")
print("Extra points (1 point):           " + str(onePoints))
print("Two point conversions (2 points): " + str(twoPoints))
print("\nOther scoring:")
print("Field goals (3 points):           " + "{:.0f}".format(fieldGoals))
print("Safeties (2 points):              " + str(safeties) + "\n")
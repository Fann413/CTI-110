# Jacob Fann
# 10/23/26
# P4HW1
# Edit P2HW2, use loops instead of individual statements

# Create list of scores
scores_list = []

# Ask for user input
score = int(input("How many scores do you want to enter? "))

for grades in range(1, score + 1):
    score_number = int(input(f"Enter Score #{grades}: "))
    # Calculates if number falls inbetween 0 and 100, if not, activate the while loop
    while score_number < 0 or score_number > 100:
            print("INVALID SCORE. Score should be between 0 and 100!")
            score_number = int(input(f"Enter Score #{grades} Again: "))
    # When a score is valid, it adds it to the list and continues the for loop
    scores_list.append(score_number)

# Determne the average of the scores
scores_average = sum(scores_list) / len(scores_list)

# Determine the letter grade
if scores_average >= 90:
      grade = "A"
elif scores_average >= 80:
      grade = "B"
elif scores_average >= 70:
      grade = "C"
elif scores_average >= 60:
      grade = "D"
else:
    grade = "F"

# Print results to user
print()
print("-----------Results-----------")
print(f"{'Lowest Grade:':<20}{min(scores_list):>9}")
print(f"{'Modified List:':<20}{scores_list}")
print(f"{'Average:':<20}{scores_average:>9,.2f}")
print(f"{'Grade:':<20}{grade:>9}")
print("-"*29)

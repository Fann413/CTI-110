# Jacob Fann
# 9/27/26
# P2HW2
# Grade average calculator using lists

# Gather data for each module grade
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Create list of all grades gathered 
grades = [module1, module2, module3, module4, module5, module6]

# Calculate average of grades
grade_average = sum(grades) / len(grades)

#Print results, format to align elements
print()
print("-----------Results-----------")
print(f"{'Lowest Grade:':<20}{min(grades):>9}")
print(f"{'Highest Grade:':<20}{max(grades):>9}")
print(f"{'Sum of Grades:':<20}{sum(grades):>9}")
print(f"{'Average:':<20}{grade_average:>9,.2f}")
print("-"*29)
print()
# Determine letter grade based on the avg
if grade_average >= 90:
    letter_grade = "A"
if grade_average >= 80 and grade_average <= 89:
    letter_grade = "B"
if grade_average >= 70 and grade_average <= 79:
    letter_grade = "C"
if grade_average >= 60 and grade_average <= 69:
    letter_grade = "D"
if grade_average >= 0 and grade_average <= 59:
    letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")
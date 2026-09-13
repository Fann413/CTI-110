# Jacob Fann
# 9/13/26
# P1HW1
# Calculating exponets, addition and subtraction

# Calculate Exponets

print("------Calculating Exponets------")
print()
print()

base = int(input("Enter an integer as the base value: "))
exponet = int(input("Enter an integer as the exponet: "))
print()
print()
result = base ** exponet
print(base, "raised to the power of", exponet, "is", result, "!!")

print()
print()

# Calculate addition and subtraction

print("------Addition and subtraction------")
print()
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print()
print()

print(num1, "+", num2, "-", num3, "is equal to", final_result)
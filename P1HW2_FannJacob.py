# Jacob Fann
# 9/13/26
# P1HW2
# Travel Expenses Caclulator

print("This program calculates and displays travel expenses")
print()

# defining each variable needed
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much will you spend on gas? "))
hotel = int(input("Approximately, how much will you need for an accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print()

# calculations for output, first adds all expenses, then subtracts from budget
total_cost = gas + hotel + food
remainder = budget - total_cost

# final output
print("--------Travel Expenses--------")
print("Initial Budget:", budget)
print()
print("fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", remainder)

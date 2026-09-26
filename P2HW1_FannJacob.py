# Jacob Fann
# 9/25/2026
# P2HW1
# Format existing program

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


print(f"You are going to: {destination}! Your expenses are as follows:")
print()
print("--------Travel Expenses--------")
print(f"{'Initial Budget:':^20} ${budget:<20}")
print("-"*31)
print(f"{'Fuel:':^20} ${gas:<20}")
print(f"{'Accomodation:':^20} ${hotel:<20}")
print(f"{'Food:':^20} ${food:<20}")
print("-"*31)
print(f"{"What's left:":^20} ${remainder:<20}")
print("-"*31)
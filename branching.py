# branching (if/else/elif)

# get age from user
age = int(input("What is your age? "))

# determine if age is older than 65
if age >= 65:
    print("You ARE a Senior Citizen")
    discount = 0.15

else:
    print("You ARE NOT a Senior Citizen")
    discount = 0
    
print("You made a $100 purchase!")
disc_amount = 100 * discount
print(f"Your discount is: {disc_amount}!")
total = 100 - disc_amount
print(f"Your total is: {total}")
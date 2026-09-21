# Helper file for P2HW2

# Get three prices from the user
price1 = float(input("Enter price of first item: "))
price2 = float(input("Enter price of second item: "))
price3 = float(input("Enter price of third item: "))

# Create a list from the input variables
prices = [price1, price2, price3]

# If list is all ints and floats, there are functions you can call on the list

# sum function adds all list items
print(sum(prices))

# min function returns lowest value in the list
min_value = min(prices)
print(f"Lowest price is {min_value}")

# max function returns highest value in the list
max_value = max(prices)
print(f"Highest price is {max_value}")

# Calculate average of prices
average = sum(prices) / len(prices)
print(f"The average of the prices is {average}")
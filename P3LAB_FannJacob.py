# Jacob Fann
# 9/30/26
# Calculate coins and dollars needed

# Get money input
money = float(input("Enter an amount of money: $"))

# Move decimal two places to the right
money_int = int(money * 100)

# determine how many dollars are needed
dollars = money_int // 100

money_int = money_int - (dollars * 100)

# determine how many quarters are needed
quarters = money_int // 25

money_int = money_int - (quarters * 25)

# Determine how many dimes are needed
dimes = money_int // 10

money_int = money_int - (dimes * 10)

# Determine how many nickels are needed
nickels = money_int // 10

money_int = money_int - (nickels * 5)

# Determine how many pennies are needed
pennies = money_int // 1

money_int = money_int - pennies

print("*" * 60)

# only display coins if one or more is needed

# define function
def  print_needed(coin, coin_name):
    if coin >=1:
        if coin == 1:
            print(f"{coin} {coin_name}")
        if coin > 1:
            if coin_name == "penny":
                print(f"{coin} pennies")
            else:
                print(f"{coin} {coin_name}s")
# Call the function using the different dollars & coins

print_needed(dollars, "dollar")
print_needed(quarters, "quarter")
print_needed(dimes, "dime")
print_needed(nickels, "nickel")
print_needed(pennies, "penny")
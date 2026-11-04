# Jacob Fann
# 11/1/2026
# P3LAB
# Using integer division and if/else statements

import random

def disperse_change(change):
    #Convert the float value into an integer
    change = int(change * 100)
        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

def main():

    # Generate random  number of money owed
    owed = round(random.uniform(0.01, 100.00), 2)
    # Display amount owed
    print(f"You owe {owed:,.2f}")
    #Get float input for amount_paid
    amount_paid = float(input("How much cash will you put in the self-checkout? "))
    # Calculate how much change
    change = amount_paid - owed
    # Display change
    print(f"Your change is {change:,.2f}")
    # Call disperse_change function
    disperse_change(change)

# Call main function
if __name__ == "__main__":
    main()
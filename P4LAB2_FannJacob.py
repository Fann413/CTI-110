# Jacob Fann
# 10/19/26
# P4LAB2
# Display multiplication tables for integers from 1 to 12

run_again = "yes"

# while loop that is true when run_again equals yes
while run_again == "yes":
    user_int = int(input("Enter an integer: "))
    print()
    
    # Determine if user int is pos or neg
    if user_int < 0:
        print("Program does not work with negative numbers.")
    else:
        # Display mult table for user int
        for mult_int in range(13):
            final_int = user_int * mult_int
            print(f"{user_int} * {mult_int} = {final_int}")
    
    print()
    # Ask user if they want to use program again
    run_again = input("Run program again? ").lower()

# Loop Break
print()
print("Thanks for using the program.")
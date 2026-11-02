# Learn python functions

# Define our own functions
def multiply_by_100(number):
    answer = number * 100
    print(f"The answer is {answer}")
    return answer

# Define the main function
def main():
    num = int(input("Enter a number: "))
    print(f"The number you chose is: {num}")
    
    # Call the funtion by that multiples
    answer = multiply_by_100(num)
    
    print(f"This is the {answer} in the main")
    
# Call the main functions
if __name__ == "__main__":
    main()
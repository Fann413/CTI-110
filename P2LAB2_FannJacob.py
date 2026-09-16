# Jacob Fann
# 9/16/2026
# P2LAB2
# Describe MPG of cars via dictionaries. 

# Dictionary, cars are keys, values are MPG
print()
cars = {"Camaro":18.21,"Prius":52.36,"Model S":110,"Silverado":26}

# Display whole dictionary
print(cars.keys())

# Get car from user
print()
vehicle_choice = input("Enter A vehicle to see it's MPG: ")

mpg_choice = cars[vehicle_choice]

print(f"The {vehicle_choice} gets {mpg_choice} mpg.")
print()

# Get miles to drive from user
miles = float(input(f"How many miles will you drive the {vehicle_choice}? "))

gas = miles / mpg_choice

print(f"{gas:.2f} gallon(s) of gas are needed to drive the Prius {miles}.")

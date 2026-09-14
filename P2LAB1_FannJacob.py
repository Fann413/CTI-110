# Jacob Fann
# 9/14/2026
# P2LAB1
# Calculating circles

# Import value for pi
from math import pi

print(pi)

# Get radius from user
radius = input("What is the radius of the circle? ")

# Show data type (string)
print(type(radius))

# Convert
radius = float(radius)

# Show data type (float)
print(type(radius))

# Calculate diameter
diameter = 2 * radius
# Calculate circumference
circumference = 2 * 3.14 * radius
# Calculate area
area = pi * radius ** 2

# Diameter Output
print()
print(f"The diameter of the circle is {diameter:.1f}")
# Circumference Output
print()
print(f"The circumference of the circle is {circumference:.2f}")
# Area Output
print()
print(f"The area of the circle is {area:.3f}")
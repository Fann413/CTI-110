#
#
#
#

import turtle

# set up the turtle drawing object
window = turtle.Screen()

cozey = turtle.Turtle()

cozey.pensize(5)
cozey.pencolor("purple")

# use loop to draw the square
for side in range(4):
    cozey.forward(200)
    cozey.right(90)

num = 1
while num <= 3:
    cozey.forward(200)
    cozey.left(120)
    num = num + 1

# Keep at bottom
window.mainloop()
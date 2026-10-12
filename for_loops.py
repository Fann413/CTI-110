# For loop that iterates 5 times

import time

'''
# for (variable) range(start,end,step amount):
# range never includes last value
for i in range(2,11,2):
    print(i)
    time.sleep(2)
    
#Loop Break
print("End!")
'''

# Create a list
friends = ["Victoria", "Sunny", "Joshua", "Jerry", "Persia"]

# Loop to display each friend with an emoji
print("These are my friends:")

for friend_name in friends:
    print(friend_name + " ^_^")
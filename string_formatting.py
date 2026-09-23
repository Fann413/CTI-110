# Learn to format strings using an f-string

num_dogs = 7
num_hamsters = 12
num_fish = 10
num_butterflies = 5

dog_cost = 55.55
hamster_cost = 5.99
fish_cost = 248.00
butterfly_cost = 27.52

print(f"======{'Animal Type':^25}{'Number Available':^25}{'Cost':^25}======")
print("-" * 100)
print(f"======{'Dogs':^25}{num_dogs:^25}${dog_cost:^25,.2f}======")
print(f"======{'Hamsters':^25}{num_hamsters:^25}${hamster_cost:^25,.2f}======")
print(f"======{'Fish':^25}{num_fish:^25}${fish_cost:^25,.2f}======")
print(f"======{'Butterflies':^25}{num_butterflies:^25}${butterfly_cost:^25,.2f}======")
#RC, 1st, Random number notes.

import random 

#Genrate state options
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

#Set states
strength = int(input("Which stat do you want as strength?\n"))
intelagence = int(input("Which stat do you want as intelagence?\n"))
wisdom = int(input("Which stat do you want as wisdom?\n"))
constitution = int(input("Which stat do you want as constitution?\n"))
charisma = int(input("Which stat do you want as charisma?\n"))
dexterity = int(input("Which stat do you want as dexterity?\n"))
print(f"This is a random number 0-1: {random.random()}")
print(f"This is a random number 1-20: {random.randint(1,20)}")

#RC, 1st, Nesting notes
import random


age = random.randint(1,37)

if age < 18:
    print("You are not an adult.")
    if age >= 16:
        print("But you can drive.")
else:
    print("You are an adult")
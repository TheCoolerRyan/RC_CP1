#For fun rock paper scissors!
print("This is a program that mimics the game rock paper scissors! I will ask you for a number...")
win = False
import random
while win == False:
    random_int = random.randint(1,3)
    if random_int == 1:
        choice = "Rock"
    elif random_int ==2:
        choice = "Paper"
    elif random_int ==3:
        choice = "Scissors"
    choice2 = int(input("Pick a number 1-3 (1 = , 2= ,3= !)"))
    
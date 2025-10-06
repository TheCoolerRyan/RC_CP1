#For fun rock paper scissors!
print("This is a program that mimics the game rock paper scissors! I will ask you for a number 1-3, 1 = Rock, 2 = Paper, 3 = scissors. You will play against a bot, 1st to 3 victorys wins it all")

rock ="""
     _______
    ---'    )
           (____)
          (_____)
          (____)
    ---.__(___)
"""
paper = """
_______
    ---'    )____
           ______)
          _______)
          _______)
    ---.__________)
"""

scissors = """
_______
    ---'    )____
           ______)
          __________)
          (____)
    ---.__(___)
"""


bot_win = 0
human_win = 0
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
    choice2 = int(input("\nPick a number 1-3 (1 = Rock, 2 = Paper,3 = Scissors!)"))
    if choice2 == 1:
        choice2 = "Rock"
    elif choice2 == 2:
        choice2 = "Paper"
    elif choice2 == 3:
        choice2 = "Scissors"
    else:
        print(f"{choice2} is not an option! >:( One point will be added to the bot as a penalty.")
        bot_win += 1




    if choice == "Rock" and  choice2 == "Rock":
        print(f"Its a tie! The bot chose {choice}\n{rock} \nand you chose {choice2}\n{rock}!")

    if choice == "Rock" and  choice2 == "Paper":
        print(f"You got a point! The bot chose {choice}\n{rock} \nand you chose {choice2}\n{paper}!")
        human_win += 1

    if choice == "Rock" and  choice2 == "Scissors":
        print(f"Oh no! The bot got a point! The bot chose {choice}\n{rock} \nand you chose {choice2}\n{scissors}!")
        bot_win += 1

    if choice == "Paper" and  choice2 == "Rock":
        print(f"Oh no! The bot got a point! The bot chose {choice}\n{paper} \nand you chose {choice2}\n{rock}!")
        bot_win += 1
    
    if choice == "Paper" and  choice2 == "Paper":
        print(f"Its a tie! The bot chose {choice}\n{paper} \nand you chose {choice2}\n{paper}!")
    
    if choice == "Paper" and  choice2 == "Scissors":
        print(f"You got a point! The bot got a point! The bot chose {choice}\n{paper} \nand you chose {choice2}\n{scissors}!")
        human_win += 1
    
    if choice == "Scissors" and  choice2 == "Rock":
        print(f"You got a point! The bot chose {choice} \n{scissors} \nand you chose {choice2}\n{rock}!")
        human_win += 1
    
    if choice == "Scissors" and  choice2 == "Paper":
        print(f"Oh no! The bot got a point! The bot chose {choice} \n{scissors} \nand you chose {choice2}\n{paper}!")
        bot_win += 1
    
    if choice == "Scissors" and  choice2 == "Scissors":
        print(f"Its a tie! The bot chose {choice} \n{scissors} \nand you chose {choice2} \n{scissors}!")

    print(f"\nYour score is: {human_win}\nThe bot's score is: {bot_win}")





    if bot_win == 3:
        win = int(input("\nSorry but the bot wins it all, maybe next time! Do you want to lay again? (Only put 1 or 2, 1 = Yes, 2 = No)"))
        if win == 1:
            win = False
        else:
            win = True
        bot_win = 0
        human_win = 0
        
    if human_win == 3:
        win = int(input("\nYay! You just won it all! Do you want to play again? (Only put 1 or 2, 1 = Yes, 2 = No)"))
        if win == 1:
            win = False
        else:
            win = True
        human_win = 0
        bot_win = 0
    
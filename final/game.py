#RC, 1st, Final game

import random

#set the list for beaten people
beaten = []
#set stat dictionary that will hold win lose and gold as well
stat = { "Charm": 8,
      "Wisdom": 8,
      "Strength": 8,
      "Win": 0,
      "Lose": 0,
      "Gold": 0}
#Set functions

# 1st function
#def stat_increase(stat, gain):
def stat_increase(stat, gain):
    #Create the stat gains for crocs, nerdy_glasses, and Suit. the first item.
    #Make sure that they must have gold and that we return new stats.
    if gain == "Crocs" and stat["Gold"] > 1:
        stat["Charm"] -= 2
        stat["wisdom"] -= 2
        stat["strength"] += 4
        stat["Gold"] -=2
        return stat
    elif gain == "Nerdy Glasses" and stat["Gold"] > 1:
        stat["Charm"] -= 2
        stat["Wisdom"] += 4
        stat["Strength"] -= 2
        stat["Gold"] -=2
        return stat
    elif gain == "Suit" and stat["Gold"] > 1:
        stat["Charm"] += 4
        stat["Wisdom"] -= 2
        stat["Strength"] -= 2
        stat["Gold"] -=2
        return stat
    elif gain == "Charm" and stat["Gold"] > 1:
        stat["Charm"] += 2
        stat["Gold"] -= 2
        return stat
    elif gain == "Wisdom" and stat["Gold"] > 1:
        stat["Wisdom"] += 2
        stat["Gold"] -= 2
        return stat
    elif gain == "Strength" and stat["Gold"] > 1:
        stat["Strength"] += 2
        stat["Gold"] -= 2
        return stat
    else:
        print("You don't have enough money...")
        return stat

# 2nd function
#def lose(stat):
def lose(stat):
    #If your lose stats are greater than 3, return true to end the game
    if stat[lose] == 3:
        return True
    #else:
    else:
        #return false and keep the game going.
        return False

# 3rd function
#def fight_room(stat, room)
def fight_room(stat,room,beaten):
    #if room == 1:
    if room == 1:
        pass
        #ask them if they want to by an upgrade/item

        #def stat_increase

        #Make sure not to allow them to buy the stats multiple times.
    #elif room == 2:
    elif room == 2:
        #if 2 isn't in beaten list:
        if 2 not in beaten:
            #write out all of the enemy stats here.
            b_strength = 5; b_wisdom = 10; b_charm = 2
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,2)
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Wisdom"
                    chain = b_wisdom
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("What stat would you like to attack with, Wisdom, Strength, or Charm?").strip().upper()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list

                #else and one loss to your stats and add the room to the 'beaten' list
        #else:
            #Print of thing telling the person this room has already been concured or that the number is to high

        #Repeat this proceses for rooms 3-7, though have the stats be different as well as the dialoge

    #if the room is 8:
        #Check to see if the user has won the mandatory amount of wins.
            #enemy = student_prez
            #write out all of the enemy stats here.
            
            #Set temporary wins and losses to 0

            #While True:
                #Roll for who gets to decide the attack.

                #if choice = 1:
                    #set attack to the bots strongest
                #else:
                    #While True:
                        #Ask the user what stat they would like to use.

                        #check if its one of the three actual stats.
                            #Break to get out of loop
                        #Else:
                            #tell them its not a choice

                #Set up bots stats for when the user picks the choice

                #Set up the rolls based on the random library and the max is there stat.

                #Check to see which is greater and then add the win or loss.

                #Check to see if the round was one or lost by using t_wins and t_loss variables

                #if you win, add gold and one win to your stats as well as adding the room to the beaten list

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that have one the game and are now the main character.
                    #set finished game to true
                    #break
                #elif t_loss >= 3:
                    #print that they will never be the main character
                    #Set failed to true
                    #break
        #else:
            #Print You do not meet the requirments
    #return stat, finished_game, failed, to see if they have won or lost this epic fight.


#Set the loop requirments to false

#Explain the game through a print statment

#Make a loop to go through the game
#while game_finished == Fales and failed == False (These are all of the different ways to win or lose.)
    #Check to see if they have lost to many times to continue to fight, if they have, exit the loop.

    #Print a list of room numbers and there base purposes

    #print statement to ask them what room they want to go into

    #While true loop for room picking
        #Ask them what room they want to go into.

        #Check if room is valid by using .isdigit() and int()    (.isdigit() checks to see if there is a number in a sentance, int() changes that number in the sentance to just a number.)
        #else:
            #print that there input is incorrect or it has already been picked.
    #Run the fight function as well as the lose function to start the game.

    #stat, finished_game, failed = fight_room(stat, room)
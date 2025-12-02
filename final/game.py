#RC, 1st, Final game

#set the list for beaten people
#beaten = []
#set stat dictionary
#stat{ "Charm": 8,
    #  "Wisdom": 8,
    #  "Strength": 8,
    #  "Win": 0,
    #  "Lose": 0,
    #  "Gold": 0}


#Set functions

# 1st function
#def stat_increase(stat, gain):
    #if gain == crocs and stat[gold] > 1:
        #stat[charm] -= 2
        #stat[wisdom] -= 2
        #stat[strength] += 4
        #gold -=2 
        #return stat
    #elif gain == nerdy_glasses and stat[gold] > 1:
        #stat[charm] -= 2
        #stat[wisdom] += 4
        #stat[strength] -= 2
        #gold -=2 
        #return stat
    #elif gain == suit and stat[gold] > 1:
        #stat[charm] += 4
        #stat[wisdom] -= 2
        #stat[strength] -= 2
        #gold -=2 
        #return stat
    #elif gain == charm and stat[gold] > 1:
        #Charm += 2
        #Gold -= 2
        #Return stat
    #elif gain == wisdom and stat[gold] > 1:
        #wisdom += 2
        #Gold -= 2
        #Return stat
    #elif gain == strength and stat[gold] > 1:
        #strength += 2
        #Gold -= 2
        #Return stat
    #else:
        #You don't have enough money...
        #break



# 2nd function
#def lose(stat):
    #if stat[lose] == 3:
        #set end/quit to true
    #else:
        #set end/quit to false
        #pass

# 3rd function
#def fight_room(stat, room)
    #if room == 1:
        #ask them if they want to by an upgrade/item

        #def stat_increase

        #Make sure not to allow them to buy the stats multiple times.
    #elif room == 2:
        #if 2 isn't in beaten list:
            #enemy = nerd
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice = 1:
                    #attack = wisdom
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 3:
        #if 3 isn't in beaten list:
            #enemy = jock
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice == 1:
                    #attack = Strength
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 4:
        #if 4 isn't in beaten list:
            #enemy = class_clown
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice == 1:
                    #attack = wisdom
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 5:
        #if 5 isn't in beaten list:
            #enemy = Slacker
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice == 1:
                    #attack = Strength
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 6:
        #if 6 isn't in beaten list:
            #enemy = chill_guy


            #Talk about how hes such a chill guy he will always let you pick what you attack with.


            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #While True:
                    #attack = user input("What would you like to attack with").strip().upper()
                    #If attack = Wisdom or attack = Strength or attack = Charisma:
                        #Break
                    #Else:
                        #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 7:
        #if 7 isn't in beaten list:
            #enemy = Actor
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice == 1:
                    #attack = Charm
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

                #Check to see if the round was one or lost by using t_wins and t_loss
                #if t_wins >= 3:
                    #print that you have one this inconter
                    #add += 1 to stats[wins]
                    #add += 1 to stats[gold]
                    #add this room to the betean room list
                    #break
                #elif t_loss >= 3:
                    #print that they have lost the battle
                    #add += 1 to stats[lose]
                    #add this room to 'Beaten' room list
                    #break
        #else:
            #Print of thing telling the person this room has already been concured

    #elif room == 8:
        #if win >= 2:
            #enemy = student_prez
            #write out all of the enemy stats here.
            
            #t_wins = 0
            #t_wins = 0

            #While True:
                #Roll for who gets to decide the attack.
                #choice = random.randint(1,2)

                #if choice == 1:
                    #attack = Wisdom
                #else:
                    #While True:
                        #attack = user input("What would you like to attack with").strip().upper()
                        #If attack = Wisdom or attack = Strength or attack = Charisma:
                            #Break
                        #Else:
                            #Print(That is not a choice...) 

                #Set up bots stats

                #if attack == "Wisdom":
                    #chain = wisdom
                #elif attack == "Strength":
                    #chain = strength
                #else:
                    #chain = charisma

                #Set up the rolls
                #human_roll = random.randint(1, stat[attack])
                #bot roll = random.randint(1, chain)

                #Check to see which is greater and then add the win or loss.
                #if human_roll > bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #elif bot_roll > human_roll:
                    #Print(You lost this battle...)
                    #t_loss += 1
                #else:
                    #print(it was a tie)

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


#Set the loop requirments to false
#game_finished = False
#failed = False

#Explain the game through a print statment

#Make a loop to go through the flow
#while game_finished == Fales and failed == False

  #Add the finish function right here.

    #print statement to ask them what room they want to go into


    #Print a list of room numbers and there base purposes


    #While true loop for room picking
        #room = input(What room, (1-9), would you like to go through?)
        #Check if room is valid

        #if room.isdigit() == True:
            #room = int(room)
            #break
        #else:
            #print that there input is incorrect.
    
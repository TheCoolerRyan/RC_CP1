#RC, 1st, Final game

#set the list for beaten people

#set stat dictionary that will hold win lose and gold as well

#Set functions

# 1st function
#def stat_increase(stat, gain):
    #Create the stat gains for crocs, nerdy_glasses, and Suit. the first item.
        #Make sure that they must have gold and that we return new stats.
    
    #Create basic if statments to check if they wanted to pick a base stat upgrade for charm, wisdom, or strength.

# 2nd function
#def lose(stat):
    #If your lose stats are greater than 3, return true to end the game
    #else:
        #return false and keep the game going.

# 3rd function
#def fight_room(stat, room)
    #if room == 1:
        #ask them if they want to by an upgrade/item

        #def stat_increase

        #Make sure not to allow them to buy the stats multiple times.
    #elif room == 2:
        #if 2 isn't in beaten list:
            #write out all of the enemy stats here.
            
            #Set base wins and losses to 0 as variables

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
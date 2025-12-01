#RC, 1st, Final game

#set the list for beaten people
#beaten = []
#set stat dictionary
#stat{ "charm": 8,
    #  "wisdom": 8,
    #  "strength": 8,
    #  "win": 0,
    #  "lose": 0,
    #  "gold": 0}


#Set functions

# 1st function
#def stat_increase(stat):
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
#def fight(stat, room)
    #if room == 1:
        #Print out options to buy and also the base stats
        #Make sure not to allow them to buy the stats multiple times.
    #elif room == 2:
        #if 2 isin't in beaten list:
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
                #if human_roll >= bot_roll:
                    #print(you won this inconter!!!)
                    #t_win += 1
                #else:
                    #Print(You lost this battle...)
                    #t_loss += 1





        #else:
            #Print of thing telling the person this room has already been concured
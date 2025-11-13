#Set up a dictionary with all of your values for each food
menu = {"BURGER": 20.00,
        "DOUBLE_BURGER": 40.00,
        "TRIPLE_BURGER": 60.00,
        
        "COKE": 5.00,
        "DIET_COKE": 10.00,
        "ZERO_SUGAR_COKE": 20.00,
        
        "FRIES": 7.00,
        "POTATO": 5.00,
        "CARROTS": 1.00,
        "ONION_RINGS": 3.00,
        
        "NONE": 0}

#Set up dictionarys for seperate courses so they can't pick the wrong ones.
main = {"BURGER": 20.00,
        "DOUBLE_BURGER": 40.00,
        "TRIPLE_BURGER": 60.00}

drink = {"COKE": 5.00,
        "DIET_COKE": 10.00,
        "ZERO_SUGAR_COKE": 20.00}

side = {"FRIES": 7.00,
        "POTATO": 5.00,
        "CARROTS": 1.00,
        "ONION_RINGS": 3.00}

order = {"Main Course:": 0,
         "Drink:": 0,
         "Side_1": 0,
         "Side_2": 0}

#Set up the function to neatly print of my menu
def print_menu(menu):
    print("Here is the menu: ")
    #For loop to print of the key and the value one at a time
    for key, value in menu.items():
        print(f"{key}: {value:.2f}")
#Create function to calculate costs
def calculate(order, menu):
    #Set needed variables to 0
    total = 0
    #Create for loop that goes through each choice in the order
    for choice in order:
        #See if its been skipped or if its valid
        if int(menu[order[choice]]) == "NONE":
            pass
        else:
            #Calculate the total prices
            price = int(menu[order[choice]]) #Fix these problems
            total += price
    #Add tax
    total = total*1.08
    #Return cost to print later
    return total

#Create loop for ordering
while True:
    #Call the menu function to create the menu
    print_menu(menu)
    #Set variabels
    count = 1
    #Create giant for loop that will go through all order options
    for choice in order:
        #Set needed variablse
        selection = False
        #Create while loop to get the item they want and to make sure its valid
        while selection == False:
            #Get there wanted item
            item = input(f"What do you want for your {choice}? Put none if you don't want to order this.").strip().upper()
            #Loops to check if its in the correct section and that it wasn't skipped.
            if count == 1:
                if item not in main and item != "NONE":
                    pass
                #Allow to exit out of the loop
                else:
                    selection = True
            #Loops to check if its in the correct section and that it wasn't skipped.
            elif count == 2:
                if item not in drink and item != "NONE":
                    pass
                #Allow to exit out of the loop
                else:
                    selection = True
            #Loops to check if its in the correct section and that it wasn't skipped.
            elif count > 2:
                if item not in side and item != "NONE":
                    pass
                #Allow to exit out of the loop
                else:
                    selection = True
            #Allow to exit out of the loop
            else:
                selection = True
        #Setup to see if the choice was skipped so it won't break in the calculating fase.
        if item == "NONE":
            order[choice] = "NONE"
        #Otherwise add your choice to its correct catagory
        else:
            order[choice] = item
        #Increase count so it will go from one to the other, (Main Course to Drink)
        count += 1
    #Call the calculating menu to get the cost
    total = calculate(order, menu)
    #Print of everything you ordered and the cost
    for key, value in order.items():
        print(f"{key} {value}")
    print(f"Your total price is: {total:.2f}")      
    
    #Setup user input to see if they want to quit.
    quit = input("Would you like to order again? If you want to order again, please put 1. If you want to quit, please put 2.").strip().title()
    #Loops to check if they selected to quit or to go again
    if quit == "1" or quit == "One" or quit == "Uno":
        pass
    else:
        print("Lame...")
        break
menu = {"Burger": 20.00,
        "Double_Burger": 40.00,
        "Triple_Burger": 60.00,
        
        "Coke": 5.00,
        "Diet_Coke": 10.00,
        "Zero_Sugar_Coke": 20.00,
        
        "Fries": 7.00,
        "Potato": 5.00,
        "Carrots": 1.00,
        "Onion_Rings": 3.00}

main = {"Burger": 20.00,
        "Double_Burger": 40.00,
        "Triple_Burger": 60.00}

drink = {"Coke": 5.00,
        "Diet_Coke": 10.00,
        "Zero_Sugar_Coke": 20.00}

side = {"Fries": 7.00,
        "Potato": 5.00,
        "Carrots": 1.00,
        "Onion_Rings": 3.00}

order = {"Main Course:": 0,
         "Drink:": 0,
         "Side_1": 0,
         "Side_2": 0}

def print_menu(menu):
    print("Here is the menu: ")
    for key, value in menu.items():
        print(f"{key}: {value:.2f}")

def calculate(order, menu):
    total = 0
    for choice in order:
        price = int(menu[order[choice]]) #Fix these problems
        total += price
    total = total*1.08
    return total

while True:
    print_menu(menu)
    count = 1
    for choice in order:
        selection = False
        while selection == False:
            item = input(f"What do you want for your {choice}? Put skip if you don't want to order this.").strip()
            if item not in menu and item != "Skip":
                pass
            elif count == 1:
                if item not in main:
                    pass
                else:
                    selection = True
            elif count == 2:
                if item not in drink:
                    pass
                else:
                    selection = True
            elif count > 2:
                if item not in side:
                    pass
                else:
                    selection = True
            else:
                selection = True
        if item == "Skip":
            order[choice] = ""
        else:
            order[choice] = item
        count += 1
    total = calculate(order, menu)
    for key, value in order.items():
        print(f"{key} {value}")
    print(total)      #Make this prettyer
    #Add an end statement
    #Make it so its all captialized
menu = {"Burger": 20.00,
        "Double Burger": 40.00,
        "Triple Burger": 60.00,
        
        "Coke": 5.00,
        "Diet Coke": 10.00,
        "Zero Sugar Coke": 20.00,
        
        "Fries": 7.00,
        "Potato": 5.00,
        "Carrots": 1.00,
        "Onion Rings": 3.00}

order = {"Main Course:": 0,
         "Drink:": 0,
         "Side 1": 0,
         "Side 2": 0}

def print_menu(menu):
    print("Here is the menu: ")
    for key, value in menu.items():
        print(f"{key}: {value:.2f}")

def calculate(order, menu):
    total = 0
    for choice in order:
        total += menu(choice) #Fix these problems
    total = total*1.08
    return total

while True:
    print_menu(menu)
    for choice in order:
        selection = False
        while selection == False:
            item = input(f"What do you want for your {choice}? Put skip if you don't want to order this.").capitalize().strip()
            if item not in menu and item != "Skip":
                pass
            else:
                selection = True
        if item == "Skip":
            order[choice] = ""
        else:
            order[choice] = item
    total = calculate(order, menu)
    print(order)
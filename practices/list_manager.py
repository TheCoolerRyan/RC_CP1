#RC, 1st, Shopping list mannager

shopping = ["Carrot", "Pinna Colada", "Cheese"]

start = True

print("\nThis is a shopping list program that will let you manipulate your list.")
print("The things already in your list are:")
for i, item in enumerate(shopping,1):
    print(f"{i, item}")
while start == True:
    action = int(input("\nPick a number 1-4 for your action, 1 = You can add an item, 2 = You can remove an item, 3 prints of the list, 4 = Stops the program."))

    if action == 1:
        add = input("\nPick something that you would like to add to your shopping list:")
        add = add.strip().title()
        shopping.append(add)
        print(f"{add} was added!")

    elif action == 2:
        task = input("\nPick an item to remove:")
        task = task.strip().title()
        if task in shopping:
            shopping.remove(task)
            print(f"{task} was removed...")
        else:
            print("That item does not exist")
    elif action == 3:
        for i, shopping in enumerate(shopping,1):
            print(f"{i, shopping}")
    elif action == 4:
        start = False
    else:
        print("That's not an option...")
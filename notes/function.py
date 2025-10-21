#RC, 1st, Function notes

#We set variables first and the we define functions
player_health = 100
monster_health = 100
#Parameters serve as variables that only serve inside the function



def damage(amount,turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
monster_health, player_health = damage(10, "player")
print(f"Monster Health: {monster_health}")
print(f"Player Health: {player_health}")




def add(x,y):
    return x+y
#Return takes whatever is in it and replaces the arguments/function calling


def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]

    return initials

print(initials("Tia LaRose"))
print(initials("Franco Barboza"))

#Arguments go inside the function calls
#Serveds as the specific value for that specific time
total =add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("Duck")
    x +=1
print("Goose!")


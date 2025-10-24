#RC, 1st, Combate Program
import random
game = True

def user (job,health,defense,attack,damage): #Add stats to valuse
    job_selection = True
    while job_selection == True:
        job = input("What is your class? (1 if you are a Fighter, 2 if your a Mage, 3 if your a Rouge.)")
        if job == "1":
            job_selection = False
            health = 30
            defense = 14
            attack = random.randint(1,21)+3
            damage = random.randint(1,19)+4
        elif job == "2":
            job_selection = False
            health = 10
            defense = 11
            attack = random.randint(1,21)+1
            damage = random.randint(1,24)
        elif job == "3":
            job_selection = False
            health = 20
            defense = 13
            attack = random.randint(1,21)+2
            damage = random.randint(1,15)+2
        else:
            print(f"{job} isn't an option, chose again.")
    print(f"Great! Here are your stats: \nHealth: {health} \nDefense: {defense} \nAttack: {attack} \nDamage: {damage}")
    stats = [health,defense,attack,damage]
    return stats

def wolf(health2,defense2,attack2,damage2):
    "Hello"

while game == True:
    list = user("","","","","")
    health = "" #Find out how to get stats from dictionary.
    print(list)
    
#RC, 1st, Combate Program
import random
game = True
first = True
job_selection = True
attack_choice = True
damage_x2 = False
health = 0
defense = 0
attack = 0
damage = 0
def user (job,health,defense,attack,damage,job_selection): 
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
    stats = [health,defense,attack,damage, job_selection]
    return stats

def wolf(health2,defense2,attack2,damage2):
    if first == True:
        health2 = 25
        defense2 = 13
        attack2 = random.randint(1,21)
        damage2 = random.randint(1,16)
        m_stats = [health2,defense2,attack2,damage2]
    return m_stats


while game == True:
    first = True
    attacking = True
    turn = random.randint(1,3)
    job_selection = True
    print("Your being attacked by a Dire Wolf!")

    list = user("", health, defense, attack, damage, job_selection)
    job_selection = False
    health = int(list[0])
    defense = int(list[1])
    attack = int(list[2])
    damage = int(list[3])

    m_list = wolf("","","","")
    first = False
    health2 = int(m_list[0])
    defense2 = int(m_list[1])
    attack2 = int(m_list[2])
    damage2 = int(m_list[3])
    while attacking == True:
        attack = random.randint(1,21)
        damage = random.randint(1,16)
        attack2 = random.randint(1,21)
        damage2 = random.randint(1,16)
        a_choice = input("Please chose your attack: \n1. Normal Attack \n2. Wild Attack - you can double the damage but you will also take damage \n3. Drink a healing potion - regain 9 health \n4. Flee - You may or may not get away\n")
        if turn == 1:
            print("You attack first!")
            while attack_choice == True:
                if a_choice == "1":
                    attack_choice = False
                    if attack > defense2:
                        health2 = health2 - damage
                        print(f"You hit! \nThe Dire Wolf has {health2} health.")
                    else:
                        print("You didn't hit!")
                elif a_choice == "2":
                    attack_choice = False
                    if attack > defense2:
                        health2 = health2 - damage*2
                        print(f"You hit! \nThe Dire Wolf has {health2} health. Though you will take double damage...")
                        damage_x2 = True
                    else:
                        print("You didn't hit!")
                        damage_x2 = True
                elif a_choice == "3":
                    attack_choice = False
                    health +=9
                elif a_choice == "4":
                    attack_choice = False
                    run = random.randint(1,3)
                    if run == 1:
                        print("You sucsceed at exscaping!")
                        attacking = False
                    else:
                        print("You failed to escape")
                else:
                    print("That is not an option, try again.")
            print("The Dire wolf is attacking!")
            if attack2 > defense:
                print("It hits!")
                if damage_x2 == True:
                    health = health - damage2*2
                else:
                    health = health - damage
            else:
                print("It misses...")
            attack_choice = True     
        if turn == 2:
            print("The dire wolf attacks first!")
            if attack2 > defense:
                print("It hits!")
                if damage_x2 == True:
                    health = health - damage2*2
                    damage_x2 = False
                else:
                    health = health - damage
            else:
                print("It misses")
            
            while attack_choice == True:
                if a_choice == "1":
                    attack_choice = False
                    if attack > 13:
                        health2 = health2 - damage
                        print(f"You hit! \nThe Dire Wolf has {health2} health.")
                    else:
                        print("You didn't hit!")
                elif a_choice == "2":
                    attack_choice = False
                    if attack > 13:
                        health2 = health2 - damage*2
                        print(f"You hit! \nThe Dire Wolf has {health2} health. Though you will take double damage...")
                        damage_x2 = True
                    else:
                        print("You didn't hit!")
                        damage_x2 = True
                elif a_choice == "3":
                    attack_choice = False
                    health +=9
                elif a_choice == "4":
                    attack_choice = False
                    run = random.randint(1,3)
                    if run == 1:
                        print("You sucsceed at exscaping!")
                        game = False
                        break
                    else:
                        print("You failed to escape")
                else:
                    print("That is not an option, try again.")
            attack_choice = True
        if health <= 0:
            print("The dire wolf has killed you.")
            attacking = False
        elif health2 <= 0:
            print("You have killed the Dire Wolf, way to go!")    
            attacking = False
        print(f"Health: {health} \nDefense: {defense} \nAttack: {attack} \nDamage: {damage}")
    again = input("Would you like to fight again? If you want to fight all over again put 1, else put 2.")
    if again == "1":
        game = True
        print("Okay! Lets get going!")
    else:
        print("Good game.")
        game = False
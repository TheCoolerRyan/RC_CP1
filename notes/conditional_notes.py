#RC, 1st, Conditional notes
import random
player_hp = 20
player_attack = 2
player_damage = 5
player_defense = 5


monster_hp = 15
monster_attack = 3
monster_damage = 10
monster_defense = 2

hit_roll = random.randint(1,20)

if hit_roll ==20:
    print("You got a crit! That means you get to roll for damage twice!")
    damage_roll = random.randint(1,8) + random.randint(1,8) +player_damage
    print(f"You did {damage_roll-monster_defense} damage.")
    monster_hp -= (damage_roll-monster_defense)
    print(f"The monsters health is at {monster_hp}")
elif hit_roll == 1:
    print("Skill issue. You roled a 1. Womp womp.")
    damage_roll = random.randint(1,12) + monster_damage
    player_hp -= (damage_roll - player_defense)
    print(f"The monster rolled {damage_roll} damage! Your hp is now {player_hp}!")
elif hit_roll >= 12:
    print("You hit! Roll for damage!")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"You did {damage_roll-monster_defense} damage.")
        monster_hp -= (damage_roll-monster_defense)
        print(f"The monsters health is at {monster_hp}")
    else:
        print("You did no damage.")
else:
    print("You missed.")
if monster_hp <= 0:
    print("You did it! You killed the monster in one turn!")
else:
    print("You didn't kill the monster in one turn. Your turn is now over")

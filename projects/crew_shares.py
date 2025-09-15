#RC, 1st, Crew Shares

print("After there adventure the crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares.\n")

mon_earned = float(input(f"How much money did they get?\n".strip()))
mon_earned = float(f"{mon_earned:.2f}")

crew_men = int(input("How many crew members are there? (Not encluding the captin and the first mate.)\n".strip()))

calculation = int(2 + crew_men)
shares = float(f"{mon_earned / calculation:.2f}")
captin = shares*7
first_mate = shares*3
crew_need = shares-500


print(f"\nHow much was earned: {mon_earned:.2f}!")
print(f"\nHow many crew members there are: {crew_men}!")
print(f"\nThe captain gets: {captin:.2f}!")
print(f"\nThe first mate gets: {first_mate:.2f}!")
print(f"\nThe crew still needs: {crew_need:.2f}!")

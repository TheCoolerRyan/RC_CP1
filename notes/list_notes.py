#RC,1st, List Notes

import random

sibs = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jefferson", "Jake"]

print(sibs[5])
print(random.choice(sibs))
print(f"The list is {len(sibs)} people long!")
print(sibs)
sibs[0] = "Eric"
sibs[6:7] = ["Xavier", "Hailey"]
sibs.pop(3)
sibs.remove("Andrew")
#sibs.clear()
#sibs.append("Andrew")
sibs.insert(2, "Andrew")
sibs.extend(["Joseph", "Israel", "Zee"])
print(sibs)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
]

fruit = ("Apple", "Orange", "Pineapple")#Tuple ordered, not changeable

veggies = {"Spinach", "Kale", "Broccoli", "Carrot"}#set imprdered, changable
print(veggies)




#RC, 1st, For loop notes

import time

times = time.timezone
nums = [4, 346, 57, 86, 456, 35, 57, 14, 75,36346, 5743 ,34]

# For starts the loop
# Num represents the current item in the list
# Nums is the list

for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number!")
    else:
        print(num)

print("Just a spacer.")

health = 15
for num in range(1,health,2 ):
    print(num)
    time.sleep(0.5)


for num in range(20,-1, -2):
    print(num)


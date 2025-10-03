#RC, 1st, While loop

import random

num = 1
while num <= 20:
    nums = random.randint(1,20)
    print(nums)
    num += 1
else:
    print("HEllO")



goose = random.randint(1,20)
count = 0

while True:
    count += 1
    if count == goose:
        break
    else:
        print(f"{count}. Duck!")
print(f"{count}. GOOSE!!!")


i = 0

while i < 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop.")
    i += 1
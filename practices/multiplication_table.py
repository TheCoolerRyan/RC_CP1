#RC, 1st, Multiplication Table
amount = int(input("How big do you want the multiplication level?"))

mult = 1

for num in range(1, amount+1):
    for i in range(1,13):
        nums = []
        nums.insert(num*mult) #Fix
        mult += 1
    print(nums)


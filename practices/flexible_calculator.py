#RC, 1st, Flexible Calculator

print("This is a Flexible Calculator that can calculate the sum, average, max, min,  and product of what you put in.")


def nums():
    x = True
    nums = []
    while x == True:
        num = input("Pick a number. If you want to stop picking numbers, put no").strip().upper()
        if num.isdigit() != True and num != "NO":
            print("That is not a choice...")
            pass
        elif num == "NO":
            x = False
        else:
            nums.append(float(num))
            print("Here are your numbers so far:")
            for y in nums:
                print(f"{y:.2f}")
    return nums

def oper(*numbers):
    chosing = True
    while chosing == True:
        opperation = input("What operation would you like to do? (Sum, Average, Max, Min, Or Product)").strip().capitalize()
        if opperation == "Sum":
            add = sum(list(*numbers))
            print(f"The sum of your numbers is: {add:.2f}")
            chosing = False
        elif opperation == "Average":
            add = sum(list(*numbers))/len(list(*numbers))
            print(f"Your average is: {add:.2f}")
            chosing = False
        elif opperation == "Max":
            biggest = max(list(*numbers))
            print(f"The max is: {biggest:.2f}")
            chosing = False
        elif opperation == "Min":
            smallest = min(list(*numbers))
            print(f"The min is: {smallest:.2f}")
            chosing = False
        elif opperation == "Product":
            product = 1
            for num in list(*numbers):
                product *= num
            print(f"The product is: {product:.2f}")
            chosing = False
        else:
            print("That is not an option...")
            pass


while True:
    oper((i for i in nums()))
    stop = input("Do you want to do another operation? If you do, put 1, otherwise put 2 to quit.")
    if stop == "1":
        pass
    else:
        print("Okay, goodbye...")
    
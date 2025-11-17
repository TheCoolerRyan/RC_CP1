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
            nums.append(num)
        
    return nums

nums()

#RC, 1st, average grade
classes = int(input("How many classes do you have?"))
number = 0
class_number = 1
average = 0
loop = True
while loop == True:
    if number < classes:
        add = int(input(f"Whats your grade for class {class_number}?"))
        average += add
        class_number += 1
        number += 1
    else:
        print(f"{average/classes:.2f}")
        loop = False
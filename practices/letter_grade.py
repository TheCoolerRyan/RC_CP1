#RC, 1st, What is my Grade?
print("In this program you will give me your percent grade. If you do it multiple times i will average it out.")

go = True
average = 1
grades = []


while go == True:
    grade = float(input("Give me one of your grades percent."))
    grades.append(grade)

    combine = sum(grades)
    total = round(combine / average,2)      #Sum is breaking...
    average += 1

    if total >= 94:
        print(f"Your grade is {total}% Thats a A!!!")
    
    elif total >= 90:
        print(f"Your grade is {total}% Thats a A-!!")
    
    elif total >= 87:
        print(f"Your grade is {total}% Thats a B+!")
    
    elif total >= 84:
        print(f"Your grade is {total}% Thats a B!")
    
    elif total >= 80:
        print(f"Your grade is {total}% Thats a B-!")
    
    elif total >= 77:
        print(f"Your grade is {total}% Thats a C+.")
    
    elif total >= 74:
        print(f"Your grade is {total}% Thats a C.")
    
    elif total >= 70:
        print(f"Your grade is {total}% Thats a C-.")
    
    elif total >= 67:
        print(f"Your grade is {total}% Thats a D+...")
    
    elif total >= 64:
        print(f"Your grade is {total}% Thats a D...")
    
    elif total >= 60:
        print(f"Your grade is {total}% Thats a D-...")
    
    elif total >= 0:
        print(f"Your grade is {total}% Thats a F...")
    
    else:
        print("How did you mess this up?")

    stop = int(input("Do you want to stop putting in your grades? Please put 1 or 2. (1 is Yes for continuing, 2 is a No!)"))
    if stop == 1:
        go = True
        print("Yay!")
    else:
        go = False
        print("Boo 👎")



    



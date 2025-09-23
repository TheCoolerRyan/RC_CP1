#RC, 1st, What is my Grade?
print("In this program you will give me your percent grade. If you do it multiple times i will average it out.")

go = True

grades = []

while go == True:
    grade = input("Give me one of your grades percent.")
    grades.append(grade)

    average = 1
    total = sum(grades)/average      #Sum is breaking...

    average += 1



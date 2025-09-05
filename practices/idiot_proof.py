#RC, 1st, Idiot Proofing
name = input("What is your name?").strip().title()
phone1 = input("Give me the first three digits of your number").strip()
phone2 = input("Give me the next three digits of your number").strip()
phone3 = input("Give me the last four digits of your number").strip()
phone_total = (f"{phone1 [0:3]} {phone2 [0:3]} {phone3 [0:4]}")
gpa = input("What is your GPA?").strip()

print(f"Name: {name}")
print(f"NUmber: {phone_total}")
print(f"GPA: {gpa}")
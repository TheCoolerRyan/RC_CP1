#RC, 1st, Password strenght.

#import function to check for special charecters and spe_char
import re
spe_char = False
# Make the variable for the while loop.
start = True
#Explain what it is
print("This is a password checker. Your password will be checked to see if it is over or = to 8 in length, has an uppercase, has a lowercase, has a number, and if it has a special character. Each can give you one point if it is in your password. 5 is the best, 0 is the worst.")
while start == True:
    #set cap & lower & has digit to No
    cap = "No"
    lower = "No"
    len = "No"
    digit = "No"
    special = "No"
    has_digit = False
    #Set score to 0
    score = 0
    #Ask for password
    password = input("Give me a strong password.")

    #Take len() and check if password is bigger then 10
        #Add + 1 to score
    length = len(password)
    if length >= 8:
        score += 1
        len = "Yes"
    #Use .isupper() to check if there is an uppercase
        #Check if true, if true -
        # Add + 1 to score
    for char in password:
        if char.isupper():
             cap = "Yes"
    if cap == "Yes":
        score += 1
    #Use .islower() to check if there is an uppercase
        #Check if true, if true -
        #Add + 1 to score
    for char in password:
        if char.islower():
             lower = "Yes"
    if lower == "Yes":
        score += 1
    #use isdigit() to check for numbers in string
        #Check if true, if true -
        #Add + 1 to score
    for char in password:
        if char.isdigit():
            has_digit = True
    if has_digit == True:
        score += 1
        digit = "Yes"
    
    #Make a function to check for special charecters
        #Check if true, if true -
        #Add + 1 to score
        if "!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password or "_" in password or "+" in password or "-" in password or "=" in password or "[" in password or "]" in password or "{" in password or "}" in password or "|" in password or ";" in password or ":" in password or "." in password or "<" in password or ">" in password or "?" in password or "'" in password or '"' in password:
            score += 1
            special = "Yes"
    print(score)
    #Make if statement for if score =

    #Make if statement for if score =

    #Make if statement for if score =

    #Make if statement for if score =

    #Make if statement for if score =

    #Make if statement for if score =


    #If thing (legth, Upper, ...) = to 1
        # Set it to Yes
    #Else
        #SET IT TO NO

    #Display with f string of all things and if they pass or not.



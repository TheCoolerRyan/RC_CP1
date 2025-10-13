#RC, 1st, Password strenght.

#Bonus ascii arts-
Five = """
   ████████   
 ██        ██  
 ██  |  |  ██
 ██ |____| ██  
 ██        ██  
   ████████   
      ██      
    ██████    
  ██  ██  ██  
██    ██    ██
██    ██    ██
██    ██    ██
      ██      
      ██      
    ██  ██    
  ██      ██  
  ██      ██  
  ██      ██  
  ██      ██  
  ██      ██
"""
One = """
   ████████   
 ██        ██  
 ██  |  |  ██
 ██  ____  ██  
 ██ |    | ██  
   ████████   
      ██      
    ██████    
  ██  ██  ██  
██    ██    ██
██    ██    ██
██    ██    ██
      ██      
      ██      
    ██  ██    
  ██      ██  
  ██      ██  
  ██      ██  
  ██      ██  
  ██      ██
"""

# Make the variable for the while loop.
start = True
#Explain what it is
print("This is a password checker. Your password will be checked to see if it is over or = to 8 in length, has an uppercase, has a lowercase, has a number, and if it has a special character. Each can give you one point if it is in your password. 5 is the best, 0 is the worst.")
while start == True:
    #set the varibales cheecking if they get the point to No
    cap = "No"
    lower = "No"
    lens = "No"
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
        lens = "Yes"
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
    
    #Calculate if score is good.
    if score > -1 and score <= 3:
        strength = " weak..."
    elif score == 3:
        strength = " moderate."
    elif score == 4:
        strength = " strong!"
    elif score == 5:
        strength = " very strong!!!"
    else:
        strength = "... How did you do that..."
    #Telling them their scores
    print(f"Length requirement: {lens}\nUppercase requirement: {cap}\nLowercase requirement: {lower}\nNumber requirement: {digit}\nSpecial character requirement: {special}\nYour final score is {score}... \nThats{strength}")
    #Input ascyart if they have a very strong password
    if score == 5:
        print(Five)  
    #Input ascii art if they have very weak password.
    if score <= 1:
        print(One)
 #Make it possible to quit
    quit = int(input("Would you like to continue? If you want to stay, put 1, but if you want to quit, put 2."))
    if quit == 1:
        pass
    else:
        start = False
        print("Goodbye...")
        print(One)
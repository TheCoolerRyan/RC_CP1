#RC,1st,Factorial Calculator

#Creat the loop for a user inputs
while True:
    #Set input variable to true
    pick = True
    #ask user for input
    while pick == True:
        number = input("What number do you want the factorial of (Zero or above, please.): ").strip
        if number == "0":
            number = 0
            pick = False
        elif number.isdigit() == True:
            number = int(number)
            pick = False
        else:
            print("That is not an acceptable number/answer...")
            pass

    #Create if statement for 0

    #calculate the factorial

    #print of number sequence and then the sum


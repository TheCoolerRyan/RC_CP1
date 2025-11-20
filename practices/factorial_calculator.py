#RC,1st,Factorial Calculator

#Creat the loop for a user inputs
while True:
    #Set input variable to true
    pick = True
    #ask user for input
    while pick == True:
        number = input("What number do you want the factorial of (Zero or above, please.): ").strip()
        #Create if statement for 0
        if number == "0":
            number = 0
            pick = False

        elif number.isdigit() == True:
            number = int(number)
            pick = False
        else:
            print("That is not an acceptable number/answer...")
            pass
    #calculate the factorial
    one = 1
    nums = []
    if number == 0:
        print("0 = 1")
        number = 0
    while number != 0:
        nums.append(number)
        number -= 1
    if nums != []:
        one = list(map(lambda n: 1 * n, nums))
        o = 1
        for x in nums:
            o *= x
        while True:
            if number == 0:
                #print of number sequence and then the sum
                for x in nums:
                    if x != 1:
                        print(f"{x} x", end=" ")
                    else:
                        print(f"{1} = {o}")
                        number = 1
                        break
            #Make choice to see if they want to leave


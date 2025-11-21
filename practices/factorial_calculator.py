#RC, 1st, Ryan Crop

#Creat functions

#Define fuactoring(number)
def factoring(number):
    #Factorial = empty list
    factorial = []
    #For i in range(number):
    for i in range(1,number):
        #If i greater than 0:
        if i > 0:
            #Factorial.append(i)
            factorial.append(i)
        #Else:
        else:
            #Break
            break
    num = 1
    for i in factorial:
        num *= i
    #return factorial and num
    return factorial, num

#Define output(factorial):
def output(factorial,num):
    #out = ""
    out = ""
    #for i in factorial:
    for i in factorial:
        #if i > 1:
        if i != number:
            #add "F{I} x" to output
            out += (f"{i} x")
        #Else:
        else:
            #add i =
            out += (f"{i} = {num}")
    #Return out
    return out

#Define check_number(number)
def check_number(number):
    #if number.isdigit() == True
    if number.isdigit() == True:
        #return True
        return True
    #else 
    else:
        #return False
        return False


while True: ######### This spot wasn't here originally, It needed to be added to actually use the functions
    while True:
        number = input("Please put the number that you want to find the factorial of here:").strip() #Fix here
        t_f = check_number(number)
        if t_f == True:
            number = int(number)
            break
        else:
            print("That is not a number, please put a number in.")
            #########
    #Factor = (Factoring(number))
    factor, num = (factoring(number))
    #print output(factorial)
    out = output(factor, num)
    print(out)


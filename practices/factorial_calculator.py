#RC, 1st, Ryan Crop

#Creat functions

#Define fuactoring(number)
def factoring(number):
    #For i in range(number):
    for i in range(number):
        #Factorial = empty list
        factorial = []
        #If i greater than 0:
        if i > 0:
            #Factorial.append(i)
            factorial.append(i)
        #Else:
        else:
            #Break
            break
    #return factorial
    return factorial

#Define output(factorial):
def ouput(factorial):
    #out = ""
    out = ""
    #for i in factorial:
    for i in factorial:
        #if i > 1:
        if i > 1:
            #add "F{I} x" to output
            out.append(f"{i} x")
        #Else:
        else:
            #add i =
            out.append(f"{i} =")
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


while True:
    number = input("Pick the number uyou") #Fix here
    #Factor = (Factoring(number))
    factor = (factoring(number))
    #print output(factorial)
    print(output(factorial))

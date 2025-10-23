#RC, 1st, Caeser Cypher

#Set basic variables for program.
start = True
result = ""

#Define function
def translator(mode, text, shift_value):
    #reset string
    result = ""
    #Create if statement for incoding 
    if mode == 1:
        #Loop to go through each character
        for char in text:
            #Reset what you will be adding.
            add = ""
            #Check if it is a-z or A-Z
            if char.isalpha():
                #See if letters are within the lowercase values
                if ord(char) > 96 and ord(char) < 123:
                    #Change the letter to the new value
                    add = (chr(ord(char) + shift_value))
                    #Check to see if its too big/wrapping from z to a
                    if ord(add) > 122:
                        #change to number
                        add = ord(add)
                        #Change the numbers value
                        add = chr(add - 26)
                    #Check to see if its too small/wrapping from z to a
                    if ord(add) < 97:
                        #Change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add + 26)
                    #Add to the final string
                    result +=  add
                #See if letters are within the uppercase values
                if ord(char) > 64 and ord(char) < 91:
                    #Change the letter to the new value
                    add = (chr(ord(char) + shift_value))
                     #Check to see if its too big/wrapping from z to a
                    if ord(add) > 90:
                        #change to number
                        add = ord(add)
                        #Change the numbers value
                        add = chr(add - 26)
                    #Check to see if its too small/wrapping from z to a
                    if ord(add) < 65:
                        #Change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add + 26)
                    #Add to the final string
                    result +=  add
            #Check for spaces and other special characters.
            else:
                #Keep them the same and add them to the list
                result += char
    #Creat if statement for decoding
    if mode == 2:
        #Creat loop to check all leters
        for char in text:
            #Check to see if its a-z or A-Z
            if char.isalpha() and char != " ":
                #See if letters are within the uppercase values
                if ord(char) > 96 and ord(char) < 123:
                    #Change the letter to the new value
                    add = (chr(ord(char) - shift_value))
                     #Check to see if its too big/wrapping from z to a
                    if ord(add) > 122:
                        #change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add - 26)
                    #Check to see if its too small/wrapping from z to a
                    if ord(add) < 97:
                        #change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add + 26)
                    #Keep them the same and add them to the list.
                    result +=  add
                #See if letters are within the lowercase values
                if ord(char) > 64 and ord(char) < 91:
                    #Change the letter to the new value
                    add = (chr(ord(char) - shift_value))
                     #Check to see if its too big/wrapping from z to a
                    if ord(add) > 90:
                        #change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add - 26)
                    #Check to see if its too small/wrapping from z to a
                    if ord(add) < 65:
                        #change to number
                        add = ord(add)
                        #Change the absuloute value
                        add = chr(add + 26)
                    #Keep them the same and add them to the list.
                    result +=  add
            #Creat statement to check for special charectars and spaces.
            else:
                #Keep them the same and add them to the list.
                result += char
    #Brings out the value
    return result
                

#Create the loop that keeeps the program going.
while start == True:
    #Create values for loop.
    value2 = False
    value = False
    #Get the text for incoding/decodding
    text = input("Give me your sentance.")
    #Loop to make sure the mode is correctly chosen
    while value2 == False:
        #Ask for the mode via 1 or 2
        mode = int(input("Do you want to incode the sentance (1) or decode the sentance (2)? (For decoding a possitive number (1) will turn B to A)"))
        #Make so you can exit out of loop
        if mode == 1 or mode == 2:
            value2 = True
        #Otherwise you are stuck
        else:
            pass
        #Creat loop for the shift value variable.
    while value == False:
        #Ask for the shift value.
        shift_value = int(input("Give me the number you will be shifting the letters by. (Don't go over 26 or under -26!)"))
        #Check to see if its to small
        if shift_value < -26:
            print("That is to low! Please pick a number between -26 and 26!")
        #Check to see if its to big.
        elif shift_value > 26:
            print("That is to high! Please pick a number between -26 and 26!")
        #Make it so you can exit the loop.
        else:
            value = True
    #Take the function from above and add its values to get the correct sentance.
    print(translator(mode, text, shift_value))
    #Make it so you can end the entire program.
    end = int(input("Would you like to continue? If you do put 1. If you want to quit then put 2."))
    #Check to see if you chose to quit.
    if end == 2:
        #End the loop
        start = False
    #Otherwise continue onward with codding
    else:
        print("Okay!")

#Bonus resources


#Lowercase is 97 to 122
#Uppercase is 65 to 90


#Fix space problem.
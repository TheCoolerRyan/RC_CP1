#RC, 1st, Caeser Cypher
start = True
result = ""

def translator(mode, text, shift_value):
    result = ""
    if mode == 1:
        for char in text:
            if char.isalpha():
                if ord(char) > 96 and ord(char) < 123:
                    add = (chr(ord(char) + shift_value))
                    if ord(add) > 122:
                        add = ord(add)
                        add = chr(add - 26)
                    result +=  add
                if ord(char) > 64 and ord(char) < 91:
                    add = (chr(ord(char) + shift_value))
                    if ord(add) > 90:
                        add = ord(add)
                        add = chr(add - 26)
                    result +=  add
    if mode == 2:
        for char in text:
            if char.isalpha():
                if ord(char) > 96 and ord(char) < 123:
                    add = (chr(ord(char) - shift_value))
                    if ord(add) > 122:
                        add = ord(add)
                        add = chr(add + 26)
                    result +=  add
                if ord(char) > 64 and ord(char) < 91:
                    add = (chr(ord(char) - shift_value))
                    if ord(add) > 90:
                        add = ord(add)
                        add = chr(add + 26)
                    result +=  add
    return result
                


while start == True:
    text = input("Give me your sentance.")
    mode = int(input("Do you want to incode the sentance (1) or decode the sentance (2)? (For decoding a possitive number (1) will turn B to A)"))
    shift_value = int(input("Give me the number you will be shifting the letters by. (Don't go over 27!)"))
    translator(mode, text, shift_value)
    print(translator(mode, text, shift_value))
#Lowercase is 97 to 122
#Uppercase is 65 to 90

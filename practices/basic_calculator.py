#RC, 1st, Basic Calculator.
print("This is a basic calculator where you will give me two numbers and will be able to do different equations with them until you want to stop.")
number1 = int(input("Give me the first number of your wanted eqaution!".strip()))
number2 = int(input("Give me the second number of your wanted eqaution!".strip()))

start = True

while start == True:
    equation = int(input("Pick the equation you want to do (1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division, 5 = Integer Division, 6 = Modulo, and 7 = Exponents)".strip()))
    if equation == 1:
        equal = number1 + number2
        print(f"{number1} + {number2} = {equal}")
    if equation == 2:
        equal = number1 - number2
        print(f"{number1} - {number2} = {equal}")
    if equation == 3:
        equal = number1 * number2
        print(f"{number1} * {number2} = {equal}")
    if equation == 4:
        equal = number1 / number2
        print(f"{number1} / {number2} = {equal}")
    if equation == 5:
        equal = number1 // number2
        print(f"{number1} // {number2} = {equal}")
    if equation == 6:
        equal = number1 % number2
        print(f"{number1} % {number2} = {equal}")
    if equation == 7:
        equal = number1 ** number2
        print(f"{number1} ** {number2} = {equal}")
    restart = int(input("Do you want to put them in another equation? Put 1 if yes, 2 if no.".strip()))
    if restart == 1:
        print("Okay, here we go again!")
    if restart == 2:
        print("Aww, well maybe next time :(")
        start = False
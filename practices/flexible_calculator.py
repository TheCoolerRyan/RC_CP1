#RC, 1st, Flexible Calculator

print("This is a Flexible Calculator that can calculate the sum, average, max, min, and product of what you put in.")

def get_numbers():
    numbers = []
    while True:
        num = input("Pick a number. If you want to stop picking numbers, put no. ").strip()
        if num.lower() == "no":
            break
        try:
            number = float(num)
            numbers.append(number)
            print("Here are your numbers so far:")
            for y in numbers:
                print(f"{y:.2f}")
        except ValueError:
            print("That is not a valid number. Please enter a valid decimal number or 'no' to stop.")
    return numbers

def perform_operation(numbers):
    chosing = True
    while chosing:
        operation = input("What operation would you like to do? (Sum, Average, Max, Min, Or Product) ").strip().capitalize()
        if operation == "Sum":
            total = sum(numbers)
            print(f"The sum of your numbers is: {total:.2f}")
            chosing = False
        elif operation == "Average":
            if len(numbers) == 0:
                print("No numbers to calculate average.")
            else:
                avg = sum(numbers) / len(numbers)
                print(f"Your average is: {avg:.2f}")
            chosing = False
        elif operation == "Max":
            if len(numbers) == 0:
                print("No numbers to find max.")
            else:
                max_num = max(numbers)
                print(f"The max is: {max_num:.2f}")
            chosing = False
        elif operation == "Min":
            if len(numbers) == 0:
                print("No numbers to find min.")
            else:
                min_num = min(numbers)
                print(f"The min is: {min_num:.2f}")
            chosing = False
        elif operation == "Product":
            product = 1
            for num in numbers:
                product *= num
            print(f"The product is: {product:.2f}")
            chosing = False
        else:
            print("That is not an option... Please choose again.")

while True:
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered. Exiting.")
        break
    perform_operation(numbers)
    stop = input("Do you want to do another operation? If you do, put 1, otherwise put 2 to quit. ").strip()
    if stop == "1":
        pass
    else:
        print("Okay, goddbye...")

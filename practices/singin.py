#RC, 1st, User sign in
username = "James123"
password = "Clang"


username1 = input("Give me your username.").strip()
password1 = input("Give me your password.").strip()

if username == username1 and password == password1:
    print(f"Hello {username}, welcome back.")
elif username == username1 and password != password1:
    print("Your username is correct but your password is wrong.")
elif username != username1 and password == password1:
    print("Your username is incorrect but your password is wright.")
else:
    print("Wow, you got everything wrong... Thats kind of sad...")
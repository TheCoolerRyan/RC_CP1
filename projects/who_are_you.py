#RC, 1st, Who are you?
go = True
names = []
while go == True:
    name = input("What is your name?")
    if name in names:
        print(name) #Find how to find specifc word part of a bigger phrase
    else:
        fav_color = input("What is your favroite color?")
        age = input("What is your age?")
        name = (name+", " +fav_color+", and "+ age+"!" )
        names.append(name)
        
    
    

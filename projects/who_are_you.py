#RC, 1st, Who are you?
go = True
names = []
while go == True:
    name = input("What is your name?")
    if name in names:
        name1 = (name+", " +fav_color+", and "+ age+"!" )
        names.append(name1)
        print(name1) 
    else:
        fav_color = input("What is your favroite color?")
        age = input("What is your age?")
        names.append(name)
        name1 = (name+", " +fav_color+", and "+ age+"!" )
        names.append(name1)
        
    
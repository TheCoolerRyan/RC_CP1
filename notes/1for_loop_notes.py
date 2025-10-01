#RC, 1st, For loops
info = {1:"Apple","Chess": 43}


#Print all       key names    in the dictonary, one by one:
for x in info:
    print(x)


#Print all       values       in the dictionary, one by one
for x in info:
    print(info[x])


#You can also use the values() method to return values of a dictionary:
for x in info.values():
    print(x)


#You can use the keys() method to return the keys of a dictionary:
for x in info.keys():
    print(x)


#Loop through both keys and values, by using the items() method:
for x, y in info.items():
    print(x,y)


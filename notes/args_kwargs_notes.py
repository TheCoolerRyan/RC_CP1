#RC, 1st, Args and Kwargs notes

"""def hello(name = "Tia!", age = 10):
    return f"Hello {name}! Age = {age}"

print(hello())
print(hello("Vienna"))
print(hello(age = 23,name = "Xaveir"))
print(hello(age = 44))"""

def hello(*names, **kwargs):
    for n in names:
        print(f"Hello {n} {kwargs["last_name"]}!")

hello("Alex", "Andrew", "Katie", "Tia", "Treyson", "Xavier", "Jake", last_name = "LaRose", dad = "Eric", num_cats = 5)


def full_name(age,**names):
    if 'middle' in names.keys():
        return (f"{names['first']} {names['middle']} {names['last']} is {age}")
    else:
        return f"{names['first']} {names['last']} is {age}"
    
print(full_name(age = '???', first = "Koro", last = "Sensei"))
print(full_name(age = "So old", first = "Albus", middle = "Brian", last = "Dumbledore"))


def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of this story."
    if "place" in story.keys():
        sum += f"The story takes place in {story['place']}."
    if 'conflict' in story.keys():
        sum += f"The problem is {story['conflict']}."

    return sum

print(summary(name = 'Luke Skywalker', place = 'A galaxy far far away'))

print(summary(name = 'Harry Potter', conflict = 'Evil wizard wants to kill him'))
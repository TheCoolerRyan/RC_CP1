#RC, 1st, string method

subject = "Computer Programing 1!"

#print(subject.upper())
#print(subject.strip())
#print(subject.casefold())
#print(subject.format())
#print("\n" + subject.center(100))

#Stupid profing
#color = input("What is your favorite color?").strip().title()
#print(f"That is cool. I like {color} too!")

#full_name = input("What is your full name?").strip().title()
#print("That is cool {full_name}. I like {color} too!".format(full_name = full_name, color = color))

pi = "3.1415926535"

print(pi.isdecimal())
word = "jumps"
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.find(word))
start = (sentence.index(word))
length = len(word)
print(sentence[start:start + length])
print(sentence.replace(word, "swims"))
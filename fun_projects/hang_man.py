nothing1 = ""
nothing2 = ""
head = """    O""" #Create if statement to make it so head starts out as blank
body = """    |           |
    |           |
    |           |
"""
body1 = """    |           |
----|---        |
    |           |
"""
body2 = """    |           |
----|---        |
    |           |
   / \           |
  /   \           |
"""
#Make body two the full body with legs added
man = (f"""
    ____________
    |           |
    |           |
{nothing1}                |
{nothing2}                |
                |
                |
                |
                |
           _____|______




""")
print(man)
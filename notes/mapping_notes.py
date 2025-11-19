#RC, 1st, Mapping Notes
numbers = [651,247,597,25,57,376,0,52,8,25]
"""new_nums = []

for num in numbers:
    new_nums.append(num/3)"""


def divide(num):
    return num/3

new_nums = map(lambda num: num/3 ,numbers)

for num in new_nums:
    print(f"{num:.2f}")
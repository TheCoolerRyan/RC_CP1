#RC, 1st, Squared numbers
#First set the list                                                                                                                             #Set index to zero      Create function for squaring
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]; x = 0; new_nums = map(lambda num: num**2, nums)
#Create the for loop to print of the results                Increase index
for num in new_nums: print(f"Original: {nums[x]}, Squared: {num}"); x += 1
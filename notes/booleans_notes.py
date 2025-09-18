#RC, 1st, Boolean notes

import time
import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)

new_current_time = date.datetime.now()
hour = new_current_time.strftime("%H")
# To get just the hour its %H
# Minutes %M
# Weekday %A
# day %d
# montgh %B, %b for the abreviation
# month num %m
# year %Y = full year, %y for two digits
# seconds %S
over = True





print(f"Current time in secods since January 1, 1970(epoch): {current_time}")
print(f"Current time from date time: {new_current_time}")
print(f"Today is {readable_time}")
print(f"The hour is: {hour}")

print(f"The hour is saved as an integer {isinstance(hour, int)}")
print(f"The hour is saved as a float {isinstance(hour, float)}")
print(f"The hour is saved as a string {isinstance(hour, str)}")


print(f"Has a value: {bool("Ryan")}")
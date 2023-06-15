from datetime import time as t, datetime as dt

curr_hour = dt.now().time().hour
curr_min = dt.now().time().minute
curr_time = t(curr_hour, curr_min, 0, 0)
print(curr_time)

while 10 < dt.now().hour < 17:
    print("true")
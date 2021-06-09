import datetime
import pytz

x = datetime.datetime.now()

# print(x.year)
# print(x.month)
print(x.strftime("%Y/%m/%d"))

local_time = x.strftime("%H:%M:%S")

print(local_time)

# utc_time = local_time.astimezone(pytz.utc)

# print(utc_time)

print(x)
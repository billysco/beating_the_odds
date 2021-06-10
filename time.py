from string_work import start_time
from datetime import datetime, timezone

dt_now = datetime.now(tz=timezone.utc)
# dt_ts = datetime.fromtimestamp(1571595618.0, tz=timezone.utc)

# time = dt_now.strftime("%H:%M:%S")
date_time = dt_now.strftime("%Y-%m-%d %H:%M:%S")

# game_time = "2021-06-10T01:30:00Z"
current_date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
game_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
# # print(d_time)
# if game_time > current_date:
#     print("It is too late to place this bet")
print(game_time, type(game_time))
print(current_date, type(current_date))
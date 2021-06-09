from string_work import start_time
from datetime import datetime, timezone

dt_now = datetime.now(tz=timezone.utc)
# dt_ts = datetime.fromtimestamp(1571595618.0, tz=timezone.utc)

time = dt_now.strftime("%H:%M:%S")
date = dt_now.strftime("%Y-%m-%d")

game_time = "2021-06-10T01:30:00Z"
from api_call_2 import my_data
from datetime import datetime, timezone

# my_string = '{"date":"2021-06-06","league":{"id":"4353138d-4c22-4396-95d8-5f587d2df25c","name":"NBA","alias":"NBA"},"games":[{"id":"333f1cb0-0c6c-415c-8563-571d64b4cb78","status":"closed","title":"Game 1","coverage":"full","scheduled":"2021-06-06T17:00:00Z","home_points":124,"away_points":128,"track_on_court":true,"sr_id":"sr:match:27573132","reference":"0042000201","time_zones":{"venue":"US/Eastern","home":"US/Eastern","away":"US/Eastern"},"venue":{"id":"b3dca541-859e-5301-bf90-4ec677a514a9","name":"Wells Fargo Center","capacity":20478,"address":"3601 S. Broad Street","city":"Philadelphia","state":"PA","zip":"19148","country":"USA","sr_id":"sr:venue:6068"},"broadcasts":[{"network":"ABC","type":"TV","locale":"National"}],"home":{"name":"Philadelphia 76ers","alias":"PHI","id":"583ec87d-fb46-11e1-82cb-f4ce4684ea4c","seed":1,"sr_id":"sr:team:3420","reference":"1610612755"},"away":{"name":"Atlanta Hawks","alias":"ATL","id":"583ecb8f-fb46-11e1-82cb-f4ce4684ea4c","seed":5,"sr_id":"sr:team:3423","reference":"1610612737"}},{"id":"42bab9ad-76ec-4f10-bb89-e92ffefcae55","status":"unnecessary","title":"Game 7 (if necessary)","coverage":"full","scheduled":"2021-06-06T17:00:00Z","track_on_court":true,"reference":"0042000107","time_zones":{"venue":"US/Eastern","home":"US/Eastern","away":"US/Eastern"},"venue":{"id":"b3dca541-859e-5301-bf90-4ec677a514a9","name":"Wells Fargo Center","capacity":20478,"address":"3601 S. Broad Street","city":"Philadelphia","state":"PA","zip":"19148","country":"USA","sr_id":"sr:venue:6068"},"home":{"name":"Philadelphia 76ers","alias":"PHI","id":"583ec87d-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3420","reference":"1610612755"},"away":{"name":"Washington Wizards","alias":"WAS","id":"583ec8d4-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3431","reference":"1610612764"}},{"id":"93cfb372-0f31-4fbd-8fbb-b371a7673302","status":"unnecessary","title":"Game 7 (if necessary)","coverage":"full","scheduled":"2021-06-06T17:00:00Z","track_on_court":true,"reference":"0042000137","time_zones":{"venue":"US/Eastern","home":"US/Eastern","away":"US/Eastern"},"venue":{"id":"583152aa-de75-5bea-ac92-ac5b8a51f9f9","name":"Madison Square Garden","capacity":19812,"address":"4 Pennsylvania Plaza","city":"New York","state":"NY","zip":"10001","country":"USA","sr_id":"sr:venue:6054"},"home":{"name":"New York Knicks","alias":"NYK","id":"583ec70e-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3421","reference":"1610612752"},"away":{"name":"Atlanta Hawks","alias":"ATL","id":"583ecb8f-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3423","reference":"1610612737"}},{"id":"ddaf896f-e4c7-45e0-92aa-82e300cc2846","status":"unnecessary","title":"Game 7 (if necessary)","coverage":"full","scheduled":"2021-06-06T17:00:00Z","track_on_court":true,"reference":"0042000147","time_zones":{"venue":"US/Mountain","home":"US/Mountain","away":"US/Central"},"venue":{"id":"53bac75a-a667-52b5-a416-b80718ae4ed2","name":"Vivint Arena","capacity":18306,"address":"301 South Temple Street","city":"Salt Lake City","state":"UT","zip":"84101","country":"USA","sr_id":"sr:venue:6944"},"home":{"name":"Utah Jazz","alias":"UTA","id":"583ece50-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3434","reference":"1610612762"},"away":{"name":"Memphis Grizzlies","alias":"MEM","id":"583eca88-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3415","reference":"1610612763"}},{"id":"976a98e9-2bbf-4f74-8599-f23cf1ad7d24","status":"closed","title":"Game 7","coverage":"full","scheduled":"2021-06-06T19:30:00Z","home_points":126,"away_points":111,"track_on_court":true,"sr_id":"sr:match:27596140","reference":"0042000177","time_zones":{"venue":"US/Pacific","home":"US/Pacific","away":"US/Central"},"venue":{"id":"792ec100-691e-5e16-8ef8-79b2b6ee38ba","name":"Staples Center","capacity":18997,"address":"1111 S. Figueroa Street","city":"Los Angeles","state":"CA","zip":"90015","country":"USA","sr_id":"sr:venue:6008"},"broadcasts":[{"network":"ABC","type":"TV","locale":"National"}],"home":{"name":"LA Clippers","alias":"LAC","id":"583ecdfb-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3425","reference":"1610612746"},"away":{"name":"Dallas Mavericks","alias":"DAL","id":"583ecf50-fb46-11e1-82cb-f4ce4684ea4c","sr_id":"sr:team:3411","reference":"1610612742"}}]}'
my_string = str(my_data)
# Code for home score
z = str(my_string.split('"away_points":')[0])

# print(z[-4:-1])
home_score = z[-4:-1]
print(home_score)

# Code for away score
x = str(my_string.split('"track_on_court":')[0])

# print(x[-4:-1])
away_score = x[-4:-1]
print(away_score)

# code for home team name
home_index = my_string.find('"home":{"name":')
# print(home_index)
home_index_end = home_index+100
# print(home_index_end)
home_string = my_string[home_index:home_index_end]
# print(home_string)
home_team = str(home_string.split('"id"')[0])
home_name = home_team[-5:-2]
print(home_name)

# code for away team name
away_index = my_string.find('"away":{"name":')
away_index_end = away_index+100
away_string = my_string[away_index:away_index_end]
away_team = str(away_string.split('"id"')[0])
away_name = away_team[-5:-2]
print(away_name)

start_time_index = str(my_string.split('","track_on_court"')[0])
start_time = start_time_index[-20:-1]
print(start_time)

dt_now = datetime.now(tz=timezone.utc)
# dt_ts = datetime.fromtimestamp(1571595618.0, tz=timezone.utc)

# time = dt_now.strftime("%H:%M:%S")
date_time = dt_now.strftime("%Y-%m-%d %H:%M:%S")

# game_time = "2021-06-10T01:30:00Z"
current_date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
game_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
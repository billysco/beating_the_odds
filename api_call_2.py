import http.client
import datetime
import os
from dotenv import load_dotenv
import json
from collections import defaultdict
import re

# Load .env variables
load_dotenv()

# Set today's date
x = datetime.datetime.now()

sportradar_api_key = os.getenv('Sportradar_api_key')

# format the date for the API call
y = (x.strftime("%Y/%m/%d"))

conn = http.client.HTTPSConnection("api.sportradar.us")

# TODO: Uncomment the line below this for the current date
conn.request("GET", f"/nba/trial/v7/en/games/{y}/schedule.json?api_key={sportradar_api_key}") 
# conn.request("GET", f"/nba/trial/v7/en/games/2021/06/06/schedule.json?api_key={sportradar_api_key}") # THIS IS FOR TESTING ONLY NOT CURRENT DATE

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))
my_data = data.decode("utf-8")

print(my_data)
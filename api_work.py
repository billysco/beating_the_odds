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
# conn.request("GET", f"/nba/trial/v7/en/games/{y}/schedule.json?api_key={sportradar_api_key}") 
conn.request("GET", f"/nba/trial/v7/en/games/2021/06/06/schedule.json?api_key={sportradar_api_key}") # THIS IS FOR TESTING ONLY NOT CURRENT DATE

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))
my_data = data.decode("utf-8")
# print(data[15])


# PATTERN = '''
#     \s*                         # Any amount of space
#     (home_points|away_points)   # Capture person
#     :\s                         # Colon and single space
#     (.*?)                       # Capture everything, non-greedy
#     (?=\shome_points:|\saway_points:|$) # Until we find following person or end of string
# '''
# s = "  home_points: *random words* away_points: *random words* home_points: *random words* away_points: *random words*"
# res = defaultdict(list)
# for person, message in re.findall(PATTERN, s, re.VERBOSE):
#     res[person].append(message)

# print res['home_points']
# print res['away_points']



# home_score = my_data["games"][5]
# scores = my_data[250:450]

# home_score = scores[9:12]

# away_score = scores[27:30]


# print(home_score, away_score)
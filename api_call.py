import os
import requests
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from functions import get_balance, place_bet_on_team_1, place_bet_on_team_2

# url = "https://api-nba-v1.p.rapidapi.com/seasons/"

# headers = {
#     'x-rapidapi-key': "203552ca96msheaefa34140ffcb4p106269jsnd1a86cee97e8",
#     'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

# Step 1, get data from API
# Step 2, display data and give option to bet on either team
# Step 3, display the amount of current bets on both teams
# Step 3 cont, write code to pay winners based on their % cont to pot
# Step 4, ability to connect ether wallets (metamask if possible)
# Step 5, get winner of game with api
# Step 6, pay winners with their stake from loser's pool 



# Stramlit code
st.header('Welcome to Beating the Odds!')

st.text('Place Your Bets with the Options Below')


# Make the pools for both teams
team1_pool = 0
team2_pool = 0

# Sidebar
st.sidebar.markdown("## Betting Slip")


# Take bets
bet_1 = st.sidebar.number_input('How much would you like to bet on team 1?')
bet_2 = st.sidebar.number_input('How much would you like to bet on team 2?')

# Add the bets to the bet pool
team1_pool += bet_1
team2_pool += bet_2

# Display the current pools to the user
st.text(f'The current prize pool for team 1 is {team1_pool}')
st.text(f'The current prize pool for team 2 is {team2_pool}')




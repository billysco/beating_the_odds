from datetime import datetime, timedelta
import os
import requests
import streamlit as st
from dotenv import load_dotenv
import web3
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from functions import get_balance, generate_account, payout_team_1, payout_team_2, place_bet_on_team_1, place_bet_on_team_2
from string_work import home_score, away_score, home_name, away_name, start_time, current_date, game_time
# from time import current_date, game_time

# Set variables for pools
team1_pool = 0
team2_pool = 0
over_pool = 0
under_pool = 0

# Stramlit code
st.header('Welcome to Beating the Odds!')

st.header('Place Your Bets with the Options on the Left')

st.header("Today's Games")
# st.header(f'{home_name} versus {away_name} at {start_time}')
st.header(f'{home_name} versus {away_name} at 2021-06-10 23:30:00')

# Sidebar
user_address = st.sidebar.text_input('Please enter your Ethereum wallet address')
st.sidebar.markdown("## Betting Slip")


# Take bets
bet_1 = st.sidebar.number_input(f'How much would you like to bet on {home_name}?')
bet_2 = st.sidebar.number_input(f'How much would you like to bet on {away_name}?')


# user_account = st.sidebar.text_input('Please enter your Ethereum wallet address')
# my_variable = generate_account('9042d38fd16a9a3d65bfd6dbfde438a44aa2033090ba23cb7d3f9eda0a21a9b4')
# user_account = generate_account('0x6b8cc206BAf6Db1255aa5fff27012e19525e0be2')

pool_1_address = '0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'
pool_2_address = '0x952c588d083c71e20944693602d0584aF66062EF'
pool_1_pk = '0c19e6356046978b468c5aa16df87e1364a021e903b9617c6033bb54424c82f1'
pool_2_pk = '4cb0982b65ac5ec6580592b3976937db1bd279349deb79db509148c3f0c553c0'


# print(web3.eth.account.privateKeyToAccount('0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'))
# print(web3.eth.getAccounts('0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'))

# Call the function to add funds to the betting pool
if st.sidebar.button(f'Place my bet on {home_name}'):
    if current_date > game_time:
        st.sidebar.text('This event has already started')
    else:
        user_account = generate_account(user_address)
        place_bet_on_team_1(user_account, pool_2_address, bet_1)
        team1_pool += bet_1

if st.sidebar.button(f'Place my bet on {away_name}'):
    if current_date > game_time:
        st.sidebar.text('This event has already started')
    else:
        user_account = generate_account(user_address)
        place_bet_on_team_1(user_account, pool_2_address, bet_2)
        team2_pool += bet_2


over_bet = st.sidebar.number_input('How much would you like to bet on Over 200.5?')
under_bet = st.sidebar.number_input('How much would you like to bet on Under 200.5?')
if st.sidebar.button(f'Place my bet on Over'):
    if current_date > game_time:
        st.sidebar.text('This event has already started')
    else:
        user_account = generate_account(user_address)
        place_bet_on_team_1(user_account, pool_1_address, over_bet)
        over_pool += over_bet

if st.sidebar.button(f'Place my bet on Under'):
    if current_date > game_time:
        st.sidebar.text('This event has already started')
    else:
        user_account = generate_account(user_address)
        place_bet_on_team_1(user_account, pool_1_address, bet_2)
        under_pool += under_bet



# Display the current pools to the user
st.text(f'The current prize pool for {home_name} is {team1_pool}')
st.text(f'The current prize pool for {away_name} is {team2_pool}')

# Set prize pools
current_prize_pool = team1_pool + team2_pool
current_prize_pool_2 = over_pool + under_pool

st.text(f'The total prize pool is {current_prize_pool}')

st.header('All NBA over/unders are set at 200.5')
st.text(f'The current prize pool for over is {over_pool}')
st.text(f'The current prize pool for under is {under_pool}')
st.text(f'The total prize pool is {current_prize_pool_2}')




# Set payouts five hours after game starts
payout_time = game_time + timedelta(hours=4)


if current_date == payout_time:
    if home_score > away_score:
        payout_team_1(pool_2_pk, user_address, bet_1, team1_pool, current_prize_pool)
    else:
        payout_team_2(pool_2_pk, user_address, bet_2, team2_pool, current_prize_pool)
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
from functions import get_balance, generate_account # place_bet_on_team_1, place_bet_on_team_2
from string_work import home_score, away_score, home_name, away_name, start_time

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
# Make the pools for both teams

team1_pool = 0
team2_pool = 0



def place_bet_on_team_1(account, to, amount): 
    """Send the user's funds to the account for the first team"""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(amount, "ether")

    # Convert eth amount to Wei
    value = w3.toWei(amount, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": w3.eth.generateGasPrice(),
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)



def place_bet_on_team_2(account, to1, amount): 
    """Send the user's funds to the account for the second team"""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(amount, "ether")

    # Convert eth amount to Wei
    value = w3.toWei(amount, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to1, "from": account, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to1,
        "from": account,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": w3.eth.generateGasPrice(),
        "nonce": w3.eth.getTransactionCount(account)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)


# Stramlit code
st.header('Welcome to Beating the Odds!')

st.header('Place Your Bets with the Options on the Left')

st.text("Today's Games")
st.text(f'{home_name} versus {away_name} at {start_time}')


# Sidebar
st.sidebar.markdown("## Betting Slip")


# Take bets
bet_1 = st.sidebar.number_input(f'How much would you like to bet on {home_name}?')
bet_2 = st.sidebar.number_input(f'How much would you like to bet on {away_name}?')

user_address = st.sidebar.text_input('Please enter your Ethereum wallet address')
# user_account = st.sidebar.text_input('Please enter your Ethereum wallet address')
# my_variable = generate_account('9042d38fd16a9a3d65bfd6dbfde438a44aa2033090ba23cb7d3f9eda0a21a9b4')
# user_account = generate_account('0x6b8cc206BAf6Db1255aa5fff27012e19525e0be2')

pool_1_address = '0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'
pool_2_address = '0x952c588d083c71e20944693602d0584aF66062EF'

# print(web3.eth.account.privateKeyToAccount('0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'))
# print(web3.eth.getAccounts('0x454C8dba0f11797B296324C5cb97CF73B19cf0dB'))

# Call the function to add funds to the betting pool
if st.sidebar.button('Place my bet on team 1'):
    user_account = generate_account(user_address)
    place_bet_on_team_1(user_account, pool_1_address, bet_1)
    team1_pool += bet_1

if st.sidebar.button('Place my bet on team 2'):
    user_account = generate_account(user_address)
    place_bet_on_team_1(user_account, pool_2_address, bet_2)
    team2_pool += bet_2

# Display the current pools to the user
st.text(f'The current prize pool for {home_name} is {team1_pool}')
st.text(f'The current prize pool for {away_name} is {team2_pool}')


current_prize_pool = team1_pool + team2_pool
st.text(f'The total prize pool is {current_prize_pool}')

@st.cache(allow_output_mutation=True)
def load_contract():
    
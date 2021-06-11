# beating_the_odds
A completely decentralized sports predictions application

## Motivation
![revenue_graphic](!insert link here)
The current gambling market is is valued at approximately $533 billion and all that revenue comes from people losing money to gambling institutions. This product aims to solve that problem by creating an application which allows users to recieve 100% (minus Ethereum gas fees) of the prize pool money. 

## Usage
![usage_video](!insert link)
To use the product, the user starts by entering their account address. After that they can choose which game or games to bet on. Then they enter the amount, in ether, that they want to bet on a specific team, then click place my bet. After a few minutes, the transaction will process and they can see the prize pools increase on the right (takes time to process on testnet/mainnet). Then, if their team wins, after the game, they'll recieve the funds in ether (the money they bet + their percent of the losers' pool).  Additionally, we added the option to bet on the over/under of the games, this works in the same way as betting on the outcome, but the user would place their bet on whether the teams combined scores will be over or under a specific number. 

## Technologies used
This product was developed with Python and Solidity. The web3 connection is done with the web3 library and the frontend application is done with streamlit.
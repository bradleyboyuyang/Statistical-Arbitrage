# StatisticalArbitrage
 Implementation sample for high-frequency statistical arbitrage


# Statistical Arbitrage

This repository includes the Notebook, which entails the data analysis and algorithm(s), a seperate python 
file that is used to do the Engle-Granger cointegration test and a datafile. 

The key to success in pairs trading lies in the identification of security pairs (Vidyamurthy, 2004). 
Therefore, first an analysis on the data provided is done in order to determine which pairs of stocks can 
be traded profitably. Thereafter, implement and backtest a trading strategy to trade the selected pairs. 


# Option Arbitrage

This project includes the Notebook, which entails identifying arbitrage opportunities and acting on them,
a seperate Python file used to perform the Black Scholes calculations and a datafile.

The options and stocks can be mispriced relative to each other (Black Scholes), and if you trade on this 
arbitrage correctly there is (small) margin to be made. Arbitrage options trading is a market-neutral strategy 
that seeks to neutralize certain market risks by taking offsetting long and short related securities.


# Dual Listing Arbitrage

A Project to identify arbitrage opportunities between two stock exchanges trading the same stock. 
The algorithm searches for the possibility of a mismatch and trades on it. Next to that, 
it takes into account certain limits, which is set to a max position of 250 to 
prevent massive losses if the algorithm malfunctions.

It requires specific datasets as added in the directory. 
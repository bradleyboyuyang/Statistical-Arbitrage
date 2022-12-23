# StatisticalArbitrage
 Implementation sample for high-frequency statistical arbitrage


## Scripts
- `pairs_trading.ipynb`: notebook for realizing pair trading based on limit orderbook stock data
- `utils`: tools used for statistical models
- `models`: realizations and simulations for stochastic models and option greeks


**1. Pairs Trading**

The key to success in pairs trading lies in the identification of security pairs (Vidyamurthy, 2004). 
Therefore, first an analysis on the data provided is done in order to determine which pairs of stocks can 
be traded profitably. Thereafter, implement and backtest a trading strategy to trade the selected pairs. 


**2. Option Arbitrage**

The options and stocks can be mispriced relative to each other (Black Scholes), and if you trade on this 
arbitrage correctly there is (small) margin to be made. Arbitrage options trading is a market-neutral strategy 
that seeks to neutralize certain market risks by taking offsetting long and short related securities.


**3. Dual Listing Arbitrage**

Identify arbitrage opportunities between two stock exchanges trading the same stock. 
The algorithm searches for the possibility of a mismatch and trades on it. Next to that, 
it takes into account certain limits, which is set to a max position of 250 to 
prevent massive losses if the algorithm malfunctions.
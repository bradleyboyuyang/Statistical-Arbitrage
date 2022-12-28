# Statistical-Arbitrage
In this project we provide a backtesting pipeline for intraday statistical arbitrage. Both traditional spread models (i.e. pairs trading with cointegration tests, time series analysis) and continuous time trading models (i.e. Ornstein-Uhlenbeck process) are used to model the spread portfolios.

## Scripts
- `data`: intraday data files, including stocks, options, and dual listing stocks
- `utils`: arbitrage tool functions including cointegration tests and regression analysis
- `models`: simulations and parameter estimations for stochastic models and option greeks
- `statistical_arbitrage.ipynb`: notebook for realizing pair trading based on limit orderbook stock data

<img src=".//pipline.png" width="650">
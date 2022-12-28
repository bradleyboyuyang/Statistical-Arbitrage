from scipy import stats
import numpy as np

_norm_cdf = stats.norm(0, 1).cdf
_norm_pdf = stats.norm(0, 1).pdf

def gbm(S, T, r, sigma):
    return S*np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T)*np.random.normal())


def _d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))


def _d2(S, K, T, r, sigma):
    return _d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def call_value(S, K, T, r, sigma):
    '''
    The fair value of a call option paying max(S_T-K, 0) at expiry, under the Black-scholes model,
    for an option with strike <K>, expiring in <T> years, under a fixed interest rate <r>,
    a stock volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The current value of the underlying stock (S0).
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    call_value : float
        The fair present value of the option.
        
    '''
    
    return S * _norm_cdf(_d1(S, K, T, r, sigma)) - K * np.exp(-r * T) * _norm_cdf(_d2(S, K, T, r, sigma))


def put_value(S, K, T, r, sigma):
    '''
    The fair value of a put option paying max(K-S_T, 0) at expiry, under the Black-scholes model,
    for an option with strike <K>, expiring in <T> years, under a fixed interest rate <r>,
    a stock volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The value of the underlying stock (S0).
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    put_value : float
        The fair present value of the option.
    '''
    
    return np.exp(-r * T) * K * _norm_cdf(-_d2(S, K, T, r, sigma)) - S * _norm_cdf(-_d1(S, K, T, r, sigma))


def call_delta(S, K, T, r, sigma):
    '''
    The delta, i.e. the first derivative of the option value with respect to the underlying, 
    of a call option paying max(S_T-K, 0) at expiry, under the Black-scholes model, for an option 
    with strike <K>, expiring in <T> years, under a fixed interest rate <r>, a stock 
    volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The value of the underlying stock.
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    call_delta : float
        The fair present value of the option.   
    '''
    
    # return _norm_cdf(_d1(S, K, T, r, sigma))
    S_T = gbm(S, T, r, sigma)
    return max(S_T-K, 0)*np.exp(-r*T)*S_T/S


def put_delta(S, K, T, r, sigma):
    '''
    The delta, i.e. the first derivative of the option value with respect to the underlying, 
    of a put option paying max(K-S_T, 0) at expiry, under the Black-scholes model, for an option 
    with strike <K>, expiring in <T> years, under a fixed interest rate <r>, a stock 
    volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The value of the underlying stock.
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    put_delta : float
        The fair present value of the option.   
    '''
    
    # return call_delta(S, K, T, r, sigma) - 1
    S_T = gbm(S, T, r, sigma)
    return max(K-S_T, 0)*np.exp(-r*T)*S_T/S


def call_vega(S, K, T, r, sigma):
    '''
    The vega, i.e. the derivative of the option value with respect to the volatility, 
    of a call option paying max(S-K, 0) at expiry, under the Black-scholes model, for an option 
    with strike <K>, expiring in <T> years, under a fixed interest rate <r>, a stock 
    volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The value of the underlying stock.
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    call_delta : float
        The fair present value of the option.   
    '''
    
    # return S * _norm_pdf(_d1(S, K, T, r, sigma)) * np.sqrt(T)
    S_T = gbm(S, T, r, sigma)
    return max(S_T-K, 0)*np.exp(-r*T)*S_T*((np.log(S_T/S)-(r+0.5*sigma**2)*T)/sigma)


def put_vega(S, K, T, r, sigma):
    '''
    The vega, i.e. the derivative of the option value with respect to the volatility, 
    of a put option paying max(K-S, 0) at expiry, under the Black-scholes model, for an option 
    with strike <K>, expiring in <T> years, under a fixed interest rate <r>, a stock 
    volatility <sigma>, and when the current price of the underlying stock is <S>.
        
    Parameters
    ----------
    S : float
        The value of the underlying stock.
    
    K : float
        The strike price of the option.
        
    T : float
        Time to expiry in years.
    
    r : float
        The fixed interest rate valid between now and expiry.
    
    sigma : float
        The volatility of the underlying stock process.
    
    Returns
    -------
    call_delta : float
        The fair present value of the option.   
    '''
    
    # return call_vega(S, K, T, r, sigma)
    S_T = gbm(S, T, r, sigma)
    return max(K-S_T, 0)*np.exp(-r*T)*S_T*((np.log(S_T/S)-(r+0.5*sigma**2)*T)/sigma)
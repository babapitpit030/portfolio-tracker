"""
Utility for fetching current and historical price data.
"""
import yfinance as yf
import pandas as pd
from typing import Optional, Tuple, List


class DataFetcher:
    """Fetches current and historical price data for assets."""
    
    @staticmethod
    def get_current_price(ticker: str) -> Optional[float]:
        """Get the current price for a ticker."""
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            if not data.empty:
                return data['Close'].iloc[-1]
        except Exception as e:
            print(f"Error fetching current price for {ticker}: {e}")
        return None
    
    @staticmethod
    def get_historical_prices(ticker: str, period: str = "1y") -> Optional[pd.Series]:
        """Get historical prices for a ticker."""
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period=period)
            if not data.empty:
                return data['Close']
        except Exception as e:
            print(f"Error fetching historical data for {ticker}: {e}")
        return None
    
    @staticmethod
    def get_multiple_historical_prices(tickers: List[str], period: str = "1y") -> pd.DataFrame:
        """Get historical prices for multiple tickers."""
        data = {}
        for ticker in tickers:
            prices = DataFetcher.get_historical_prices(ticker, period)
            if prices is not None:
                data[ticker] = prices
        return pd.DataFrame(data)
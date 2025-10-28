"""
Utility functions for financial calculations.
"""
import numpy as np
import pandas as pd
from typing import Dict, List


class PortfolioCalculations:
    """Handles various portfolio calculations."""
    
    @staticmethod
    def calculate_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
        """Calculate daily returns from price data."""
        return prices.pct_change().dropna()
    
    @staticmethod
    def calculate_cumulative_returns(returns: pd.DataFrame) -> pd.DataFrame:
        """Calculate cumulative returns from daily returns."""
        return (1 + returns).cumprod()
    
    @staticmethod
    def calculate_volatility(returns: pd.DataFrame) -> Dict[str, float]:
        """Calculate annualized volatility for each asset."""
        volatility = {}
        for column in returns.columns:
            volatility[column] = returns[column].std() * np.sqrt(252)  # Annualized
        return volatility
    
    @staticmethod
    def normalize_prices(prices: pd.DataFrame) -> pd.DataFrame:
        """Normalize prices to start at 100 for better comparison."""
        return (prices / prices.iloc[0]) * 100
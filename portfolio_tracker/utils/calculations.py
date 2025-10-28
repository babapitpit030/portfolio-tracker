"""
Utility functions for financial calculations.
"""
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt


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
    
    @staticmethod
    def calculate_annual_returns(returns: pd.DataFrame) -> Dict[str, float]:
        """Calculate annualized returns for each asset."""
        annual_returns = {}
        for column in returns.columns:
            # Annualize the mean daily return
            annual_returns[column] = (1 + returns[column].mean()) ** 252 - 1
        return annual_returns
    
    @staticmethod
    def geometric_brownian_motion_simulation(
        current_price: float,
        mu: float,
        sigma: float,
        years: int = 15,
        num_paths: int = 100000,
        time_steps_per_year: int = 252
    ) -> np.ndarray:
        """
        Simulate future price paths using Geometric Brownian Motion.
        
        Formula: S_{t+1} = S_t * exp((μ - 0.5*σ²)Δt + σ√Δt * Z)
        Where Z ~ N(0,1)
        
        Parameters:
        - current_price: Current price of the asset
        - mu: Annual expected return (drift)
        - sigma: Annual volatility
        - years: Number of years to simulate
        - num_paths: Number of simulation paths
        - time_steps_per_year: Time steps per year (daily = 252)
        
        Returns:
        - Array of shape (time_steps, num_paths) with simulated prices
        """
        # Time parameters
        total_time_steps = years * time_steps_per_year
        dt = 1 / time_steps_per_year  # Time step in years
        
        # Initialize price matrix
        prices = np.zeros((total_time_steps, num_paths))
        prices[0] = current_price
        
        # GBM parameters
        drift = (mu - 0.5 * sigma ** 2) * dt
        volatility = sigma * np.sqrt(dt)
        
        # Generate random shocks
        random_shocks = np.random.standard_normal((total_time_steps - 1, num_paths))
        
        # Simulate price paths
        for t in range(1, total_time_steps):
            prices[t] = prices[t-1] * np.exp(drift + volatility * random_shocks[t-1])
        
        return prices
    
    @staticmethod
    def portfolio_gbm_simulation(
        portfolio_assets: List[Tuple[str, float, float, float]],
        years: int = 15,
        num_paths: int = 100000
    ) -> Dict[str, np.ndarray]:
        """
        Simulate GBM for multiple assets in a portfolio.
        
        Parameters:
        - portfolio_assets: List of (ticker, current_price, mu, sigma) tuples
        - years: Simulation years
        - num_paths: Number of paths
        
        Returns:
        - Dictionary with ticker -> simulated paths
        """
        simulations = {}
        
        for ticker, current_price, mu, sigma in portfolio_assets:
            simulations[ticker] = PortfolioCalculations.geometric_brownian_motion_simulation(
                current_price=current_price,
                mu=mu,
                sigma=sigma,
                years=years,
                num_paths=num_paths
            )
        
        return simulations
    
    @staticmethod
    def calculate_simulation_statistics(simulated_prices: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Calculate statistics from simulated price paths.
        
        Returns:
        - Dictionary with 'mean', 'median', 'percentile_5', 'percentile_95', 'percentile_25', 'percentile_75'
        """
        return {
            'mean': np.mean(simulated_prices, axis=1),
            'median': np.median(simulated_prices, axis=1),
            'percentile_5': np.percentile(simulated_prices, 5, axis=1),
            'percentile_25': np.percentile(simulated_prices, 25, axis=1),
            'percentile_75': np.percentile(simulated_prices, 75, axis=1),
            'percentile_95': np.percentile(simulated_prices, 95, axis=1)
        }
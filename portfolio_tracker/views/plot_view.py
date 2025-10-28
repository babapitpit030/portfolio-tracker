"""
View component for creating graphs and visualizations.
"""
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Optional, Dict
import numpy as np


class PlotView:
    """Handles creation of graphs and visualizations."""
    
    @staticmethod
    def plot_historical_prices(prices: pd.DataFrame, title: str = "Historical Prices") -> None:
        """Plot historical prices for one or multiple assets."""
        plt.figure(figsize=(12, 6))
        
        for column in prices.columns:
            plt.plot(prices.index, prices[column], label=column, linewidth=2)
        
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_normalized_prices(prices: pd.DataFrame, title: str = "Normalized Prices (Base=100)") -> None:
        """Plot normalized prices starting from 100."""
        normalized_prices = (prices / prices.iloc[0]) * 100
        
        plt.figure(figsize=(12, 6))
        for column in normalized_prices.columns:
            plt.plot(normalized_prices.index, normalized_prices[column], label=column, linewidth=2)
        
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Normalized Price (Base=100)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_portfolio_weights(weights: Dict[str, float], title: str = "Portfolio Weights") -> None:
        """Plot portfolio weights as a pie chart."""
        if not weights:
            print("No data to plot")
            return
        
        plt.figure(figsize=(10, 8))
        labels = list(weights.keys())
        sizes = list(weights.values())
        
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(title, fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_sector_allocation(sector_weights: Dict[str, float]) -> None:
        """Plot sector allocation as a bar chart."""
        if not sector_weights:
            print("No data to plot")
            return
        
        plt.figure(figsize=(12, 6))
        sectors = list(sector_weights.keys())
        weights = list(sector_weights.values())
        
        plt.bar(sectors, weights, color='skyblue', alpha=0.7)
        plt.title('Sector Allocation', fontsize=14, fontweight='bold')
        plt.xlabel('Sector')
        plt.ylabel('Weight (%)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.show()
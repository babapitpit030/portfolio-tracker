"""
View component for creating graphs and visualizations.
"""
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Optional, Dict, Any
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
    
    @staticmethod
    def plot_gbm_simulation(
        simulated_prices: np.ndarray,
        ticker: str,
        years: int = 15,
        show_paths: bool = True,
        num_sample_paths: int = 100
    ) -> None:
        """
        Plot GBM simulation results for a single asset.
        
        Parameters:
        - simulated_prices: Array of simulated prices (time_steps, num_paths)
        - ticker: Asset ticker for title
        - years: Simulation period in years
        - show_paths: Whether to show individual sample paths
        - num_sample_paths: Number of sample paths to display
        """
        time_steps = simulated_prices.shape[0]
        time_points = np.linspace(0, years, time_steps)
        
        # Calculate statistics
        stats = {
            'mean': np.mean(simulated_prices, axis=1),
            'median': np.median(simulated_prices, axis=1),
            'percentile_5': np.percentile(simulated_prices, 5, axis=1),
            'percentile_95': np.percentile(simulated_prices, 95, axis=1)
        }
        
        plt.figure(figsize=(14, 8))
        
        # Plot sample paths (transparent)
        if show_paths and num_sample_paths > 0:
            # Select random sample of paths
            sample_indices = np.random.choice(simulated_prices.shape[1], 
                                            min(num_sample_paths, simulated_prices.shape[1]), 
                                            replace=False)
            for i in sample_indices:
                plt.plot(time_points, simulated_prices[:, i], 
                        color='lightgray', alpha=0.1, linewidth=0.5)
        
        # Plot statistics
        plt.plot(time_points, stats['mean'], 'b-', linewidth=2, label='Mean')
        plt.plot(time_points, stats['median'], 'r--', linewidth=2, label='Median')
        plt.fill_between(time_points, stats['percentile_5'], stats['percentile_95'], 
                        alpha=0.3, color='orange', label='90% Confidence Interval')
        
        plt.title(f'GBM Simulation: {ticker} - {years} Year Forecast\n(100,000 Paths)', 
                 fontsize=14, fontweight='bold')
        plt.xlabel('Years')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_multiple_gbm_simulations(
        simulations: Dict[str, np.ndarray],
        years: int = 15
    ) -> None:
        """
        Plot GBM simulations for multiple assets in separate subplots.
        
        Parameters:
        - simulations: Dictionary with ticker -> simulated prices
        - years: Simulation period
        """
        num_assets = len(simulations)
        fig, axes = plt.subplots(num_assets, 1, figsize=(14, 5 * num_assets))
        
        if num_assets == 1:
            axes = [axes]
        
        time_steps = list(simulations.values())[0].shape[0]
        time_points = np.linspace(0, years, time_steps)
        
        for idx, (ticker, prices) in enumerate(simulations.items()):
            ax = axes[idx]
            
            # Calculate statistics
            stats = {
                'mean': np.mean(prices, axis=1),
                'median': np.median(prices, axis=1),
                'percentile_5': np.percentile(prices, 5, axis=1),
                'percentile_95': np.percentile(prices, 95, axis=1)
            }
            
            # Plot sample paths (transparent)
            sample_indices = np.random.choice(prices.shape[1], min(50, prices.shape[1]), replace=False)
            for i in sample_indices:
                ax.plot(time_points, prices[:, i], color='lightgray', alpha=0.1, linewidth=0.5)
            
            # Plot statistics
            ax.plot(time_points, stats['mean'], 'b-', linewidth=2, label='Mean')
            ax.plot(time_points, stats['median'], 'r--', linewidth=2, label='Median')
            ax.fill_between(time_points, stats['percentile_5'], stats['percentile_95'], 
                           alpha=0.3, color='orange', label='90% CI')
            
            ax.set_title(f'{ticker} - 15 Year GBM Forecast (100,000 Paths)', fontsize=12, fontweight='bold')
            ax.set_xlabel('Years')
            ax.set_ylabel('Price ($)')
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_final_value_distribution(simulated_prices: np.ndarray, ticker: str) -> None:
        """
        Plot distribution of final portfolio values.
        
        Parameters:
        - simulated_prices: Array of simulated prices
        - ticker: Asset ticker
        """
        final_prices = simulated_prices[-1, :]  # Final prices for all paths
        
        plt.figure(figsize=(12, 6))
        
        # Histogram
        plt.hist(final_prices, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        
        # Add vertical lines for statistics
        mean_price = np.mean(final_prices)
        median_price = np.median(final_prices)
        percentile_5 = np.percentile(final_prices, 5)
        percentile_95 = np.percentile(final_prices, 95)
        
        plt.axvline(mean_price, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_price:.2f}')
        plt.axvline(median_price, color='green', linestyle='--', linewidth=2, label=f'Median: ${median_price:.2f}')
        plt.axvline(percentile_5, color='orange', linestyle=':', linewidth=2, label=f'5th %: ${percentile_5:.2f}')
        plt.axvline(percentile_95, color='orange', linestyle=':', linewidth=2, label=f'95th %: ${percentile_95:.2f}')
        
        plt.title(f'Final Value Distribution: {ticker}\n(100,000 Simulations)', 
                 fontsize=14, fontweight='bold')
        plt.xlabel('Final Price ($)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
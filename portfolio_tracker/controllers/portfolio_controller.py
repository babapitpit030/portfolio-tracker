"""
Controller component managing data flow between Model and View.
"""
from typing import Optional, Dict, List
import pandas as pd
from ..models.portfolio import Portfolio
from ..models.asset import Asset
from ..views.cli_view import CLIView
from ..views.plot_view import PlotView
from ..utils.data_fetcher import DataFetcher
from ..utils.calculations import PortfolioCalculations


class PortfolioController:
    """Manages the portfolio application logic and data flow."""
    
    def __init__(self):
        """Initialize the controller with empty portfolio and views."""
        self.portfolio = Portfolio()
        self.cli_view = CLIView()
        self.plot_view = PlotView()
        self.data_fetcher = DataFetcher()
    
def add_asset(self) -> None:
    """Add a new asset to the portfolio with automatic sector/asset class detection."""
    self.cli_view.display_message("Add New Asset")
    
    try:
        ticker = input("Enter asset ticker (e.g., AAPL, MSFT, VOO): ").strip().upper()
        
        # Fetch stock information automatically
        self.cli_view.display_message(f"Fetching information for {ticker}...")
        stock_info = self.data_fetcher.get_stock_info(ticker)
        
        if not stock_info['success']:
            self.cli_view.display_message(f"Warning: Could not automatically detect information for {ticker}")
            # Fall back to manual input
            sector = input("Enter sector (or press Enter for 'Unknown'): ").strip() or "Unknown"
            asset_class = input("Enter asset class (or press Enter for 'Stocks'): ").strip() or "Stocks"
        else:
            # Use automatically detected information
            sector = stock_info['sector'] or "Unknown Sector"
            asset_class = stock_info['asset_class']
            company_name = stock_info['company_name']
            
            self.cli_view.display_message(f"Detected: {company_name}")
            self.cli_view.display_message(f"Sector: {sector}")
            self.cli_view.display_message(f"Asset Class: {asset_class}")
            
            # Allow user to override if needed
            override = input("Override detected values? (y/N): ").strip().lower()
            if override == 'y':
                sector = input(f"Enter sector [current: {sector}]: ").strip() or sector
                asset_class = input(f"Enter asset class [current: {asset_class}]: ").strip() or asset_class
        
        # Get quantity and purchase price (still manual)
        quantity = float(input("Enter quantity: "))
        purchase_price = float(input("Enter purchase price: "))
        
        # Create new asset
        asset = Asset(
            ticker=ticker,
            sector=sector,
            asset_class=asset_class,
            quantity=quantity,
            purchase_price=purchase_price
        )
        
        # Try to get current price
        current_price = self.data_fetcher.get_current_price(ticker)
        if current_price:
            asset.update_price(current_price)
            self.cli_view.display_message(f"Current price: ${current_price:.2f}")
        else:
            self.cli_view.display_message(f"Could not fetch current price. Using purchase price.")
            asset.update_price(purchase_price)
        
        # Add to portfolio
        self.portfolio.add_asset(asset)
        self.cli_view.display_message(f"Asset {ticker} added successfully!")
        
    except ValueError as e:
        self.cli_view.display_message(f"Error: Invalid input. Please enter numeric values for quantity and price.")
    except Exception as e:
        self.cli_view.display_message(f"Error adding asset: {e}")
    
    def remove_asset(self) -> None:
        """Remove an asset from the portfolio."""
        ticker = input("Enter ticker to remove: ").strip().upper()
        
        if self.portfolio.remove_asset(ticker):
            self.cli_view.display_message(f"Asset {ticker} removed successfully!")
        else:
            self.cli_view.display_message(f"Asset {ticker} not found in portfolio.")
    
    def view_portfolio(self) -> None:
        """Display the current portfolio."""
        if not self.portfolio.assets:
            self.cli_view.display_message("Portfolio is empty.")
            return
        
        df = self.portfolio.get_portfolio_dataframe()
        self.cli_view.display_dataframe(df, "CURRENT PORTFOLIO")
        
        # Display summary
        summary = self.portfolio.get_performance_summary()
        self.cli_view.display_portfolio_summary(summary)
    
    def update_prices(self) -> None:
        """Update current prices for all assets in portfolio."""
        if not self.portfolio.assets:
            self.cli_view.display_message("Portfolio is empty.")
            return
        
        updated_count = 0
        for asset in self.portfolio.assets:
            current_price = self.data_fetcher.get_current_price(asset.ticker)
            if current_price:
                asset.update_price(current_price)
                updated_count += 1
                self.cli_view.display_message(f"Updated {asset.ticker}: ${current_price:.2f}")
            else:
                self.cli_view.display_message(f"Could not update price for {asset.ticker}")
        
        self.cli_view.display_message(f"Updated prices for {updated_count} assets.")
    
    def view_asset_weights(self) -> None:
        """Display asset weights."""
        weights = self.portfolio.calculate_weights()
        self.cli_view.display_weights(weights, "ASSET WEIGHTS")
    
    def view_sector_allocation(self) -> None:
        """Display sector allocation."""
        sector_weights = self.portfolio.calculate_sector_weights()
        self.cli_view.display_weights(sector_weights, "SECTOR ALLOCATION")
    
    def view_asset_class_allocation(self) -> None:
        """Display asset class allocation."""
        class_weights = self.portfolio.calculate_asset_class_weights()
        self.cli_view.display_weights(class_weights, "ASSET CLASS ALLOCATION")
    
    def plot_historical_prices(self) -> None:
        """Plot historical prices for selected assets."""
        if not self.portfolio.assets:
            self.cli_view.display_message("Portfolio is empty.")
            return
        
        # Get tickers from portfolio
        tickers = [asset.ticker for asset in self.portfolio.assets]
        
        # Let user select which tickers to plot
        self.cli_view.display_message("Available tickers: " + ", ".join(tickers))
        selected = input("Enter tickers to plot (comma-separated, or 'all' for all): ").strip()
        
        if selected.lower() == 'all':
            selected_tickers = tickers
        else:
            selected_tickers = [t.strip().upper() for t in selected.split(',')]
        
        # Fetch and plot historical data
        period = input("Enter period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max) [default: 1y]: ").strip() or "1y"
        
        prices = self.data_fetcher.get_multiple_historical_prices(selected_tickers, period)
        if prices is not None and not prices.empty:
            self.plot_view.plot_historical_prices(prices, f"Historical Prices ({period})")
        else:
            self.cli_view.display_message("Could not fetch historical data.")
    
    def plot_normalized_prices(self) -> None:
        """Plot normalized historical prices."""
        if not self.portfolio.assets:
            self.cli_view.display_message("Portfolio is empty.")
            return
        
        tickers = [asset.ticker for asset in self.portfolio.assets]
        selected = input("Enter tickers to plot (comma-separated, or 'all' for all): ").strip()
        
        if selected.lower() == 'all':
            selected_tickers = tickers
        else:
            selected_tickers = [t.strip().upper() for t in selected.split(',')]
        
        period = input("Enter period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max) [default: 1y]: ").strip() or "1y"
        
        prices = self.data_fetcher.get_multiple_historical_prices(selected_tickers, period)
        if prices is not None and not prices.empty:
            self.plot_view.plot_normalized_prices(prices, f"Normalized Prices ({period})")
        else:
            self.cli_view.display_message("Could not fetch historical data.")
    
    def plot_portfolio_weights(self) -> None:
        """Plot portfolio weights as pie chart."""
        weights = self.portfolio.calculate_weights()
        self.plot_view.plot_portfolio_weights(weights)
    
    def plot_sector_allocation(self) -> None:
        """Plot sector allocation as bar chart."""
        sector_weights = self.portfolio.calculate_sector_weights()
        self.plot_view.plot_sector_allocation(sector_weights)
    
    def run(self) -> None:
        """Run the main application loop."""
        self.cli_view.display_message("Welcome to Portfolio Tracker!")
        
        while True:
            self.cli_view.display_menu()
            
            try:
                choice = input("\nEnter your choice (0-11): ").strip()
                
                if choice == "0":
                    self.cli_view.display_message("Thank you for using Portfolio Tracker!")
                    break
                elif choice == "1":
                    self.add_asset()
                elif choice == "2":
                    self.remove_asset()
                elif choice == "3":
                    self.view_portfolio()
                elif choice == "4":
                    self.update_prices()
                elif choice == "5":
                    self.view_asset_weights()
                elif choice == "6":
                    self.view_sector_allocation()
                elif choice == "7":
                    self.view_asset_class_allocation()
                elif choice == "8":
                    self.plot_historical_prices()
                elif choice == "9":
                    self.plot_normalized_prices()
                elif choice == "10":
                    self.plot_portfolio_weights()
                elif choice == "11":
                    self.plot_sector_allocation()
                else:
                    self.cli_view.display_message("Invalid choice. Please try again.")
            
            except KeyboardInterrupt:
                self.cli_view.display_message("\n\nApplication interrupted. Goodbye!")
                break
            except Exception as e:
                self.cli_view.display_message(f"An error occurred: {e}")
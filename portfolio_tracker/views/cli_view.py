"""
View component for command-line interface display.
"""
from tabulate import tabulate
import pandas as pd
from typing import Dict, List, Any


class CLIView:
    """Handles command-line interface display and formatting."""
    
    @staticmethod
    def display_message(message: str) -> None:
        """Display a simple message."""
        print(f"\n{message}")
    
    @staticmethod
    def display_table(data: List[Dict[str, Any]], headers: str = "keys") -> None:
        """Display data in a formatted table."""
        if not data:
            print("No data to display")
            return
        
        print(tabulate(data, headers=headers, tablefmt="grid", floatfmt=".2f"))
    
    @staticmethod
    def display_dataframe(df: pd.DataFrame, title: str = None) -> None:
        """Display a pandas DataFrame as a formatted table."""
        if df.empty:
            print("No data to display")
            return
        
        if title:
            print(f"\n{title}")
        
        print(tabulate(df, headers='keys', tablefmt="grid", floatfmt=".2f", showindex=False))
    
    @staticmethod
    def display_portfolio_summary(summary: Dict[str, float]) -> None:
        """Display portfolio performance summary."""
        print("\n" + "="*50)
        print("PORTFOLIO SUMMARY")
        print("="*50)
        
        summary_table = [
            ["Total Invested", f"${summary['total_invested']:,.2f}"],
            ["Current Value", f"${summary['total_value']:,.2f}"],
            ["Total P&L", f"${summary['total_profit_loss']:,.2f}"],
            ["Total P&L %", f"{summary['total_profit_loss_percentage']:.2f}%"]
        ]
        
        print(tabulate(summary_table, tablefmt="simple"))
        print("="*50)
    
    @staticmethod
    def display_weights(weights: Dict[str, float], title: str = "Portfolio Weights") -> None:
        """Display asset weights in a table."""
        if not weights:
            print("No weights to display")
            return
        
        weight_data = [{"Asset": asset, "Weight (%)": weight} 
                      for asset, weight in weights.items()]
        
        print(f"\n{title}")
        CLIView.display_table(weight_data)
    
    @staticmethod
    def display_menu() -> None:
        """Display the main menu options."""
        menu_options = [
            ["1", "Add Asset"],
            ["2", "Remove Asset"],
            ["3", "View Portfolio"],
            ["4", "Update Prices"],
            ["5", "View Asset Weights"],
            ["6", "View Sector Allocation"],
            ["7", "View Asset Class Allocation"],
            ["8", "Plot Historical Prices"],
            ["9", "Plot Normalized Prices"],
            ["10", "Plot Portfolio Weights"],
            ["11", "Plot Sector Allocation"],
            ["12", "GBM Simulation (15Y Forecast)"],  # Add this line
            ["0", "Exit"]
        ]
        
        print("\n" + "="*40)
        print("PORTFOLIO TRACKER - MAIN MENU")
        print("="*40)
        print(tabulate(menu_options, headers=["Option", "Action"], tablefmt="simple"))
"""
Portfolio model managing multiple assets and calculations.
"""
from typing import List, Dict, Optional
import pandas as pd
from .asset import Asset


class Portfolio:
    """Manages a collection of assets and performs portfolio-level calculations."""
    
    def __init__(self, name: str = "My Portfolio"):
        """Initialize an empty portfolio."""
        self.name = name
        self.assets: List[Asset] = []
    
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the portfolio."""
        self.assets.append(asset)
    
    def remove_asset(self, ticker: str) -> bool:
        """Remove an asset by ticker symbol."""
        for i, asset in enumerate(self.assets):
            if asset.ticker.upper() == ticker.upper():
                self.assets.pop(i)
                return True
        return False
    
    def get_asset(self, ticker: str) -> Optional[Asset]:
        """Get an asset by ticker symbol."""
        for asset in self.assets:
            if asset.ticker.upper() == ticker.upper():
                return asset
        return None
    
    @property
    def total_value(self) -> float:
        """Calculate the total current value of the portfolio."""
        return sum(asset.current_value for asset in self.assets)
    
    @property
    def total_invested(self) -> float:
        """Calculate the total invested amount."""
        return sum(asset.transaction_value for asset in self.assets)
    
    @property
    def total_profit_loss(self) -> float:
        """Calculate the total profit/loss."""
        return self.total_value - self.total_invested
    
    @property
    def total_profit_loss_percentage(self) -> float:
        """Calculate the total profit/loss percentage."""
        if self.total_invested == 0:
            return 0.0
        return (self.total_profit_loss / self.total_invested) * 100
    
    def calculate_weights(self) -> Dict[str, float]:
        """Calculate the weight of each asset in the portfolio."""
        if self.total_value == 0:
            return {}
        
        weights = {}
        for asset in self.assets:
            weights[asset.ticker] = (asset.current_value / self.total_value) * 100
        return weights
    
    def calculate_sector_weights(self) -> Dict[str, float]:
        """Calculate the weight of each sector in the portfolio."""
        if self.total_value == 0:
            return {}
        
        sector_values = {}
        for asset in self.assets:
            sector_values[asset.sector] = sector_values.get(asset.sector, 0) + asset.current_value
        
        sector_weights = {}
        for sector, value in sector_values.items():
            sector_weights[sector] = (value / self.total_value) * 100
        
        return sector_weights
    
    def calculate_asset_class_weights(self) -> Dict[str, float]:
        """Calculate the weight of each asset class in the portfolio."""
        if self.total_value == 0:
            return {}
        
        class_values = {}
        for asset in self.assets:
            class_values[asset.asset_class] = class_values.get(asset.asset_class, 0) + asset.current_value
        
        class_weights = {}
        for asset_class, value in class_values.items():
            class_weights[asset_class] = (value / self.total_value) * 100
        
        return class_weights
    
    def get_portfolio_dataframe(self) -> pd.DataFrame:
        """Convert portfolio to pandas DataFrame for display and analysis."""
        data = [asset.to_dict() for asset in self.assets]
        return pd.DataFrame(data)
    
    def get_performance_summary(self) -> Dict[str, float]:
        """Get a summary of portfolio performance."""
        return {
            'total_invested': self.total_invested,
            'total_value': self.total_value,
            'total_profit_loss': self.total_profit_loss,
            'total_profit_loss_percentage': self.total_profit_loss_percentage
        }
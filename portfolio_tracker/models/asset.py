"""
Asset model representing a single investment asset.
"""
from dataclasses import dataclass
from typing import Optional
import pandas as pd


@dataclass
class Asset:
    """Represents a single investment asset in the portfolio."""
    
    ticker: str
    sector: str
    asset_class: str
    quantity: float
    purchase_price: float
    current_price: Optional[float] = None
    
    @property
    def transaction_value(self) -> float:
        """Calculate the transaction value (quantity * purchase price)."""
        return self.quantity * self.purchase_price
    
    @property
    def current_value(self) -> float:
        """Calculate the current value (quantity * current price)."""
        if self.current_price is None:
            return self.transaction_value
        return self.quantity * self.current_price
    
    @property
    def profit_loss(self) -> float:
        """Calculate the profit/loss."""
        return self.current_value - self.transaction_value
    
    @property
    def profit_loss_percentage(self) -> float:
        """Calculate the profit/loss percentage."""
        if self.transaction_value == 0:
            return 0.0
        return (self.profit_loss / self.transaction_value) * 100
    
    def update_price(self, new_price: float) -> None:
        """Update the current price of the asset."""
        self.current_price = new_price
    
    def to_dict(self) -> dict:
        """Convert asset to dictionary for display purposes."""
        return {
            'ticker': self.ticker,
            'sector': self.sector,
            'asset_class': self.asset_class,
            'quantity': self.quantity,
            'purchase_price': self.purchase_price,
            'current_price': self.current_price if self.current_price else self.purchase_price,
            'transaction_value': self.transaction_value,
            'current_value': self.current_value,
            'profit_loss': self.profit_loss,
            'profit_loss_percentage': self.profit_loss_percentage
        }
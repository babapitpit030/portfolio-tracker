"""
Utility for fetching current and historical price data.
"""
import yfinance as yf
import pandas as pd
from typing import Optional, Tuple, List, Dict


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
    
    @staticmethod
    def get_stock_info(ticker: str) -> Dict[str, Optional[str]]:
        """Get comprehensive stock information including sector and industry."""
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Extract sector and industry
            sector = info.get('sector', None)
            industry = info.get('industry', None)
            long_name = info.get('longName', ticker)
            
            # Determine asset class based on available information
            asset_class = DataFetcher._determine_asset_class(info, ticker)
            
            return {
                'sector': sector,
                'industry': industry,
                'asset_class': asset_class,
                'company_name': long_name,
                'success': True
            }
            
        except Exception as e:
            print(f"Error fetching stock info for {ticker}: {e}")
            return {
                'sector': None,
                'industry': None,
                'asset_class': 'Unknown',
                'company_name': ticker,
                'success': False
            }
    
    @staticmethod
    def _determine_asset_class(info: Dict, ticker: str) -> str:
        """Determine asset class based on available information."""
        # Check if it's an ETF
        if info.get('quoteType') == 'ETF':
            return 'ETF'
        
        # Check if it's a mutual fund
        if info.get('quoteType') == 'MUTUALFUND':
            return 'Mutual Fund'
        
        # Check for bond indicators
        if any(keyword in ticker.upper() for keyword in ['BOND', 'TLT', 'IEF', 'HYG']):
            return 'Bonds'
        
        # Check for cryptocurrency
        if any(keyword in ticker.upper() for keyword in ['BTC', 'ETH', 'COIN', 'GBTC']):
            return 'Cryptocurrency'
        
        # Check for real estate (REITs)
        if info.get('industry') and 'REIT' in info.get('industry', '').upper():
            return 'Real Estate'
        if info.get('sector') and 'REAL ESTATE' in info.get('sector', '').upper():
            return 'Real Estate'
        
        # Check for specific sectors that might indicate asset class
        sector = info.get('sector', '').upper()
        if sector in ['FINANCIAL SERVICES', 'FINANCIALS']:
            # Check if it's a bank or insurance company
            industry = info.get('industry', '').upper()
            if any(word in industry for word in ['BANK', 'INSURANCE', 'FINANCIAL']):
                return 'Financials'
        
        # Default to Stocks for most equity tickers
        if info.get('quoteType') == 'EQUITY':
            return 'Stocks'
        
        # Final fallback
        return 'Stocks'  # Most common case for individual stock tickers
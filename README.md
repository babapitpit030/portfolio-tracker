# Portfolio Tracker

A command-line interface (CLI) application for tracking investment portfolios, built with Python following the Model-View-Controller (MVC) architecture.

## Features

- **Asset Management**: Add and remove assets with detailed information
- **Real-time Price Updates**: Fetch current market prices using Yahoo Finance API
- **Portfolio Analysis**: View performance metrics, weights, and allocations
- **Data Visualization**: Create graphs for historical prices and portfolio composition
- **Sector & Asset Class Analysis**: Analyze portfolio by sectors and asset classes

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/babapitpit030/portfolio-tracker.git
   cd portfolio-tracker
# Portfolio Tracker

A comprehensive command-line interface (CLI) application for tracking investment portfolios, built with Python following the Model-View-Controller (MVC) architecture. This application automatically fetches real-time market data and provides detailed portfolio analysis with visualizations.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-orange)

## 🚀 Features

- **🔄 Automatic Asset Detection**: Enter just the ticker symbol - the app automatically detects sector, asset class, and company name
- **📊 Real-time Price Updates**: Live market data from Yahoo Finance API
- **📈 Portfolio Analytics**: Comprehensive performance metrics and weight calculations
- **🎯 Sector & Asset Class Analysis**: Breakdown by sectors and investment types
- **📉 Data Visualization**: Historical price charts and portfolio composition graphs
- **💾 No Database Required**: Everything runs in memory with option to export data

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage Guide](#detailed-usage-guide)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/babapitpit030/portfolio-tracker.git
   cd portfolio-tracker
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   *Alternatively, install packages individually:*
   ```bash
   pip install pandas numpy matplotlib yfinance tabulate requests python-dateutil
   ```

## 🚀 Quick Start

1. **Run the Application**
   ```bash
   python -m portfolio_tracker.main
   ```

2. **Add Your First Asset**
   ```
   Welcome to Portfolio Tracker!

   ========================================
   PORTFOLIO TRACKER - MAIN MENU
   ========================================
   Option  Action
   1       Add Asset
   2       Remove Asset
   ...

   Enter your choice (0-11): 1

   Add New Asset
   Enter asset ticker (e.g., AAPL, MSFT, VOO): AAPL
   Fetching information for AAPL...
   Detected: Apple Inc.
   Sector: Technology
   Asset Class: Stocks
   Enter quantity: 10
   Enter purchase price: 150.00
   Current price: $172.50
   Asset AAPL added successfully!
   ```

3. **View Your Portfolio**
   ```
   Enter your choice (0-11): 3

   CURRENT PORTFOLIO
   +---------+-------------+--------------+----------+----------------+---------------+-------------------+---------------+-------------+-----------------------+
   | ticker  | sector      | asset_class  | quantity | purchase_price | current_price | transaction_value | current_value | profit_loss | profit_loss_percentage |
   +---------+-------------+--------------+----------+----------------+---------------+-------------------+---------------+-------------+-----------------------+
   | AAPL    | Technology  | Stocks       |    10.00 |         150.00 |        172.50 |           1500.00 |       1725.00 |      225.00 |                 15.00 |
   +---------+-------------+--------------+----------+----------------+---------------+-------------------+---------------+-------------+-----------------------+

   ==================================================
   PORTFOLIO SUMMARY
   ==================================================
   Total Invested  $1,500.00
   Current Value   $1,725.00
   Total P&L       $225.00
   Total P&L %     15.00%
   ==================================================
   ```

## 📖 Detailed Usage Guide

### Main Menu Options

| Option | Action | Description |
|--------|--------|-------------|
| 1 | Add Asset | Add new investment with automatic sector/asset class detection |
| 2 | Remove Asset | Remove asset by ticker symbol |
| 3 | View Portfolio | Display complete portfolio with performance metrics |
| 4 | Update Prices | Fetch latest market prices for all assets |
| 5 | View Asset Weights | Show percentage allocation of each asset |
| 6 | View Sector Allocation | Breakdown by industry sectors |
| 7 | View Asset Class Allocation | Breakdown by investment types |
| 8 | Plot Historical Prices | Chart historical price movements |
| 9 | Plot Normalized Prices | Compare performance with normalized charts |
| 10 | Plot Portfolio Weights | Pie chart of asset allocation |
| 11 | Plot Sector Allocation | Bar chart of sector distribution |
| 0 | Exit | Close the application |

### Adding Assets

The application automatically detects:
- **Company Name**
- **Sector** (Technology, Healthcare, Financials, etc.)
- **Asset Class** (Stocks, ETFs, Bonds, Real Estate, etc.)

**Supported Ticker Examples:**
- **Stocks**: `AAPL`, `MSFT`, `TSLA`, `GOOGL`
- **ETFs**: `VOO`, `QQQ`, `SPY`, `ARKK`
- **REITs**: `O`, `VNQ`, `AMT`
- **Bonds**: `BND`, `TLT`, `IEF`
- **Cryptocurrency**: `BTC-USD`, `ETH-USD`

**Example Session:**
```
Add New Asset
Enter asset ticker (e.g., AAPL, MSFT, VOO): VOO
Fetching information for VOO...
Detected: Vanguard S&P 500 ETF
Sector: Diversified
Asset Class: ETF
Enter quantity: 5
Enter purchase price: 400.00
Current price: $415.25
Asset VOO added successfully!
```

### Portfolio Analysis Features

#### 1. Performance Metrics
- Current value vs. invested amount
- Total profit/loss (absolute and percentage)
- Individual asset performance

#### 2. Weight Calculations
- Asset weights (percentage of portfolio)
- Sector allocation
- Asset class distribution

#### 3. Visualizations
- Historical price charts (1 day to 10 years)
- Normalized performance comparison
- Portfolio composition pie charts
- Sector allocation bar charts

### Example Workflow

1. **Build Your Portfolio**
   ```bash
   # Add diverse assets
   AAPL (Technology Stocks)
   VOO (Diversified ETF)  
   O (Real Estate REIT)
   BND (Bond ETF)
   ```

2. **Analyze Performance**
   - View portfolio summary (Option 3)
   - Check asset weights (Option 5)
   - Analyze sector allocation (Option 6)

3. **Create Visualizations**
   - Plot historical prices (Option 8)
   - View portfolio weights chart (Option 10)
   - Analyze sector distribution (Option 11)

## 🏗 Project Structure

```
portfolio-tracker/
├── portfolio_tracker/
│   ├── models/
│   │   ├── asset.py              # Asset data model with financial calculations
│   │   └── portfolio.py          # Portfolio management and analytics
│   ├── views/
│   │   ├── cli_view.py           # Command-line interface and table formatting
│   │   └── plot_view.py          # Data visualization with matplotlib
│   ├── controllers/
│   │   └── portfolio_controller.py # Application logic and menu system
│   ├── utils/
│   │   ├── data_fetcher.py       # Yahoo Finance API integration
│   │   └── calculations.py       # Financial calculations and metrics
│   ├── __init__.py
│   └── main.py                   # Application entry point
├── tests/                        # Unit tests
├── docs/                         # Documentation
├── requirements.txt              # Python dependencies
├── setup.py                      # Package installation configuration
├── run.py                        # Alternative entry point
└── README.md                     # This file
```

## 🔧 Technical Details

### Architecture
- **Model-View-Controller (MVC) Pattern**
  - **Models**: Data structures and business logic (`Asset`, `Portfolio`)
  - **Views**: User interface components (`CLIView`, `PlotView`)
  - **Controllers**: Application flow management (`PortfolioController`)

### Data Sources
- **Yahoo Finance API**: Real-time and historical market data
- **Automatic Classification**: Smart detection of sectors and asset classes

### Dependencies
| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `matplotlib` | Data visualization and charts |
| `yfinance` | Yahoo Finance API integration |
| `tabulate` | Beautiful CLI table formatting |
| `requests` | HTTP requests for data fetching |

### Supported Time Periods for Historical Data
- `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`

## 🐛 Troubleshooting

### Common Issues

1. **"Command not found: python"**
   ```bash
   # Use python3 instead
   python3 -m portfolio_tracker.main
   ```

2. **"Module not found" errors**
   ```bash
   # Ensure virtual environment is activated and dependencies are installed
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Price data not loading**
   - Check internet connection
   - Verify ticker symbol is correct
   - Try again later (API might be temporarily unavailable)

4. **Plotting not working**
   - Ensure matplotlib is properly installed
   - On macOS, you might need: `pip install --upgrade matplotlib`

This project is developed for educational purposes as part of the a.s.r. Vermogensbeheer assignment. Feel free to use and modify for personal or educational purposes.

## 🙏 Acknowledgments

- **Yahoo Finance** for providing free market data API
- **Python community** for excellent data science libraries
- **a.s.r. Vermogensbeheer** for the project assignment inspiration

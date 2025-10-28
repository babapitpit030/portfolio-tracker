from setuptools import setup, find_packages

setup(
    name="portfolio-tracker",
    version="1.0.0",
    description="A command-line portfolio tracking application",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "requests>=2.28.0",
        "yfinance>=0.2.0",
        "tabulate>=0.9.0",
        "python-dateutil>=2.8.0",
    ],
    entry_points={
        'console_scripts': [
            'portfolio-tracker=portfolio_tracker.main:main',
        ],
    },
    python_requires='>=3.8',
)
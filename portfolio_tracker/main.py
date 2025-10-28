"""
Main entry point for the Portfolio Tracker application.
"""
from .controllers.portfolio_controller import PortfolioController


def main():
    """Main function to run the Portfolio Tracker application."""
    try:
        controller = PortfolioController()
        controller.run()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
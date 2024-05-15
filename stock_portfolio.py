import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] -= shares
            if self.portfolio[symbol] <= 0:
                del self.portfolio[symbol]
        else:
            print(f"{symbol} not found in portfolio.")

    def get_stock_price(self, symbol):
        try:
            response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=YOUR_API_KEY')
            response.raise_for_status()
            return float(response.json()['Global Quote']['05. price'])
        except (requests.exceptions.RequestException, KeyError, ValueError) as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def display_portfolio(self):
        print("Portfolio:")
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                print(f"{symbol}: {shares} shares - Current Price: ${price:.2f}")

# Example usage
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10)
portfolio.add_stock('GOOGL', 5)
portfolio.display_portfolio()

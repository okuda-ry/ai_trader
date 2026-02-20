import pandas as pd


class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window
        self.prices = []

    def update(self, price):
        self.prices.append(price)

        if len(self.prices) < self.long_window:
            return "WAIT"

        df = pd.DataFrame(self.prices, columns=["price"])
        short_ma = df["price"].rolling(self.short_window).mean().iloc[-1]
        long_ma = df["price"].rolling(self.long_window).mean().iloc[-1]

        if short_ma > long_ma:
            return "BUY"
        elif short_ma < long_ma:
            return "SELL"
        else:
            return "WAIT"

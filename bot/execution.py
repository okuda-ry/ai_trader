class PaperTrader:
    def __init__(self, initial_balance=1000000):
        self.balance = initial_balance
        self.position = 0
        self.entry_price = None

    def execute(self, signal, price):

        if signal == "BUY" and self.position == 0:
            self.position = 1
            self.entry_price = price
            print(f"BUY at {price}")

        elif signal == "SELL" and self.position == 1:
            profit = price - self.entry_price
            self.balance += profit
            self.position = 0
            print(f"SELL at {price} | Profit: {profit}")

        return self.balance

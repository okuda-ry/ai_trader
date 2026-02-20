import time
from market import get_market
from strategy import MovingAverageStrategy
from execution import PaperTrader

strategy = MovingAverageStrategy()
trader = PaperTrader()


def run():
    print("Paper trading started")

    while True:
        market = get_market()
        price = market["price"]

        signal = strategy.update(price)
        balance = trader.execute(signal, price)

        print(f"Price: {price} | Signal: {signal} | Balance: {balance}")

        time.sleep(60)


if __name__ == "__main__":
    run()

import requests

URL = "https://api.bitflyer.com/v1/ticker?product_code=BTC_JPY"


def get_market():
    r = requests.get(URL).json()

    return {
        "price": r["ltp"],
        "bid": r["best_bid"],
        "ask": r["best_ask"],
        "volume": r["volume"],
        "timestamp": r["timestamp"],
    }

import time

from crypto_data import get_coins, Coin

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, 'Triggered!!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    while True:
        time.sleep(30)
        alert('btc', bottom=20000, top=88000, coins_list=coins)
        alert('eth', bottom=2000, top=3500, coins_list=coins)
        alert('xrp', bottom=2.0, top=3.0, coins_list=coins)

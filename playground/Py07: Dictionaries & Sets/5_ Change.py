def change(money):
    coin_types = [2.0, 1.0, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]
    result = {}
    for coin in coin_types:
        result[coin] = int(money//coin)
        money -= coin* result[coin]
        money = round(money,2)
    return result
def shopping(alist, stock):
    paid = 0
    missing = {}
    for key,value in alist.items():
        if key in stock.keys():
            available_quantity, item_price = stock[key]
            quantity_bought = min(value, available_quantity)
            if value <= quantity_bought:
                paid += quantity_bought * item_price
            else:
                missing[key] = (value - quantity_bought)
                paid += quantity_bought * item_price
        else:
            missing[key] = value
    return (paid, missing)

#print(shopping({'banana': 10, 'apples': 20, 'oranges': 30}, {'banana': (30, 3), 'apples': (10, 2)}))
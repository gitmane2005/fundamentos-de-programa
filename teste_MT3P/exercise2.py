def shopping(alist, stock):
    paid = 0
    missing = {}
    for key,value in alist.items():
        if key in stock:
            available_quantity, price = stock[key]
            bought_quantity = min(value, available_quantity)
            if available_quantity >= bought_quantity:
                paid += value * price
            else:
                missing[key] = bought_quantity
                paid += bought_quantity * price
        else:
            missing[key] = value 
    return paid, missing

"""def shopping(desired_list, stock):
    spent = 0
    missing = {}

    for item, quantity in desired_list.items():
        if item in stock:
            available_quantity, price = stock[item]
            bought_quantity = min(quantity, available_quantity)
            spent += bought_quantity * price
            if bought_quantity < quantity:
                missing[item] = quantity - bought_quantity
        else:
            missing[item] = quantity

    return spent, missing"""
print(shopping({'banana': 10, 'apples': 20, 'oranges': 30}, {'banana': (30, 3), 'apples': (10, 2)}))

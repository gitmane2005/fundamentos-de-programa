distance = int(input())
consup_km = float(input())
price_liter = float(input())

liter_consuption = (consup_km*distance) / 100

money_needed = liter_consuption*price_liter

print(round(money_needed, 2))

price = int(input())
paid = int(input())
change = paid - price

bil_50 = 0
bil_20 = 0
bil_10 = 0
bil_5 = 0
    
if 50 <= change:
    bil_50 = change // 50
    change = change % 50
if 20 <= change:
    bil_20 = change // 20
    change = change % 20
if 10 <= change:
    bil_10 = change // 10
    change = change % 10
if 5 <= change:
    bil_5 = change // 5
    change = change % 5

print(str(bil_50) + " " + str(bil_20) + " "  + str(bil_10) + " "  + str(bil_5))
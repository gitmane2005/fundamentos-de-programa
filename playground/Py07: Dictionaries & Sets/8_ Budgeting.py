def budgeting(budget, products, wishlist):
    dream = budget
    wishlist_list = []
    for (key,number) in wishlist.items():
        wishlist_list.append((key,number))
        dream = dream - products[key]*number
    if dream >= 0:
        return wishlist
    wishlist_list.sort(reverse= True,key= lambda x: products[x[0]])
    
    for tup in wishlist_list:
        if products[tup[0]]* tup[1] < budget:
            budget -= products[tup[0]]* tup[1]
        elif products[tup[0]] > budget:
            wishlist.pop(tup[0])
        else:
            for x in range(tup[1]):
                if products[tup[0]]>budget:
                    break
                else:
                    wishlist[tup[0]] = x+1
                    budget -= products[tup[0]]
    return wishlist


print(budgeting(750, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))
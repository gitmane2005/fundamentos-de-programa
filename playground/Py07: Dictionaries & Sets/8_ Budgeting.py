def budgeting(budget, products, wishlist):
    wishlist_list = sorted(wishlist.items(), key=lambda x: products[x[0]], reverse=True)

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
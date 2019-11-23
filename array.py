# price = 100
# discount = 5
# price_with_discount = price - price * discount/100
# print(price_with_discount)
def discounted(price, discount=5):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)
discounted(100,8)
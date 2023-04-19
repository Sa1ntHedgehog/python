def apply_discount(product,discount):
    price=int(product['price']*(1.0-discount))
    assert 0<=price<=product['price']
    if 0<=price<=product['price']:
        return price
    else: return "Discount error"

prod={'name':'Some product','price':15999}
print(apply_discount(prod,-0.25))

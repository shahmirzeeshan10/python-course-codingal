
# My Snack Shop

snack = "Chips"

price = 1.50

quantity = 10

available = True

# Data types

print(snack, price, quantity, available)
print("welcome to codingal")
print(type(snack), type(price), type(quantity), type(available))

# Arithmetic

print("Total:", price * quantity)

print("Sale price:", price - 0.25) #shop is giving 25% discount

print("Double stock:", quantity * 2)

# Comparison

print("Cheap?", price < 2)

print("Enough stock?", quantity > 5)

print("Price is 1.50?", price == 1.50)
shop="Quick" +" bites"
print(shop)
print(len(snack))
print(snack[0])
price_a=1.50
price_b=3.00
temp =price_a
price_a=price_b
price_b= temp
print("after swap :", price_a, "and" , price_b)



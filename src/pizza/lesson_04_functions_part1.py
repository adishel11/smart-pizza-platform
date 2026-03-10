def say_hello():
    print("Hello, welcome to Smart Pizza!")
print("--- BASIC FUNCTION ---")
say_hello()
say_hello()
say_hello()


print()
print("--- FUNCTION WITH PARAMETER ---")
def greet_customer(name):
    print(f"Hello, {name}! Welcome to Smart Pizza!")
greet_customer("Adish")
greet_customer("Maria")
greet_customer("Chef John")


print()
print("--- MULTIPLE PARAMETERS ---")
def show_pizza_price(pizza_name, price):
    print(f"{pizza_name}: ${price:.2f}")
show_pizza_price("Margherita", 10.99)
show_pizza_price("Pepperoni", 12.99)
show_pizza_price("Veggie", 11.99)


print()
print("--- RETURN VALUES ---")
def calculate_tax(amount):
    tax = amount * 0.08
    return tax
my_tax = calculate_tax(100)
print(f"Tax on $100: ${my_tax:.2f}")

print()
subtotal = 50.00
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${calculate_tax(subtotal):.2f}")

print()
print("--- RETURN MULTIPLE VALUES ---")
def calculate_order(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.08
    total = subtotal + tax
    return subtotal, tax, total
sub, tx, tot = calculate_order(12.99, 3)
print(f"Subtotal: ${sub:.2f}")
print(f"Tax: ${tx:.2f}")
print(f"Total: ${tot:.2f}")


print()
print("--- DEFAULT PARAMETERS ---")
def calculate_total(price, quantity=1):
    return price * quantity
print(f"1 pizza: ${calculate_total(10.99)}")
print(f"3 pizzas: ${calculate_total(10.99, 3)}")


print()
def create_order(pizza, size="Medium", quantity=1):
    print(f"Order: {quantity}x {size} {pizza}")
create_order("Margherita")
create_order("Pepperoni", "Large")
create_order("Veggie", "Small", 2)


print()
print("--- KEYWORD ARGUMENTS ---")
create_order("BBQ Chicken", quantity=4)
create_order("Hawaiian", size="Large", quantity=2)
create_order(quantity=3, size="Small", pizza="Veggie")


print()
print("=" * 40)
print("COMPLETE PIZZA CALCULATOR")
print("=" * 40)
def calculate_pizza_order(pizza_name, price, quantity=1, delivery=False):
    subtotal = price * quantity
    tax = subtotal * 0.08   
    if delivery:
        delivery_fee = 3.99
    else:
        delivery_fee = 0.00   
    total = subtotal + tax + delivery_fee  
    return subtotal, tax, delivery_fee, total
print()
print("Order 1: Pickup")
sub, tax, fee, total = calculate_pizza_order("Margherita", 10.99, 2)
print(f"  Subtotal: ${sub:.2f}")
print(f"  Tax: ${tax:.2f}")
print(f"  Delivery: ${fee:.2f}")
print(f"  Total: ${total:.2f}")
print()
print("Order 2: Delivery")
sub, tax, fee, total = calculate_pizza_order("Pepperoni", 12.99, quantity=3, delivery=True)
print(f"  Subtotal: ${sub:.2f}")
print(f"  Tax: ${tax:.2f}")
print(f"  Delivery: ${fee:.2f}")
print(f"  Total: ${total:.2f}")


print()
print("--- VARIABLE SCOPE ---")
restaurant_name = "Smart Pizza"
def show_restaurant():
    print(f"Welcome to {restaurant_name}")
def try_to_change():
    pizza_of_the_day = "Hawaiian"
    print(f"Today's special: {pizza_of_the_day}")
show_restaurant()
try_to_change()
print(f"Restaurant: {restaurant_name}")


 

print("=" * 50)
print("🍕 LESSON 02: ORDERING PIZZA 🍕")
print("=" * 50)
print()
customer_name = input("Enter your name: ")
print(f"Hello, {customer_name}")

print()
print("--- MENU ---")
print("1. Margherita  - $10.99")
print("2. Pepperoni   - $12.99")
print("3. Veggie      - $11.99")

print()
choice = int(input("Please select a pizza (1, 2, or 3): "))
print(f"You selected option {choice}")
print(f"Type of choice variable: {type(choice)}")  # This will be a string!

print()
if choice == 1:
    pizza_name = "Margherita"
    price = 10.99
    toppings = ["mozzarella", "tomato", "basil"]
    is_vegetarian = True
elif choice == 2:
    pizza_name = "Pepperoni"
    price = 12.99
    toppings = ["mozzarella", "tomato", "pepperoni"]
    is_vegetarian = False
elif choice == 3:
    pizza_name = "Veggie"
    price = 11.99
    toppings = ["mozzarella", "tomato", "bell peppers", "olives"]
    is_vegetarian = True
else:
    pizza_name = "Margherita"
    price = 10.99
    toppings = ["mozzarella", "tomato", "basil"]
    print("Invalid choice. Defaulting to Margherita.")
print(f"You've selected: {pizza_name} pizza with toppings: {toppings}")

print()
quantity = int(input("How many pizzas would like to order? "))
subtotal = price * quantity
print(f"Your SubTotal {subtotal}")
taxrate = 0.08
tax = subtotal * taxrate
print(f"You tax (8%) {tax: .2f}")
grandtotal = subtotal + tax
print(f"Your grand total {grandtotal: .2f}")

print()
print("--- DELIVERY OPTIONS ---")
print("D - Delivery ($3.99 fee)")
print("P - Pickup (Free)")
delivery_choice = input("Enter D or P: ")
delivery_choice = delivery_choice.upper()
if delivery_choice == "D":
    delivery_fee = 3.99
    print("Delivery selected!")
    address = input("Enter delivery address: ")
    print(f"Delivering to: {address}")
else:
    delivery_fee = 0.00
    print("Pickup selected - ready in 20 minutes!")
    address = "N/A"

grandtotal = subtotal + tax + delivery_fee
print(f"Your grand total {grandtotal: .2f}")

print()
print("=" * 40)
print("         RECEIPT")
print("=" * 40)

print(f"Customer: {customer_name}")
print("-" * 40)

print(f"Pizza: {pizza_name}")
print(f"Quantity: {quantity}")
print(f"Price each: ${price:.2f}")
print("-" * 40)

print(f"Subtotal:     ${subtotal:.2f}")
print(f"Tax (8%):     ${tax:.2f}")
print(f"Delivery:     ${delivery_fee:.2f}")
print("-" * 40)
print(f"TOTAL:        ${grandtotal:.2f}")
print("=" * 40)

print()
if delivery_choice == "D":
    print(f"🚗 Delivering to: {address}")
    print("Estimated time: 30-45 minutes")
else:
    print("🏪 Pickup at: 123 Pizza Street")
    print("Ready in: 20 minutes")

print()
print("🍕 Thank you for your order! 🍕")
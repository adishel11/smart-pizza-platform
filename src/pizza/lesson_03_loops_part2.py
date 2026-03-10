pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]
prices = [10.99, 12.99, 11.99, 13.99]

print()
print("=" * 50)
print("🍕 SMART PIZZA ORDERING SYSTEM 🍕")
print("=" * 50)

print()
print("--- MENU ---")
for index, (pizza, price) in enumerate(zip(pizzas, prices)):
    print(f"  {index + 1}. {pizza:>15} ${price:6.2f}")
print()

order = []
print("Enter pizza number to add (or 'done' to finish)")
print()
while True:
    choice = input("Your choice: ")    
    if choice.lower() == "done":
        break

    choice = int(choice)
    
    if choice < 1 or choice > len(pizzas):
        print(f"❌ Please enter 1-{len(pizzas)}")
        continue

    selected_pizza = pizzas[choice - 1]
    selected_price = prices[choice - 1]
    
    order.append({"pizza": selected_pizza, "price": selected_price})
    print(f"✓ Added {selected_pizza} - ${selected_price:.2f}")
    print()

print()
if len(order) == 0:
    print("No pizzas ordered. Goodbye!")
else:
    print()
    print("=" * 40)
    print("       ORDER SUMMARY")
    print("=" * 40)
    
    subtotal = 0
    for index, item in enumerate(order):
        print(f"  {index + 1}. {item['pizza']:<15} ${item['price']:.2f}")
        subtotal += item['price']
    
    tax = subtotal * 0.08
    total = subtotal + tax
    
    print("-" * 40)
    print(f"  {'Subtotal:':<17} ${subtotal:.2f}")
    print(f"  {'Tax (8%):':<17} ${tax:.2f}")
    print(f"  {'TOTAL:':<17} ${total:.2f}")
    print("=" * 40)
    print()
    print(f"🍕 Thank you! {len(order)} pizza(s) coming up!")

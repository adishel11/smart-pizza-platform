print()
print("=" * 50)
print("COMPLETE ORDERING SYSTEM WITH FUNCTIONS")
print("=" * 50)

def display_banner():
    print()
    print("=" * 40)
    print("   🍕 SMART PIZZA PLATFORM 🍕")
    print("=" * 40)

def display_menu(pizzas, prices):
    print()
    print("--- MENU ---")
    for index, (pizza, price) in enumerate(zip(pizzas, prices)):
        print(f"  {index + 1}. {pizza:<15} ${price:.2f}")
    print()

def get_valid_choice(max_choice):
    while True:
        choice = input("Enter pizza number (or 'done'): ")
        
        if choice.lower() == "done":
            return None
        
        choice = int(choice)
        
        if choice < 1 or choice > max_choice:
            print(f"❌ Please enter 1-{max_choice}")
            continue
        
        return choice
    
def calculate_order(order_items, tax_rate=0.08):
    subtotal = sum(item["price"] for item in order_items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

def display_receipt(order_items, subtotal, tax, total):
    print()
    print("=" * 40)
    print("         RECEIPT")
    print("=" * 40)
    
    for index, item in enumerate(order_items):
        print(f"  {index + 1}. {item['pizza']:<15} ${item['price']:.2f}")
    
    print("-" * 40)
    print(f"  {'Subtotal:':<20} ${subtotal:.2f}")
    print(f"  {'Tax (8%):':<20} ${tax:.2f}")
    print(f"  {'TOTAL:':<20} ${total:.2f}")
    print("=" * 40)

def main():
    pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]
    prices = [10.99, 12.99, 11.99, 13.99]
    order_items = []
    
    display_banner()
    display_menu(pizzas, prices)
    
    print("Start your order!")
    print()
    
    while True:
        choice = get_valid_choice(len(pizzas))
        
        if choice is None:
            break
        
        selected_pizza = pizzas[choice - 1]
        selected_price = prices[choice - 1]
        
        order_items.append({"pizza": selected_pizza, "price": selected_price})
        print(f"✓ Added {selected_pizza}")
        print()
    
    if len(order_items) == 0:
        print("No items ordered. Goodbye!")
    else:
        subtotal, tax, total = calculate_order(order_items)
        display_receipt(order_items, subtotal, tax, total)
        print()
        print(f"🍕 Thank you for ordering {len(order_items)} pizza(s)!")

main()
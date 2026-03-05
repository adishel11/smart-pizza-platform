"""
🍕 Smart Pizza Platform - Lesson 1.1: EXERCISE SOLUTIONS

These are the solutions to the 3 exercises from lesson_01_variables.py
"""

# ============================================================
# Exercise 1: Create a new pizza
# ============================================================

your_pizza_name = "Pepperoni Feast"
your_pizza_price = 15.99
your_pizza_toppings = ["pepperoni", "mozzarella", "tomato sauce", "oregano"]

print("=== EXERCISE 1: Your Pizza ===")
print(f"Pizza Name: {your_pizza_name}")
print(f"Price: ${your_pizza_price}")
print(f"Toppings: {your_pizza_toppings}")
print()


# ============================================================
# Exercise 2: Create a complete pizza dictionary
# ============================================================

my_custom_pizza = {
    "name": "Spicy BBQ Chicken",
    "price": 17.99,
    "size": "large",
    "toppings": ["grilled chicken", "bbq sauce", "red onions", "jalapeños", "mozzarella"],
    "is_spicy": True
}

print("=== EXERCISE 2: Custom Pizza Dictionary ===")
print(f"Name: {my_custom_pizza['name']}")
print(f"Price: ${my_custom_pizza['price']}")
print(f"Size: {my_custom_pizza['size']}")
print(f"Toppings: {my_custom_pizza['toppings']}")
print(f"Spicy: {my_custom_pizza['is_spicy']}")
print()


# ============================================================
# Exercise 3: Calculate total for 3 pizzas with 8% tax
# ============================================================

your_quantity = 3
your_subtotal = your_pizza_price * your_quantity  # 15.99 * 3 = 47.97
your_tax = your_subtotal * 0.08                    # 47.97 * 0.08 = 3.8376
your_total = your_subtotal + your_tax              # 47.97 + 3.8376 = 51.8076

print("=== EXERCISE 3: Order Calculation ===")
print(f"Pizza: {your_pizza_name}")
print(f"Price per pizza: ${your_pizza_price}")
print(f"Quantity: {your_quantity}")
print(f"Subtotal: ${your_subtotal:.2f}")
print(f"Tax (8%): ${your_tax:.2f}")
print(f"Total: ${your_total:.2f}")
print()


# ============================================================
# BONUS: Let's combine everything into a full order!
# ============================================================

# Create an order dictionary that contains everything
order = {
    "customer_name": "Adish",
    "pizza": my_custom_pizza,
    "quantity": 2,
    "delivery": True,
    "delivery_address": "123 Main Street"
}

# Calculate order total
order_subtotal = order["pizza"]["price"] * order["quantity"]
order_tax = order_subtotal * 0.08
delivery_fee = 3.99 if order["delivery"] else 0  # Add fee only if delivery
order_total = order_subtotal + order_tax + delivery_fee

print("=== BONUS: Complete Order ===")
print(f"Customer: {order['customer_name']}")
print(f"Pizza: {order['pizza']['name']} x{order['quantity']}")
print(f"Subtotal: ${order_subtotal:.2f}")
print(f"Tax: ${order_tax:.2f}")
print(f"Delivery Fee: ${delivery_fee:.2f}")
print(f"Grand Total: ${order_total:.2f}")
print(f"Delivering to: {order['delivery_address']}")
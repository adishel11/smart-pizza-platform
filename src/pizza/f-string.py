"""
🍕 f-string Practice
"""

# Your pizza order
pizza_name = "Hawaiian"
size = "large"
base_price = 14.99
quantity = 2
tax_rate = 0.08

# Calculate
subtotal = base_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# Print a beautiful receipt using f-strings
print("=" * 40)
print(f"{'PIZZA RECEIPT':^40}")  # Centered title
print("=" * 40)
print(f"{'Item':<20} {'Amount':>18}")
print("-" * 40)
print(f"{pizza_name + ' (' + size + ')':<20} ${base_price:>16.2f}")
print(f"{'Quantity':<20} {quantity:>18}")
print(f"{'Subtotal':<20} ${subtotal:>16.2f}")
print(f"{'Tax (8%)':<20} ${tax:>16.2f}")
print("-" * 40)
print(f"{'TOTAL':<20} ${total:>16.2f}")
print("=" * 40)
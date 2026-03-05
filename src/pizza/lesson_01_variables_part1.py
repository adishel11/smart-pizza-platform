"""
🍕 Smart Pizza Platform - Lesson 1.1: Variables & Data Types

Learning objectives:
- Understand what variables are
- Learn Python's core data types
- Practice creating and using variables
"""

# ============================================================
# STRINGS (str) - Text data, wrapped in quotes
# ============================================================

pizza_name = "Margherita"
description = 'Classic Italian pizza with fresh basil'  # Single or double quotes work

# String with multiple lines
menu_header = """
================================
🍕 SMART PIZZA PLATFORM 🍕
================================
"""

print(menu_header)
print(f"Today's Special: {pizza_name}")
print(f"Description: {description}")
print()

# ============================================================
# NUMBERS - int (whole) and float (decimal)
# ============================================================

# Integers - whole numbers
quantity = 2
calories = 850

# Floats - decimal numbers
price = 12.99
tax_rate = 0.08  # 8% tax

# Basic math
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("--- ORDER CALCULATION ---")
print(f"Pizza: {pizza_name}")
print(f"Price per pizza: ${price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"Tax (8%): ${tax:.2f}")           # :.2f means 2 decimal places
print(f"Total: ${total:.2f}")
print()

# ============================================================
# BOOLEANS (bool) - True or False
# ============================================================

is_vegetarian = True
is_spicy = False
has_gluten = True
is_available = True

print("--- PIZZA INFO ---")
print(f"Vegetarian: {is_vegetarian}")
print(f"Spicy: {is_spicy}")
print(f"Contains Gluten: {has_gluten}")
print()

# ============================================================
# LISTS - Ordered, changeable collections
# ============================================================

# A list of toppings
toppings = ["mozzarella", "tomato sauce", "fresh basil", "olive oil"]

print("--- TOPPINGS ---")
print(f"All toppings: {toppings}")
print(f"First topping: {toppings[0]}")      # Index starts at 0!
print(f"Last topping: {toppings[-1]}")      # -1 means last item
print(f"Number of toppings: {len(toppings)}")

# Add a topping
toppings.append("garlic")
print(f"After adding garlic: {toppings}")
print()

# ============================================================
# DICTIONARIES (dict) - Key-value pairs
# ============================================================

# A pizza as a dictionary
pizza = {
    "name": "Margherita",
    "price": 12.99,
    "size": "medium",
    "toppings": ["mozzarella", "tomato", "basil"],
    "is_vegetarian": True
}

print("--- PIZZA DICTIONARY ---")
print(f"Pizza name: {pizza['name']}")
print(f"Price: ${pizza['price']}")
print(f"Size: {pizza['size']}")
print(f"Toppings: {pizza['toppings']}")
print(f"Vegetarian: {pizza['is_vegetarian']}")
print()

# ============================================================
# TUPLES - Ordered but UNCHANGEABLE (immutable)
# ============================================================

# Good for fixed values that shouldn't change
sizes = ("small", "medium", "large", "extra-large")
print("--- AVAILABLE SIZES ---")
print(f"Sizes: {sizes}")
print(f"Default size: {sizes[1]}")  # medium
print()

# ============================================================
# SETS - Unique items only (no duplicates)
# ============================================================

# Customer's allergens (no duplicates allowed)
allergens = {"dairy", "gluten", "dairy"}  # "dairy" appears twice
print("--- ALLERGENS ---")
print(f"Unique allergens: {allergens}")   # Will show dairy only once!
print()

# ============================================================
# TYPE CHECKING - Find out what type a variable is
# ============================================================

print("--- TYPE CHECKING ---")
print(f"pizza_name is: {type(pizza_name)}")
print(f"price is: {type(price)}")
print(f"quantity is: {type(quantity)}")
print(f"is_vegetarian is: {type(is_vegetarian)}")
print(f"toppings is: {type(toppings)}")
print(f"pizza is: {type(pizza)}")
print(f"sizes is: {type(sizes)}")
print(f"allergens is: {type(allergens)}")

# ============================================================
# 🎯 YOUR TURN! Uncomment and complete these exercises:
# ============================================================

# Exercise 1: Create a new pizza
# your_pizza_name = ???
# your_pizza_price = ???
# your_pizza_toppings = ???

# Exercise 2: Create a complete pizza dictionary
# my_custom_pizza = {
#     "name": ???,
#     "price": ???,
#     "size": ???,
#     "toppings": ???,
#     "is_spicy": ???
# }

# Exercise 3: Calculate the total for 3 of your pizzas with 8% tax
# your_quantity = ???
# your_subtotal = ???
# your_tax = ???
# your_total = ???
# print(f"Total for {your_quantity} {your_pizza_name} pizzas: ${your_total:.2f}")
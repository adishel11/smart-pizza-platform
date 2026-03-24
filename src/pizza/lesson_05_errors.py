print("--- HANDLING AN ERROR ---")

try:
    number = int("hello")
    print(f"The number is: {number}")
except:
    print("Oops! That wasn't a valid number.")

print("Program continues running!")




print()
print("--- ERROR TYPES ---")

# ValueError - wrong type of value
try:
    number = int("pizza")
except ValueError:
    print("ValueError: Cannot convert 'pizza' to integer")

# ZeroDivisionError - dividing by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

# IndexError - list index out of range
try:
    pizzas = ["Margherita", "Pepperoni"]
    print(pizzas[10])
except IndexError:
    print("IndexError: That index doesn't exist")





print()
print("--- MULTIPLE ERROR TYPES ---")

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please use numbers only!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))





print()
print("--- TRY/EXCEPT/ELSE ---")

def convert_to_int(value):
    try:
        number = int(value)
    except ValueError:
        print(f"'{value}' is not a valid number")
    else:
        print(f"Success! Converted to {number}")

convert_to_int("42")
convert_to_int("pizza")




print()
print("--- TRY/EXCEPT/FINALLY ---")

def process_order(pizza_number):
    print(f"Processing order...")
    try:
        if pizza_number < 1:
            raise ValueError("Invalid pizza number")
        print(f"Order #{pizza_number} confirmed!")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting Smart Pizza!")
    print()

process_order(5)
process_order(-1)






print()
print("--- RAISING ERRORS ---")

def set_quantity(qty):
    if qty < 1:
        raise ValueError("Quantity must be at least 1")
    if qty > 100:
        raise ValueError("Maximum order is 100 pizzas")
    return qty

try:
    quantity = set_quantity(5)
    print(f"Quantity set to: {quantity}")
except ValueError as e:
    print(f"Invalid quantity: {e}")

try:
    quantity = set_quantity(0)
except ValueError as e:
    print(f"Invalid quantity: {e}")

try:
    quantity = set_quantity(200)
except ValueError as e:
    print(f"Invalid quantity: {e}")







print()
print("=" * 40)
print("BULLETPROOF INPUT SYSTEM")
print("=" * 40)

def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Please enter a valid number!")




print()
print("--- TEST: Get Integer ---")
age = get_integer("Enter your age: ")
print(f"Your age is: {age}")



def get_integer_in_range(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"❌ Please enter {min_val}-{max_val}")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number!")




print()
print("--- TEST: Get Integer in Range ---")
choice = get_integer_in_range("Pick a pizza (1-4): ", 1, 4)
print(f"You picked: {choice}")




def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower().strip()
        if answer in ["y", "yes"]:
            return True
        if answer in ["n", "no"]:
            return False
        print("❌ Please enter yes or no (y/n)")




print()
print("--- TEST: Yes/No ---")
wants_delivery = get_yes_no("Do you want delivery? (y/n): ")
if wants_delivery:
    print("🚗 Delivery selected!")
else:
    print("🏪 Pickup selected!")




print()
print("=" * 40)
print("🍕 COMPLETE BULLETPROOF SYSTEM 🍕")
print("=" * 40)

def main():
    pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]
    prices = [10.99, 12.99, 11.99, 13.99]
    
    print()
    print("--- MENU ---")
    for i, (pizza, price) in enumerate(zip(pizzas, prices)):
        print(f"  {i + 1}. {pizza:<15} ${price:.2f}")
    print()
    
    order = []
    
    while True:
        print("Enter pizza number (or 0 to finish)")
        choice = get_integer_in_range("Your choice: ", 0, len(pizzas))
        
        if choice == 0:
            break
        
        quantity = get_integer_in_range("How many? (1-10): ", 1, 10)
        
        pizza_name = pizzas[choice - 1]
        pizza_price = prices[choice - 1]
        
        order.append({
            "pizza": pizza_name,
            "price": pizza_price,
            "quantity": quantity
        })
        
        print(f"✓ Added {quantity}x {pizza_name}")
        print()
    
    if len(order) == 0:
        print("No order placed. Goodbye!")
        return
    
    wants_delivery = get_yes_no("Delivery? (y/n): ")
    delivery_fee = 3.99 if wants_delivery else 0.00
    
    print()
    print("=" * 40)
    print("         RECEIPT")
    print("=" * 40)
    
    subtotal = 0
    for item in order:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total
        print(f"  {item['quantity']}x {item['pizza']:<12} ${item_total:.2f}")
    
    tax = subtotal * 0.08
    total = subtotal + tax + delivery_fee
    
    print("-" * 40)
    print(f"  {'Subtotal:':<20} ${subtotal:.2f}")
    print(f"  {'Tax (8%):':<20} ${tax:.2f}")
    print(f"  {'Delivery:':<20} ${delivery_fee:.2f}")
    print("-" * 40)
    print(f"  {'TOTAL:':<20} ${total:.2f}")
    print("=" * 40)
    print()
    print("🍕 Thank you for your order!")

main()
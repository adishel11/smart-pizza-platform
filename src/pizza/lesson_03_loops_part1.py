pizzas = ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"]
prices = [10.99, 12.99, 11.99, 13.99]

print("--- MENU (Without Loop) ---")
print(pizzas[0])
print(pizzas[1])
print(pizzas[2])
print(pizzas[3])

print()
print("--- MENU (With Loop) ---")
for pizza in pizzas:
    print(pizza)

print()
print("--- MENU (With Numbers) ---")
for index, pizza in enumerate(pizzas):
    print(index, pizza)

print()
print("--- MENU (With Numbers) ---")
for index, pizza in enumerate(pizzas):
    print(f"{index + 1}. {pizza}")

print()
print("--- MENU (With Prices) ---")
for pizza, price in zip(pizzas, prices):
    print(f"{pizza}: ${price}")

print()
print("--- FULL MENU ---")
for index, (pizza, price) in enumerate(zip(pizzas, prices)):
    print(f"{index + 1}. {pizza:<15} ${price:.2f}")

print()
print("--- RANGE BASICS ---")
for i in range(5):
    print(i)

print()
print("--- RANGE (1 to 5) ---")
for i in range(1, 6):
    print(i)

print()
print("--- RANGE (counting by 2) ---")
for i in range(0, 10, 2):
    print(i)

print()
print("--- MENU (Using range) ---")
for i in range(len(pizzas)):
    print(f"{i + 1}. {pizzas[i]} - ${prices[i]}")

print()
print("--- PIZZA OVEN COUNTDOWN ---")
for seconds in range(5, 0, -1):
    print(f"{seconds}...")
print("🍕 Pizza is ready!")


print()
print("--- LEN() FUNCTION ---")
print(f"Number of pizzas: {len(pizzas)}")
print(f"Number of prices: {len(prices)}")

len([1, 2, 3])        # 3 (list)
len("Pizza")          # 5 (string - counts characters)
len({"a": 1, "b": 2}) # 2 (dictionary - counts keys)    

print()
print("--- SUM() FUNCTION ---")
print(f"All prices: {prices}")
total_of_all = sum(prices)
print(f"Sum of all prices: ${total_of_all:.2f}")

print()
print("--- MIN() and MAX() ---")
cheapest = min(prices)
expensive = max(prices)
print(f"Cheapest pizza: ${cheapest:.2f}")
print(f"Most expensive: ${expensive:.2f}")

print()
print("--- IN OPERATOR ---")
if "Pepperoni" in pizzas:
    print("Yes! We have Pepperoni")
if "Sushi" in pizzas:
    print("We have Sushi")
else:
    print("Sorry, no Sushi here!")

print()
if "Anchovies" not in pizzas:
    print("Good news: No anchovies on the menu!")

print()
print("--- ANY() and ALL() ---")
order_quantities = [2, 0, 3, 1]
if any(q > 0 for q in order_quantities):
    print("At least one item was ordered!")
if all(q > 0 for q in order_quantities):
    print("All items have quantity > 0")
else:
    print("Some items have zero quantity")

print()
print("--- SORTED() ---")
print(f"Original prices: {prices}")
print(f"Sorted (low to high): {sorted(prices)}")
print(f"Sorted (high to low): {sorted(prices, reverse=True)}")

print()
print("--- REVERSED() ---")
print("Pizzas in reverse order:")
for pizza in reversed(pizzas):
    print(f"  - {pizza}")

print()
print("=" * 40)
print("PART 3: WHILE LOOPS")
print("=" * 40)

print()
print("--- BASIC WHILE ---")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count = count + 1
print("Done counting!")

print()
print("--- SHORTHAND OPERATORS ---")
number = 10
print(f"Start: {number}")
number += 5
print(f"After += 5: {number}")
number -= 3
print(f"After -= 3: {number}")
number *= 2
print(f"After *= 2: {number}")



print()
print("--- PIZZA OVEN TIMER ---")
minutes_left = 3
while minutes_left > 0:
    print(f"⏱️  {minutes_left} minute(s) remaining...")
    minutes_left -= 1
print("🍕 DING! Pizza is ready!")



print()
print("--- WHILE TRUE WITH BREAK ---")
print("Type 'quit' to exit")
while True:
    user_input = input("Enter something: ")
    
    if user_input == "quit":
        print("Goodbye!")
        break  
    print(f"You typed: {user_input}")



print()
print("--- CONTINUE (Skip Invalid) ---")
print("Enter pizza numbers 1-4 (type 'done' to finish)")
order_count = 0
while True:
    choice = input("Pizza number: ")
    if choice == "done":
        break   
    choice = int(choice)  
    if choice < 1 or choice > 4:
        print("❌ Invalid! Enter 1-4 only.")
        continue  
    order_count += 1
    print(f"✓ Added pizza #{choice}")
print(f"Total pizzas ordered: {order_count}")




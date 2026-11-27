# Lesson 18 · Functions: reusable recipes
# def makes a function. Like a Scratch "My Block": write it once, use it many times.
# Run it:  python 18_functions.py

# 1. A function with no inputs
def say_welcome():
    print("Welcome to Mama Put Kitchen!")

say_welcome()          # call it: () runs the function
say_welcome()

# 2. Parameters: inputs the function needs
def greet(name):
    print(f"Hello, {name}!")

greet("Kemi")
greet("Yusuf")

# 3. Several parameters, and a default value
def delivery_fee(distance_km, express=False):
    fee = 500 if distance_km <= 3 else 1000
    if express:
        fee += 700
    return fee         # return: send the answer back to whoever called the function

print(delivery_fee(2))                # 500
print(delivery_fee(8, express=True))  # 1700

# 4. Use the returned value in your own code
def add_vat(price):
    """Return the price with 7.5% VAT added."""
    return price * 1.075

total = add_vat(10000) + delivery_fee(5)
print(f"Total: ₦{total}")

# print vs return: print SHOWS a value; return GIVES it back so you can keep using it.

# ── TRY IT YOURSELF ──
# 1. Write a function square(n) that returns n * n. Print square(4) and square(9).
# 2. Write a function is_adult(age) that returns True or False.
# 3. Write a function naira_to_dollars(naira, rate=1500) that returns the amount in dollars, rounded to 2 decimals.

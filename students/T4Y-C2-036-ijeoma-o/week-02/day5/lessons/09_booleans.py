# Lesson 9 · Booleans: True or False
# A bool has only two values: True and False (capital T and F).
# Run it:  python 09_booleans.py

is_open = True
has_paid = False
print(is_open, has_paid)
print(type(is_open))

# Comparisons always give a bool
age = 19
print(age >= 18)      # True
print(age == 21)      # False

balance = 4500
price = 6000
can_buy = balance >= price
print("Can I buy it?", can_buy)

# Text comparisons are exact: capitals matter
print("abuja" == "Abuja")   # False

# ── TRY IT YOURSELF ──
# 1. Make a variable is_raining and set it to True or False. Print it.
# 2. data_left = 1.2 (GB). Print whether data_left is less than 2.
# 3. Predict, then check: print(10 > 3), print(3 == 3.0), print("cat" == "Cat")

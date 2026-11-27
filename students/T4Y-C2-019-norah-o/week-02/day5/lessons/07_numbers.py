# Lesson 7 · Numbers: int and float
# int   = a whole number:   25, -3, 150000
# float = a decimal number: 2.5, 0.075, 99.99
# Run it:  python 07_numbers.py

bags_of_rice = 3          # int
price_per_kg = 1250.50    # float

print(type(bags_of_rice))
print(type(price_per_kg))

# Maths works like a calculator
print(10 + 3)    # add
print(10 - 3)    # subtract
print(10 * 3)    # multiply
print(10 / 3)    # divide: always gives a float

# round(number, digits) tidies up long decimals
print(round(10 / 3, 2))

# Big numbers: you can use _ to make them easier to read. Python ignores it.
population = 3_600_000
print(population)

# ── TRY IT YOURSELF ──
# 1. Make variables for the price of one bottle of water (₦300) and how many you buy (12). Print the total.
# 2. Print 7 / 2. Is the answer an int or a float? Check with type().
# 3. Your phone has 64.5 GB used of 128 GB. Print the free space, rounded to 1 decimal.

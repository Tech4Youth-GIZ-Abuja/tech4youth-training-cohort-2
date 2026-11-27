# Lesson 10 · Converting types and reading input
# input() waits for the user to type, and ALWAYS gives a string (text).
# Run it:  python 10_type_conversion.py
# Example answers: Amina | 22 | 1500.50

name = input("What is your name? ")
age_text = input("How old are you? ")
print(type(age_text))            # str, even though you typed a number!

# Convert the text to a number before doing maths
age = int(age_text)              # int()   → whole number
print(f"Next year you will be {age + 1}.")

price = float(input("Price of a meal in naira? "))   # float() → decimal number
print(f"Two meals cost {price * 2}.")

# str() turns a number into text, so you can join it with +
print("Name: " + name + ", age: " + str(age))

# Other conversions
print(int(3.9))        # 3: int() cuts off the decimals, it does not round
print(float(7))        # 7.0
print(bool(0), bool(5), bool(""), bool("hi"))   # 0 and empty text are False

# ── TRY IT YOURSELF ──
# 1. Ask for two numbers with input(). Print their sum. (Did you get 55 instead of 10? Use int().)
# 2. Ask for a temperature in °C. Print it in °F: f = c * 9 / 5 + 32
# 3. What happens if you type "abc" when the program expects a number? Read the error.

# Lesson 3 · Python errors: reading the red text
# Errors are normal. They are Python telling you exactly what it did not understand.
# How to read one: start at the LAST line (what went wrong), then look at the line number (where).
# Run it:  python 03_errors.py

print("This line runs fine.")

# Remove the # in front of ONE line at a time, run the file, read the error, then put the # back.

# print(nme)                 # NameError: Python doesn't know a variable called nme
# print("Age: " + 25)        # TypeError: you can't add text and a number
# print(int("twenty"))       # ValueError: "twenty" is not a number Python can read
# print(10 / 0)              # ZeroDivisionError: you can't divide by zero
# print("Hello"              # SyntaxError: a bracket was opened but never closed

# ── TRY IT YOURSELF ──
# 1. Turn on each broken line one at a time. Write down the error name (the word before the colon).
# 2. Fix each line so it works. Hint for the TypeError: print("Age:", 25)
# 3. Make your own mistake on purpose and ask a classmate to find it.

# Lesson 12 · String manipulation: working with text
# A method is a tool that belongs to a value. You use it with a dot: text.upper()
# Run it:  python 12_string_methods.py

name = "  ada okafor  "

# f-strings: put variables inside text with { }
city = "Jos"
print(f"Welcome, {name.strip()} from {city}!")

# Clean up and change case
print(name.strip())          # "ada okafor"   removes spaces at the start and end
print(name.strip().title())  # "Ada Okafor"   capital first letters
print(name.upper())          # "  ADA OKAFOR  "
print(name.lower())

# Search
message = "Do you deliver to Wuse?"
print("deliver" in message)            # True: is this word inside?
print(message.startswith("Do"))        # True
print(message.endswith("?"))           # True
print(message.find("Wuse"))            # 18: the position where it starts (-1 if not found)
print(message.count("o"))              # how many times "o" appears

# Change
print(message.replace("Wuse", "Garki"))
print("-" * 20)                        # repeat text 20 times

# Split text into a list of words
print("rice,beans,garri".split(","))

# ── TRY IT YOURSELF ──
# 1. Ask the user for their name with input(). Print it in capitals and in title case.
# 2. Make phone = "0803 123 4567". Remove the spaces with replace(). Print how long it is with len().
# 3. Make an f-string receipt line:  item = "Suya", price = 1500  →  "Suya ........ ₦1500"

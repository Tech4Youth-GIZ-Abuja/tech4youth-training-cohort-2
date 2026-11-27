# Lesson 8 · Strings: text
# A string is text inside quotes. Python calls the type str.
# Run it:  python 08_strings.py

first_name = "Chidi"
city = 'Enugu'
message = "I'm learning Python"      # use " " when the text contains '

print(first_name)
print(type(first_name))

# Join strings with +
full = first_name + " from " + city
print(full)

# len() counts the characters (letters, spaces and symbols)
print(len(first_name))

# Each character has a position (index). Counting starts at 0!
print(first_name[0])     # C
print(first_name[-1])    # i  (negative counts from the end)

# A number inside quotes is text, not a number
print("5" + "5")         # 55, not 10

# ── TRY IT YOURSELF ──
# 1. Make a variable with your full name. Print how many characters it has.
# 2. Print the first letter of your name and the last letter.
# 3. Join your first name and your city with + so it prints like: Amina - Kano

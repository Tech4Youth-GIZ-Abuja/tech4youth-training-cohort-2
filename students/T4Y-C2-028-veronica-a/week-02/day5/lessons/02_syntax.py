# Lesson 2 · Python syntax: the spelling and grammar rules
# Run it:  python 02_syntax.py

# Rule 1: Python is case-sensitive. print works, Print does not.
print("Rule 1: small letters for print")

# Rule 2: text goes inside matching quotes: "..." or '...'
print('Rule 2: single quotes work too')

# Rule 3: every opening bracket ( needs a closing bracket )
print("Rule 3:", 10 + 5)

# Rule 4: one instruction per line
city = "Abuja"
print("Rule 4: I live in", city)

# Rule 5: a line ending in a colon : starts a block.
#         The lines inside the block are indented with 4 spaces.
if city == "Abuja":
    print("Rule 5: these lines are inside the if block")
    print("        because they start with 4 spaces")
print("This line is outside the block again")

# ── TRY IT YOURSELF ──
# 1. Each line below breaks one rule. Remove the # in front of ONE line, run it, read the error, then fix it.
# Print("Hello")
# print("Hello)
# print("Hello"
# 2. Change city to "Lagos". Which lines stop printing? Why?
# 3. Remove the 4 spaces in front of one line inside the if block. What error do you get?

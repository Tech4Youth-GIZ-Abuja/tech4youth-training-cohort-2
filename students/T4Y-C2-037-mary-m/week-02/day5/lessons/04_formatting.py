# Lesson 4 · Code formatting: make it easy to read
# Python doesn't care about most spaces between words, but PEOPLE do.
# Run it:  python 04_formatting.py

# Messy (works, but hard to read):
price=2500;qty=3;total=price*qty;print(total)

# Clean (same result, easy to read):
price = 2500
quantity = 3
total = price * quantity
print(total)

# The style rules most Python programmers follow (called PEP 8):
#  - one space on each side of = + - * /
#  - one instruction per line
#  - names in snake_case: small letters with _ between words
#  - 4 spaces for indentation (VS Code does this when you press Tab)
#  - a blank line between parts of your program

# ── TRY IT YOURSELF ──
# 1. Rewrite this messy line as clean code on 4 lines:  a=100;b=250;c=a+b;print(c)
# 2. Give a, b and c better names that say what they mean (e.g. rice_price).
# 3. In VS Code, right-click → Format Document. What changed?

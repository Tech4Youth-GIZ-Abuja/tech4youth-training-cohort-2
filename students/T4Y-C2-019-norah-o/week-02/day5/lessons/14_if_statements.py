# Lesson 14 · If statements: making decisions
# Run it:  python 14_if_statements.py

temperature = 34

# if: run the block only when the condition is True
if temperature > 30:
    print("It's hot. Drink water!")

# if / else: one of two paths
battery = 15
if battery < 20:
    print("Low battery. Plug in your phone.")
else:
    print("Battery is fine.")

# if / elif / else: many paths. Python checks from top to bottom and stops at the FIRST True one.
score = 72
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} → grade {grade}")

# Combine conditions with and / or
age = 25
has_bvn = True
if age >= 18 and has_bvn:
    print("You can open a bank account.")

# Inside a loop: check every number
for n in range(1, 7):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# ── TRY IT YOURSELF ──
# 1. Ask for an age. Print "Adult" if it is 18 or more, otherwise print "Young person".
# 2. Ask for a number. Print whether it is positive, negative or zero (use if / elif / else).
# 3. Ticket prices: under 5 free, 5 to 17 ₦1000, 18 and over ₦2500. Ask for an age and print the price.

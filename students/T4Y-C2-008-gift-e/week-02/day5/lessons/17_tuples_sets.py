# Lesson 17 · Tuples and sets
# Run it:  python 17_tuples_sets.py

# ── Tuple ( ): like a list, but it can NOT be changed after you make it ──
# Use it for values that belong together and should stay fixed.
abuja = (9.0765, 7.3986)          # latitude, longitude
print(abuja[0])

days = ("Mon", "Tue", "Fri")      # our class days
print(len(days))

lat, lon = abuja                  # unpack: put each value in its own variable
print(f"Latitude {lat}, longitude {lon}")

# days[0] = "Wed"   ← TypeError: tuples can't be changed

# ── Set { }: no order, and NO duplicates ──
# Use it to remove repeats or to check membership quickly.
signups = ["Ada", "Musa", "Ada", "Ngozi", "Musa"]
unique = set(signups)
print(unique)                     # each name only once (order may differ)
print(len(unique), "different people signed up")

class_a = {"Ada", "Musa", "Ngozi"}
class_b = {"Musa", "Tunde"}
print(class_a & class_b)          # in BOTH: {'Musa'}
print(class_a | class_b)          # in EITHER (all names)

# ── Which one do I use? ──
# list  [ ]  ordered, can change, duplicates OK     → a shopping list
# tuple ( )  ordered, can NOT change                → coordinates, days of the week
# set   { }  no order, no duplicates                → unique visitors
# dict  {k: v} look up by key                       → a price list

# ── TRY IT YOURSELF ──
# 1. Make a tuple with your birthday: (day, month, year). Unpack it into 3 variables and print them.
# 2. Make a list of 6 colours with some repeats. Use set() to print each colour once.
# 3. Make two sets of foods you and a friend like. Print the foods you BOTH like with &.

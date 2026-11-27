# Lesson 16 · Dictionaries: look things up by name
# A dictionary stores pairs: key → value. Like a real dictionary: word → meaning.
# Run it:  python 16_dictionaries.py

menu = {
    "jollof": 2500,
    "fried rice": 2500,
    "chicken": 1500,
}
print(menu)

# Look up a value by its key
print(menu["jollof"])            # 2500

# .get() is safer: it gives None (or your default) if the key is missing
print(menu.get("pizza"))         # None
print(menu.get("pizza", 0))      # 0

# Add, change and remove
menu["plantain"] = 700           # add a new pair
menu["chicken"] = 1800           # change a value
del menu["fried rice"]           # remove a pair
print(menu)

print("jollof" in menu)          # True: checks the KEYS

# Loop through all pairs
for food, price in menu.items():
    print(f"{food}: ₦{price}")

# A dictionary can describe one thing with many details
student = {"name": "Bola", "age": 23, "city": "Ibadan"}
print(f"{student['name']} is {student['age']} and lives in {student['city']}.")

# ── TRY IT YOURSELF ──
# 1. Make a dictionary about you: name, city and favourite food. Print each value.
# 2. Make a dictionary of 3 states and their capitals. Ask the user for a state and print its capital with .get().
# 3. Add 1 new food to menu, then print the total price of everything on the menu.

# Lesson 15 · Lists: many values in one variable, in order
# Run it:  python 15_lists.py

foods = ["jollof", "suya", "puff-puff"]
print(foods)
print(len(foods))          # 3 items

# Get an item by its position (index). Counting starts at 0.
print(foods[0])            # jollof
print(foods[-1])           # puff-puff (the last one)

# Change, add and remove
foods[1] = "pepper soup"   # replace position 1
foods.append("moi moi")    # add to the end
foods.remove("jollof")     # remove by value
print(foods)

# Is it in the list?
print("suya" in foods)     # False now

# Loop through a list
prices = [2500, 1500, 800]
total = 0
for p in prices:
    total += p
print("Total:", total)

# Handy tools
print(sum(prices), min(prices), max(prices))
print(sorted(prices))      # a sorted copy: [800, 1500, 2500]

# ── TRY IT YOURSELF ──
# 1. Make a list of 4 friends. Print the first and the last name.
# 2. Add one more friend with append(). Print how many friends are in the list now.
# 3. Make a list of 5 test scores. Print the highest, the lowest and the average (sum ÷ len).

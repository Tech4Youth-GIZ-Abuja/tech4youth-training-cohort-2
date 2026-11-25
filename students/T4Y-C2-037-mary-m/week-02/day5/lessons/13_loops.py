# Lesson 13 · Loops: repeat without copying
# Run it:  python 13_loops.py

# for + range: repeat a set number of times
for i in range(3):          # 0, 1, 2
    print("Hello", i)

for i in range(1, 6):       # 1 to 5: the end number is NOT included
    print(f"5 x {i} = {5 * i}")

# for can walk through text (and lists, in Lesson 15) one item at a time
for letter in "ABUJA":
    print(letter)

# while: repeat WHILE a condition is True
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1          # without this line, the loop never ends!
print("Lift off!")

# break: leave a loop early
total = 0
for day in range(1, 31):
    total += 500            # save ₦500 a day
    if total >= 5000:
        print(f"Reached ₦5,000 on day {day}")
        break

# Stuck in a loop that never ends? Press Ctrl + C in the terminal.

# ── TRY IT YOURSELF ──
# 1. Print the numbers 1 to 10 with a for loop.
# 2. Print the 7 times table (7 x 1 = 7 … 7 x 12 = 84).
# 3. With a while loop, double the number 1 until it is bigger than 1000. Print each step.

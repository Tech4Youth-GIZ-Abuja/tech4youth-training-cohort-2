# Lab 7 · Loops: a times table and a savings plan
# Example answers: 7 | 2000

number = int(input("Which times table? "))
for i in range(1, 13):                  # 1 to 12
    print(f"{number} x {i} = {number * i}")

# while: how many weeks to save ₦20,000?
weekly = int(input("How much can you save each week? "))
saved = 0
weeks = 0
while saved < 20000:
    saved += weekly
    weeks += 1
print(f"You reach ₦20,000 after {weeks} weeks (₦{saved:,} saved).")

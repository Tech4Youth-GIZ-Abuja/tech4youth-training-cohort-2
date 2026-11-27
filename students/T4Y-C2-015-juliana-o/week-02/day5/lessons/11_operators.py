# Lesson 11 · Operators: doing maths, comparing and combining
# Run it:  python 11_operators.py

# ── Arithmetic ──
print(17 + 5)    # 22  add
print(17 - 5)    # 12  subtract
print(17 * 5)    # 85  multiply
print(17 / 5)    # 3.4 divide (always a float)
print(17 // 5)   # 3   floor division: how many whole times 5 fits in 17
print(17 % 5)    # 2   modulo: the remainder
print(2 ** 3)    # 8   power: 2 × 2 × 2

# Real example: 17 chin-chin packs shared into boxes of 5
packs = 17
print("Full boxes:", packs // 5, "| Left over:", packs % 5)

# ── Order of operations: brackets first, then ** , then * / // %, then + - ──
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20

# ── Comparison: the answer is True or False ──
print(5 == 5, 5 != 3, 7 > 2, 7 < 2, 5 >= 5, 4 <= 3)

# ── Logical: combine True/False ──
age = 20
has_id = True
print(age >= 18 and has_id)    # and: BOTH must be True
print(age < 13 or age > 65)    # or: at least ONE must be True
print(not has_id)              # not: flips True ↔ False

# ── Assignment shortcuts ──
balance = 5000
balance += 2000     # same as balance = balance + 2000
balance -= 1500     # same as balance = balance - 1500
balance *= 2        # same as balance = balance * 2
print(balance)

# ── TRY IT YOURSELF ──
# 1. 100 minutes is how many hours and minutes? Use // and %.
# 2. Is 2026 an even number? Use % 2 (even numbers have remainder 0).
# 3. A club lets you in if you are 18 or older AND have a ticket. Make age and has_ticket and print the answer.

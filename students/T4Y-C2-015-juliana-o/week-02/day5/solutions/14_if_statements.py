# Solutions · Lesson 14 · If statements
# Example answers: 20 | -4 | 12
# 1.
age = int(input("Age: "))
if age >= 18:
    print("Adult")
else:
    print("Young person")
# 2.
n = float(input("A number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
# 3.
age = int(input("Age for the ticket: "))
if age < 5:
    price = 0
elif age <= 17:
    price = 1000
else:
    price = 2500
print(f"Ticket: ₦{price}")

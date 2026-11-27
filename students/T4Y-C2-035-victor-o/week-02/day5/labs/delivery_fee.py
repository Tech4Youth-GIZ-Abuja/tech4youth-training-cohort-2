# Lab 8 · If statements: a delivery price calculator for a small food business
# Example answers: 6500 | 7 | no

price = float(input("Food price in naira: "))
distance = float(input("Distance in km: "))
express = input("Express delivery? (yes/no) ").strip().lower() == "yes"

if distance <= 3:
    delivery = 500
elif distance <= 10:
    delivery = 1000
else:
    delivery = 2000

if express:
    delivery += 700

total = price + delivery
print(f"Delivery fee: ₦{delivery:,.0f}")
print(f"Total to pay: ₦{total:,.0f}")

if total > 10000:
    print("You get a free drink!")

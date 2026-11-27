# Lab 9 · Shop menu: a dictionary for the prices, a list for the order
# Example answers: jollof | chicken | pizza | done

menu = {"jollof": 2500, "fried rice": 2500, "chicken": 1500, "plantain": 700, "zobo": 500}
order = []

print("Today's menu:")
for food, price in menu.items():
    print(f"  {food:<12} ₦{price:,}")

while True:
    choice = input("Add an item (or type done): ").strip().lower()
    if choice == "done":
        break
    if choice in menu:
        order.append(choice)
        print(f"  Added {choice}")
    else:
        print("  Sorry, that's not on the menu.")

total = 0
for item in order:
    total += menu[item]

print(f"Your order: {', '.join(order)}")
print(f"{len(order)} items. Total: ₦{total:,}")

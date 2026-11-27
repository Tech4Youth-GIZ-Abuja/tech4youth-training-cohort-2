# Lab 5 · Split the bill: arithmetic, comparison and logical operators
# Example answers: 18500 | 4 | 10

bill = float(input("Total bill in naira: "))
people = int(input("How many people? "))
tip_percent = float(input("Tip in percent (e.g. 10): "))

tip = bill * tip_percent / 100
total = bill + tip
each = total // people           # whole naira per person
left_over = total % people       # what is left after everyone pays the same

print(f"Tip: ₦{tip:,.0f}")       # :,.0f adds commas and shows no decimals
print(f"Total with tip: ₦{total:,.0f}")
print(f"Each person pays: ₦{each:,.0f}")
print(f"Left over for the host: ₦{left_over:,.0f}")

big_group = people >= 6
expensive = each > 5000
print("Ask for a group discount?", big_group or expensive)

# Solutions · Lesson 12 · String manipulation
# Example answers: emeka obi
# 1.
name = input("Your name: ")
print(name.upper())               # EMEKA OBI
print(name.title())               # Emeka Obi
# 2.
phone = "0803 123 4567"
digits = phone.replace(" ", "")
print(digits, len(digits))        # 08031234567 11
# 3.
item = "Suya"
price = 1500
print(f"{item} ........ ₦{price}")

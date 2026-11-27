# Solutions · Lesson 16 · Dictionaries
# Example answers: Kaduna
# 1.
me = {"name": "Amina", "city": "Abuja", "food": "jollof rice"}
print(me["name"], me["city"], me["food"])
# 2.
capitals = {"Lagos": "Ikeja", "Kaduna": "Kaduna", "Rivers": "Port Harcourt"}
state = input("Which state? ")
print(capitals.get(state, "I don't know that one yet"))
# 3.
menu = {"jollof": 2500, "chicken": 1800, "plantain": 700}
menu["moi moi"] = 600
total = 0
for price in menu.values():
    total += price
print(total)                      # 5600  (or simply: sum(menu.values()))

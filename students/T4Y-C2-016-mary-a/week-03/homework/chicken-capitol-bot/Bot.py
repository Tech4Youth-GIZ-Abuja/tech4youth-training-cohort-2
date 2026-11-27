menu={
    "grilled chicken": {"price": 4500, "available": True},
    "large combo": {"price": 7500, "available": True},
    "spicy wings": {"price": 2500, "available": False},
    "family fries": {"price": 2000, "available": True},
}
hours = "Monday to Thursday 9am to 11pm, Friday to Sunday 10am to 11:59pm"
address = "Chicken Capitol, No 4 Lingu Cresent Wuse 2"


def get_reply(message):
    text = message.lower()

    if "open" in text or "hours" in text or "close" in text:
        return "We are open " + hours + "."
    if "where" in text or "location" in text or "address" in text:
        return "You can find us at " + address + "."
    if "deliver" in text:
        return "Yes, we deliver. Please share your area and a staff member will confirm."
    if "cold" in text or "complain" in text or "bad" in text:
        return "I am sorry about that. Please send your order number and a manager will contact you."
    for item in menu:
        if item in text:
            if not menu[item]["available"]:
                return item + " is out of stock today."
            if "order" in text or "want" in text:
                return "Order: " + item + " at " + str(menu[item]["price"]) + " naira. A staff member will confirm it."
            return item + " is available. Price: " + str(menu[item]["price"]) + " naira."
    return "Sorry, I am not sure. A staff member will get back to you."


print("Chicken Capitol Assistant. Type quit to stop.")
while True:
    message = input("You: ")
    if message == "quit":
        break
    print("Bot:", get_reply(message))
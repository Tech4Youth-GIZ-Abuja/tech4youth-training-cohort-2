# Lab 10 · Tolu, the rule bot: functions + a dictionary + a loop
# The Scratch mini chatbot, rebuilt in Python. On Friday we replace the rules with a real AI model.
# Example answers: hello | what is on the menu? | when are you open | do you sell pizza | bye

ANSWERS = {
    "menu": "Jollof ₦2,500 · Fried rice ₦2,500 · Chicken ₦1,500",
    "open": "We are open 8am to 9pm, Monday to Saturday.",
    "deliver": "Yes! Delivery is ₦500 within 3 km.",
}


def clean(text):
    """Small letters, no extra spaces, no question mark."""
    return text.lower().strip().replace("?", "")


def reply(message):
    """Return Tolu's answer to one message."""
    words = message.split()
    if "hello" in words or "hi" in words:
        return "Hello! How can I help you today?"
    for keyword, answer in ANSWERS.items():
        if keyword in message:
            return answer
    return "Sorry, I don't understand. Try asking about the menu, opening time or delivery."


print("Tolu: Hi! I'm Tolu from Mama Put Kitchen. Type 'bye' to leave.")
count = 0
while True:
    message = clean(input("You: "))
    if message == "bye":
        print(f"Tolu: Bye! Thanks for the {count} messages. Come again.")
        break
    count += 1
    print("Tolu:", reply(message))

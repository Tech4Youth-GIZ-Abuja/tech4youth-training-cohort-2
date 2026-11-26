from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This function decides how JoyBot responds
def chatbot_response(message):
    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to JoyBot. How can I help you today?"

    elif "your name" in message:
        return "My name is JoyBot, your friendly chat assistant!"

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "who created you" in message:
        return "I was created by Joy using HTML, CSS, JavaScript and Python."

    elif "what can you do" in message:
        return "I can chat with you and answer simple questions."

    elif "thank" in message:
        return "You're welcome! Happy to help."

    elif "bye" in message:
        return "Goodbye! Have a wonderful day!"

    else:
        return "I'm still learning! Could you ask me something else?"


# Display the chatbot webpage
@app.route("/")
def home():
    return render_template("index.html")


# Receive messages and return chatbot responses
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({"reply": "Please enter a message."}), 400

    reply = chatbot_response(user_message)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)

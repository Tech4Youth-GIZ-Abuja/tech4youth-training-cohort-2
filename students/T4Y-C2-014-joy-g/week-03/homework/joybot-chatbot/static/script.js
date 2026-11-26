// Get HTML elements
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const clearButton = document.getElementById("clear-chat");

// Welcome message
const welcomeMessage =
    "Hello! 👋 I'm JoyBot. How can I help you today?";

// Function to display messages
function displayMessage(message, sender) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add(sender + "-message");
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);

    // Scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Listen for form submission
chatForm.addEventListener("submit", async function(event) {
    event.preventDefault();

    const message = userInput.value.trim();

    if (!message) return;

    // Display the user's message
    displayMessage(message, "user");

    // Clear the input field
    userInput.value = "";

    try {
        // Send message to Python backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.reply || "Something went wrong.");
        }

        // Display JoyBot's response
        displayMessage(data.reply, "bot");

    } catch (error) {
        displayMessage(
            "Sorry, I couldn't connect to the server. Please try again.",
            "bot"
        );
    }
});

// Clear the conversation
clearButton.addEventListener("click", function() {
    chatBox.innerHTML = "";

    displayMessage(welcomeMessage, "bot");
});

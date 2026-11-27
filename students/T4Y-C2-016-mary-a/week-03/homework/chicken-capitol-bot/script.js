// This Contains menu, prices, hours and address
const menu = {
  "grilled chicken": { price: 4500, available: true },
  "large combo": { price: 7500, available: true },
  "spicy wings": { price: 2500, available: false },
  "family fries": { price: 2000, available: true }
};
const hours = "Monday to Thursday 9am to 11pm, Friday to Sunday 10am to 11:59pm";
const address = "Chicken Capitol, No 4 Lingu Cresent Wuse 2";

function getReply(message) {
  const text = message.toLowerCase();

  if (text.includes("open") || text.includes("hours") || text.includes("close")) {
    return "We are open " + hours + ".";
  }
  if (text.includes("where") || text.includes("location") || text.includes("address")) {
    return "You can find us at " + address + ".";
  }
  if (text.includes("deliver")) {
    return "Yes, we deliver. Please share your area and a staff member will confirm.";
  }
  if (text.includes("cold") || text.includes("complain") || text.includes("bad")) {
    return "I am sorry about that. Please send your order number and a manager will contact you.";
  }
  for (const item in menu) {
    if (text.includes(item)) {
      if (!menu[item].available) {
        return item + " is out of stock today.";
      }
      if (text.includes("order") || text.includes("want")) {
        return "Order: " + item + " at " + menu[item].price + " naira. A staff member will confirm it.";
      }
      return item + " is available. Price: " + menu[item].price + " naira.";
    }
  }
  return "Sorry, I am not sure. A staff member will get back to you.";
}

function addLine(who, words) {
  const chat = document.getElementById("chat");
  const line = document.createElement("p");
  const label = document.createElement("b");

  label.textContent = who + ": ";
  line.append(label, document.createTextNode(words));
  chat.appendChild(line);
}

function sendMessage() {
  const box = document.getElementById("userInput");
  const message = box.value.trim();
  if (message === "") { return; }

  addLine("You", message);
  addLine("Bot", getReply(message));
  box.value = "";
}
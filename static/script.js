document.getElementById("send-btn").addEventListener("click", function() {
    let inputField = document.getElementById("user-input");
    let userMessage = inputField.value;
    if (userMessage.trim() === "") return;
    displayMessage(userMessage, "user");
    inputField.value = "";
    
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, "bot");
    })
    .catch(error => console.error("Error:", error));
});

function displayMessage(message, sender) {
    let chatBox = document.getElementById("chat-box");
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    if (sender === "user") {
        messageDiv.classList.add("user-message");
    } else {
        messageDiv.classList.add("bot-message");
    }
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

function sendMessage() {
    const inputField = document.getElementById('user-input');
    const messageText = inputField.value.trim();

    if (messageText === '') return;

    appendMessage(messageText, 'user-message');
    inputField.value = '';

    setTimeout(() => {
        appendMessage("Bot: Thank you for asking! Backend will connect soon.", 'bot-message');
    }, 600);
}

function appendMessage(text, className) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    messageElement.innerText = text;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// static/js/chatbot.js
document.getElementById('sendMessage').onclick = function() {
    const userMessage = document.getElementById('userMessage').value;
    const chatbox = document.getElementById('chatbox');

    // Check if the user message is not empty
    if (userMessage.trim() !== "") {
        // Display user message
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user'; // User message class
        userMessageDiv.textContent = userMessage;
        chatbox.appendChild(userMessageDiv);

        // Clear the input field immediately after sending the message
        document.getElementById('userMessage').value = '';

        // Send message to Flask backend
        fetch('/chat', {  // Ensure this URL matches your Flask route
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => {
            console.log('Response received:', response);
            return response.json();
        })
        .then(data => {
            console.log('Data received from server:', data);  // Log server response
            
            // Show "Bot is typing..." message
            const thinkingMessageDiv = document.createElement('div');
            thinkingMessageDiv.className = 'message bot'; // Bot message class
            thinkingMessageDiv.textContent = 'typing...'; // Temporary thinking message
            chatbox.appendChild(thinkingMessageDiv); // Append thinking message
            
            // Simulate bot thinking time with a delay
            setTimeout(() => {
                // Remove the thinking message
                chatbox.removeChild(thinkingMessageDiv);

                // Display chatbot response after a delay
                const botMessageDiv = document.createElement('div');
                botMessageDiv.className = 'message bot'; // Bot message class
                botMessageDiv.textContent = data.response; // Bot response text
                chatbox.appendChild(botMessageDiv); // Append bot response
                
                // Scroll to the bottom of messages
                chatbox.scrollTop = chatbox.scrollHeight; // Keep chatbox scrolled to bottom
            }, 1000); // Adjust the delay time (in milliseconds) as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
};

// Toggle chat window visibility
document.getElementById('toggleChat').onclick = function() {
    const chatBox = document.getElementById('chatbox');
    const chatInput = document.getElementById('chatInputArea');

    // Toggle visibility of chatbox and input area
    chatBox.classList.toggle('hidden'); // Toggle visibility of the chatbox
    chatInput.classList.toggle('minimized'); // Toggle visibility of the input area

    // Update toggle button text based on visibility
    const isHidden = chatBox.classList.contains('hidden');
    this.textContent = isHidden ? '+' : '-';
};

// Handle pressing "Enter" key to send a message
document.getElementById('userMessage').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        document.getElementById('sendMessage').click(); // Trigger send message button
    }
});

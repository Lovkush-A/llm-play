async function generateText() {
    const userInput = document.getElementById('userInput').value;
    const pretrainedResult = document.getElementById('pretrainedResult');
    const chatbotResult = document.getElementById('chatbotResult');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput })
        });

        const data = await response.json();
        
        pretrainedResult.innerHTML = data.pretrained.replace(/\n/g, '<br>');
        chatbotResult.innerHTML = data.chatbot.replace(/\n/g, '<br>');
    } catch (error) {
        console.error('Error:', error);
    }
} 
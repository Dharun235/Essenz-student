document.getElementById('prompt-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const prompt = document.getElementById('prompt').value;
    
    fetch('/get_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response-text').textContent = data.answer;
    })
    .catch(error => console.error('Error:', error));
});

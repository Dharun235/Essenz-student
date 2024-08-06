from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Initialize the Hugging Face pipeline
pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-8B-Instruct")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.json
    prompt = data['prompt']
    
    # Generate the response using the pipeline
    response = pipe(prompt, max_length=500, num_return_sequences=1)
    response_text = response[0]['generated_text']
    
    return jsonify({'answer': response_text})

if __name__ == '__main__':
    app.run(debug=True)

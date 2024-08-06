# Essenz Student

A web application for prompt-based answering using the Llama model from Hugging Face.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/essenz_student.git
   cd essenz_student
2. Create a virtual environment and activate it:
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install the dependencies:
    pip install -r requirements.txt
4. Run the Flask app:
    python app.py
5. Open your browser and go to http://127.0.0.1:5000/.
6. To run the unit tests: 
    python -m unittest discover


### Instructions
1. **Clone the Repository**: Clone the repository from GitHub.
2. **Create Virtual Environment**: Set up a virtual environment for Python dependencies.
3. **Install Dependencies**: Install the required dependencies listed in `requirements.txt`.
4. **Run Flask App**: Start the Flask app by running `app.py`.
5. **Run Unit Tests**: Execute unit tests to ensure the application works as expected.

 This setup uses the Hugging Face `InferenceClient` to query the Llama model and provide answers based on user prompts. Make sure to replace `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` with your actual Hugging Face API key. This code will set up a simple web application that intersacts with the Llama model and provides AI-generated responses.

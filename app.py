from flask import Flask, request, jsonify,render_template
import google.generativeai as genai
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Fix CORS issue to allow frontend requests

# Configure Gemini API Key
genai.configure(api_key=os.environ.get('GEM_API'))

def gemini_ai(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure model name is correct
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "No response from AI."
    except Exception as e:
        return f"Error: {e}"
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_ai():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "Error: No input received!"})

    ai_response = gemini_ai(prompt)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)

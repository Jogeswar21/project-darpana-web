import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import json

# --- CONFIGURATION & SETUP ---
# template_folder ensures Flask finds your HTML files (index.html, etc.)
app = Flask(__name__, template_folder='templates')

# Environment Variable Check
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY not found. AI features will be disabled.")
    # Initialize a dummy model if key is missing, to prevent crashing
    model = None 
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Use Gemini 1.5 Flash for speed across all vision and text tasks
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- CORE ROUTE: Serves the HTML pages ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 1. DRISTI: VISION AI ENDPOINT ---
# Handles image upload, equation recognition, and analysis.
@app.route('/api/dristi_analyze', methods=['POST'])
def dristi_analyze():
    if not model:
        return jsonify({"error": "AI Service Unavailable. Missing GOOGLE_API_KEY."}), 503

    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "No image file provided."}), 400

        # 1. Image Preprocessing
        img_bytes = image_file.read()
        image = Image.open(io.BytesIO(img_bytes))

        # 2. AI Prompting (The Competitive Edge)
        system_prompt = """
        You are 'DRISTI', an elite AI Vision Engine for Project Darpana.
        Your task is to analyze the provided image of a handwritten or printed equation.
        
        Analyze the image and respond STRICTLY in the following JSON format.
        Do NOT include any extra text or markdown outside the JSON object.
        
        {
          "recognized_equation": "[The full equation in LaTeX format]",
          "confidence": [A number between 0.7 and 1.0],
          "analysis_steps": [
            "Step 1: Detected symbols and structure.",
            "Step 2: Identified type (e.g., Integral Calculus).",
            "Step 3: Verified syntax and formatting.",
            "Step 4: Provided relevant formula context."
          ]
        }
        """
        
        response = model.generate_content([system_prompt, image], 
                                          config=genai.types.GenerateContentConfig(response_mime_type="application/json"))
        
        # 3. Parse and Return
        # The AI is instructed to return JSON, so we safely parse it.
        result = json.loads(response.text)
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"DRISTI Analysis Error: {e}")
        return jsonify({"error": f"Internal server error during processing: {str(e)}"}), 500

# --- 2. SIDDHANTA: LOGIC AI ENDPOINT ---
# Handles logical proof verification and suggestions.
@app.route('/api/siddhanta_verify', methods=['POST'])
def siddhanta_verify():
    if not model:
        return jsonify({"valid_status": False, "feedback": "AI Service Unavailable. Missing GOOGLE_API_KEY."})
    
    data = request.get_json()
    steps = data.get('steps', [])
    theorem = data.get('theorem', '')
    
    # Simple check for empty proof
    if not steps:
        return jsonify({"valid_status": False, "feedback": "Proof steps are empty."})

    full_proof_text = f"Theorem: {theorem}\nProof Steps:\n" + "\n".join([f"Step {i+1}: {step['content']}" for i, step in enumerate(steps)])

    system_prompt = f"""
    You are 'SIDDHANTA', an AI Logic Verifier. Your job is to meticulously check the logical flow of the given proof steps against the stated theorem.
    
    Respond STRICTLY in the following JSON format. Identify the first logical error, if any, and suggest a correction.
    
    {{
      "valid_status": [true/false],
      "feedback": "[Detailed analysis or successful confirmation]",
      "suggestions": [
        "Suggestion 1: What to change in the proof.",
        "Suggestion 2: Alternative approach."
      ]
    }}
    """
    
    try:
        response = model.generate_content(system_prompt + "\n\n" + full_proof_text,
                                          config=genai.types.GenerateContentConfig(response_mime_type="application/json"))
        return jsonify(json.loads(response.text))
    except Exception as e:
        return jsonify({"valid_status": False, "feedback": f"AI Logic Error: {str(e)}", "suggestions": []})

# --- 3. SAMVAD: MULTILINGUAL AI ENDPOINT ---
# Handles scientific term lookup and cultural context.
@app.route('/api/samvad_lookup', methods=['POST'])
def samvad_lookup():
    if not model:
        return jsonify({"error": "AI Service Unavailable. Missing GOOGLE_API_KEY."})
        
    data = request.get_json()
    term = data.get('term', '')
    language = data.get('language', 'english')

    system_prompt = f"""
    You are 'SAMVAD', a Multilingual Scientific Communication AI.
    Look up the term '{term}' and provide its phonetic guide, definition, and cultural context tailored for students.
    The response should be primarily in {language} where possible.
    
    Respond STRICTLY in the following JSON format.
    
    {{
      "term": "{term}",
      "language": "{language}",
      "phonetic": "[Pronunciation guide, e.g., /ˌfoʊtoʊˈsɪnθəsɪs/]",
      "definition": "[Concise definition in the requested language]",
      "cultural_context": "[Brief explanation of the term's origin or relevance to Indian science/etymology]"
    }}
    """
    
    try:
        response = model.generate_content(system_prompt,
                                          config=genai.types.GenerateContentConfig(response_mime_type="application/json"))
        return jsonify(json.loads(response.text))
    except Exception as e:
        return jsonify({"error": f"AI Lookup Error: {str(e)}"}), 500


if __name__ == '__main__':
    # Required for deployment on Hugging Face Spaces
    app.run(host='0.0.0.0', port=7860)

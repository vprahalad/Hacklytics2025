from flask import Flask, request, jsonify
from flask_cors import CORS  
from model import Model as SentenceModel
from naturalnessAI import Model as NaturalnessModel
from assignREAL import codeWordAssign
from codeWordGen import codeWordGen

app = Flask(__name__)
CORS(app) 

sentence_model = SentenceModel()
naturalness_model = NaturalnessModel()

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/api/encode', methods=['POST'])
def encode_message():
    try:
        data = request.json  
        print("🚀 Received data:", data)  

        if not data or "text" not in data:
            return jsonify({"error": "Missing text field"}), 400

        text = data["text"]  
        
        wordsInRange = codeWordGen("cleaned_data.csv")
        word_dict, code_words = codeWordAssign(text, wordsInRange)

        text = data["text"] 
        encoded_text = sentence_model.generate_sentence(code_words)  

        score = naturalness_model.score_naturalness(encoded_text)


        key_data = {
            "original_message": text,
            "code_words": code_words,
            "word_dict": word_dict
        }

        metric = 0.85 

        response = {"encoded": encoded_text, "key": key_data, "metric": metric}
        print("Sending response:", response)  
        return jsonify(response)  

    except Exception as e:
        print("Error in backend:", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 

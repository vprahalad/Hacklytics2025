# from flask import Flask, request, jsonify
# from flask_cors import CORS  
# from model import Model as SentenceModel  
# from naturalnessAI import Model as NaturalnessModel 
# from assignREAL import codeWordAssign
# from codeWordGen import codeWordGen

# app = Flask(__name__)
# CORS(app)  # Allow frontend to access backend

# sentence_model = SentenceModel()  
# naturalness_model = NaturalnessModel()

# @app.route('/')
# def home():
#     return "Flask API is running!"

# @app.route('/api/encode', methods=['POST'])
# def encode_message():
#     try:
#         data = request.json  
#         print("🚀 Received request data:", data)  # Debugging

#         if not data or "text" not in data:
#             print("⚠️ Missing 'text' in request!")
#             return jsonify({"error": "Invalid request"}), 400

#         text = data["text"]  # User input
#         encoded_text = "This is a sample encoded message"  
#         key = {"example_key": "value"}  
#         metric = 0.85  

#         response = {"encoded": encoded_text, "key": key, "metric": metric}
#         print("✅ Sending response:", response)  # Debugging

#         return jsonify(response)

#     except Exception as e:
#         print("🔥 Error in backend:", e)
#         return jsonify({"error": "Internal server error"}), 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows cross-origin requests
from model import Model as SentenceModel
from naturalnessAI import Model as NaturalnessModel
from assignREAL import codeWordAssign
from codeWordGen import codeWordGen

app = Flask(__name__)
CORS(app)  # Enable CORS to handle requests from the frontend

# Initialize models
sentence_model = SentenceModel()
naturalness_model = NaturalnessModel()

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/api/encode', methods=['POST'])
def encode_message():
    try:
        data = request.json  # Get the JSON data sent from frontend
        print("🚀 Received data:", data)  # Debugging

        if not data or "text" not in data:
            return jsonify({"error": "Missing text field"}), 400

        text = data["text"]  # User input from frontend
        
        # Generate code words (assume this logic is fine)
        wordsInRange = codeWordGen("cleaned_data.csv")
        word_dict, code_words = codeWordAssign(text, wordsInRange)

        text = data["text"]  # User input from frontend
        encoded_text = sentence_model.generate_sentence(code_words)  # Using model to generate sentence

        # Score the naturalness of the generated sentence
        score = naturalness_model.score_naturalness(encoded_text)

        # Create a response key (can be modified based on real key logic)
        key_data = {
            "original_message": text,
            "code_words": code_words,
            "word_dict": word_dict
        }

        metric = 0.85  # Replace with real metric score

        response = {"encoded": encoded_text, "key": key_data, "metric": metric}
        print("✅ Sending response:", response)  # Debugging

        return jsonify(response)  # Send back response as JSON

    except Exception as e:
        print("🔥 Error in backend:", e)
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run Flask on port 5000

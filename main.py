from flask import Flask, request, jsonify
from model import Model as SentenceModel  
from naturalnessAI import Model as NaturalnessModel 
from assignREAL import codeWordAssign
from codeWordGen import codeWordGen
import csv

app = Flask(__name__)

# Load models once to avoid reloading them on each request
sentence_model = SentenceModel()  
naturalness_model = NaturalnessModel()

@app.route("/api/send", methods=["POST"])
def process_message():
    try:
        data = request.get_json()
        secret_message = data.get("message", "")

        if not secret_message:
            return jsonify({"error": "No message provided"}), 400

        # Generate code words
        wordsInRange = codeWordGen("cleaned_data.csv")
        word_dict, code_words = codeWordAssign(secret_message, wordsInRange)

        # Generate sentence
        sentence = sentence_model.generate_sentence(code_words)

        # Score the naturalness of the generated sentence
        score = naturalness_model.score_naturalness(sentence)

        # Create a response key (can be modified based on real key logic)
        key_data = {
            "original_message": secret_message,
            "code_words": code_words,
            "word_dict": word_dict
        }

        return jsonify({
            "response": sentence,
            "metric": score,
            "key": key_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

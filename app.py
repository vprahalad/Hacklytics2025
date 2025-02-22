from flask import Flask, request, jsonify
from flask_cors import CORS  # f-b communication
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/api/encode', methods=['POST'])
def encode_message():
    data = request.json  
    text = data.get("text", "")  # input message
    encoded_text = "This is a sample encoded message" # but put actual backend encoded message here
    key = {"example_key": "value"}  # but put actual backend key here
    metric = 0.85 # but put actual backend metric here

    return jsonify({"encoded": encoded_text, "key": key, "metric": metric})

if __name__ == '__main__':
    app.run(debug=True)

import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from llamaapi import LlamaAPI

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

llama = LlamaAPI("YOUR_API_KEY_HERE")

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        api_request_json = {
            "messages": [
                {"role": "user", "content": prompt},
            ]
        }
           # Execute the Request
        response = llama.run(api_request_json)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}),   500

if __name__ == '__main__':
    app.run(debug=True)
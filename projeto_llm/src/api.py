# api.py

from flask import Flask, request, jsonify
from flask_cors import CORS  # New import for CORS
from langchain import LLMChain

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Loading the trained model
llm_chain = LLMChain.load('../models/llm_model')

@app.route('/query', methods=['POST'])
def query_llm():
    query = request.json.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    try:
        response = llm_chain.run(query)
        if not response:
            raise ValueError("No response from the model")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000)

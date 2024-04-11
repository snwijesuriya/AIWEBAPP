# api.py
from flask import Flask, jsonify, request
from summarization_logic import generate_summary

webapp = Flask(__name__)

@webapp.route('/process_text', methods=['POST'])
def process_text():
    # Parse incoming JSON data
    data = request.get_json()
    text = data['text']
    
    # Generate summary using the summarization logic module
    summary = generate_summary(text)
    
    # Return processed text as JSON response
    return jsonify({'processed_text': summary})

if __name__ == '__main__':
    webapp.run(debug=True)

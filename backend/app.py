from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BartTokenizer, BartForConditionalGeneration
import os
import logging

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
CORS(app)

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_length=150, min_length=25):
    inputs = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        app.logger.error('No file part in the request')
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        app.logger.error('No selected file')
        return "No selected file", 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        summary = summarize_text(content)
        app.logger.info(f'File {file.filename} uploaded and summarized successfully')
        return jsonify({"content": content, "summary": summary})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    if 'text' not in data:
        app.logger.error('No text provided for summarization')
        return "No text provided", 400
    summary = summarize_text(data['text'])
    app.logger.info('Text summarized successfully')
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

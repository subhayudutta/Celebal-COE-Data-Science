import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_id = os.getenv('AZURE_DEPLOYMENT_ID')
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='content-generator-for-social-media'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        response = openai.Completion.create(
            engine=deployment_name,  
            prompt=prompt,
            max_tokens=150,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        result_text = response.choices[0].text.strip()
        return jsonify({'generated_text': result_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

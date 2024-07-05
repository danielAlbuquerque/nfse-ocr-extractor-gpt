import os
import json
import base64
import requests
from flask import Flask, request, jsonify
from urllib.parse import urlparse
from dotenv import load_dotenv
from openai import OpenAI
from pdf2image import convert_from_path

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)

def upload_to_temp_storage(file_path: str) -> str:
    url = "https://file.io"  # File.io is a service that allows temporary file sharing
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={"file": file})
    if response.status_code == 200:
        return response.json().get('link')
    else:
        raise Exception("Failed to upload file")

def load_json_schema(schema_file: str) -> dict:
    with open(schema_file, 'r') as file:
        return json.load(file)

@app.route('/extract-data', methods=['POST'])
def process_pdf():
    print('Iniciando processamento')
    file = request.files['pdf']
    if file:
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)

        nfse_schema = load_json_schema('nfse_schema.json')

        if file.filename.lower().endswith('.pdf'):
            print('Convertendo PDF para imagem')
            images = convert_from_path(file_path)
            image_path = '/tmp/temp_image.png'
            images[0].save(image_path, 'PNG')
            file_to_upload = image_path
        else:
            file_to_upload = file_path

        print('Gerando url')
        file_url = upload_to_temp_storage(file_to_upload)
        print(file_url)
        print('Enviando para o chatgpt')

        pass
        
        response = client.chat.completions.create(
            model='gpt-4o',
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "provide JSON file that represents this document, if the json does has all the info just return the ones that you got, it's import the json is valid. Use this JSON Schema: " +
                            json.dumps(nfse_schema)},
                        {
                            "type": "image_url",
                            "image_url": {"url": file_url}
                        }
                    ],
                }
            ],
            max_tokens=1000,
        )
        
        response_content = response.choices[0].message.content
        print('Resposta GPT:')
        print(response_content)

        # Ensure the response is a complete and valid JSON
        try:
            json_data = json.loads(response_content)
        except json.JSONDecodeError:
            # Handle incomplete JSON
            return jsonify({'error': 'Incomplete JSON received from the model'}), 500
        print('Enviando resposta pro client')
        return jsonify(json_data)

    return jsonify({'error': 'No file uploaded'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

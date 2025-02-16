from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Nastavení složky pro ukládání souborů
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads', methods=['POST'])
def upload_file():
    # Zkontroluj, jestli soubor byl přidán v požadavku
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # Zkontroluj, zda byl vybrán soubor
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Pokud je soubor, ulož ho a vypiš název
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Zde by se mohla provést transkripce souboru Whisperem (není implementováno)

        return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200

if __name__ == '__main__':
    app.run(debug=True)

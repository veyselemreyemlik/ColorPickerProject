from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Renk veri setini yükle
with open('colors.json', 'r') as f:
    color_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_color', methods=['POST'])
def save_color():
    color = request.json.get('color')
    # Kaydetme işlemi (bir veritabanına veya dosyaya yazabilirsiniz)
    # Şimdilik sadece geri döndürüyoruz.
    return jsonify({"status": "success", "color": color})

if __name__ == '__main__':
    app.run(debug=True)


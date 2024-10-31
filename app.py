from flask import Flask, render_template
from api import api_bp

app = Flask(__name__)

# API Blueprint kaydet
app.register_blueprint(api_bp)

# Ana sayfa rotası
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

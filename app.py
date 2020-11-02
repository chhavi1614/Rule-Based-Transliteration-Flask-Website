from flask import Flask, render_template, request, redirect, jsonify
from models import rule_based_transliterator_service as transliterator

app = Flask(__name__)


@app.route('/')
@app.route('/start')
def home():
    return render_template('index.html')


@app.route('/transliterate', methods=['POST', 'GET'])
def index():
    input_text = request.form['content']
    word = request.args.get('content')
    trans = transliterator.getTransliteration(input_text)
    result = {
        "output": trans
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)

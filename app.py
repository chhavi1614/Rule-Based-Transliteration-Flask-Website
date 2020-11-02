from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/start')
def home():
    return render_template('index.html')



@app.route('/transliterate', methods=['POST', 'GET'])
def index():
        input_text = request.form['content']
        word = request.args.get('content')
        trans = input_text.lower()
        result = {
            "output" : trans
        }
        result = {str(key): value for key, value in result.items()}
        return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)

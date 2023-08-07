from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request.form['word']
    return render_template('index.html')

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

@app.route('/score')
def score():
    return render_template('score.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def one():
    return render_template('index.html', )

@app.route('/play/<int:num>')
def two(num):
    return render_template('index.html', times = num)

@app.route('/play/<int:num>/<color>')
def three(num , color):
    return render_template('index.html', times = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)
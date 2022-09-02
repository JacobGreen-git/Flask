from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/play/<num>')
def wordRepeat(num, word):
    return word * int(num)

if __name__=="__main__": 
    app.run(debug=True)
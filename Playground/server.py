from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/play')
def play():
    return render_template('index.html')  


# @app.route('/play/<num>')
# def wordRepeat(num, word):
#     return word * int(num)


if __name__=="__main__":  
    app.run(debug=True) 
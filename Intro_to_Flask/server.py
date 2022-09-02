from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')      
def index():
    return render_template('index.html')  

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<num>/<word>')
def wordRepeat(num, word):
    return word * int(num)


if __name__=="__main__": 
    app.run(debug=True) 

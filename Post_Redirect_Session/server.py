from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github" #this is required to use session


@app.route('/')
def render_form():
    return render_template('index.html')

@app.route('/process_form', methods =["POST"])
def process_form():
    print(request.form)
    session['dog_name'] = request.form['dog_name']
    session['dog_breed'] = request.form['dog_breed']
    # return render_template('display.html', name = dog_name,breed = dog_breed)
    return redirect("/show_info")

@app.route('/show_info')
def show_info():
    name = session['dog_name']
    breed = session['dog_breed']
    return render_template("display.html", name = name, breed = breed)

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')



if __name__=="__main__":  
    app.run(debug=True) 
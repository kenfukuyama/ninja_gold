from flask import Flask, render_template, redirect, request, session
import random


app = Flask(__name__)  
app.secret_key = "hello"  

# session['visitedTimes'] = 0 # cant do here

# answer_key = random.randint(1, 100)


@app.route('/')          
def index():
    if 'visitedTimes' in session:
        session['visitedTimes'] += 1
    else: 
        session['visitedTimes'] = 0
        session["answer_key"] = random.randint(1, 100)

    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojoLocation'] = request.form['dojoLocation']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form['comment']
    

    # print(session)
    return redirect('/result')


@app.route('/result')
def show_result():
    return render_template('result.html')

if __name__=="__main__":   
    app.run(debug=True)   






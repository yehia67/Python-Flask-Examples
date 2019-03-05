from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Check : </h1> <ol><li>result</li> <li>grade/YOUR GRADE </li></ol>"

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/grade/<int:score>')
def hello_name(score):
   return render_template('grade.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)

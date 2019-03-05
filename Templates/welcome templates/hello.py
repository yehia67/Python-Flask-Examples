from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
   return "Hey Find your page by query = hello/YOURNAME"

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)

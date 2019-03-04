from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
homepage = "<h1> Hello %s </h1> <p> welcome welcome</p>"

@app.route('/success/<name>')
def success(name):
   return homepage % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
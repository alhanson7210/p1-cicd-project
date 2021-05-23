from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def hello():
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        return redirect('/followers')

def followers():
    if request.method == "GET":
        return render_template('data.html')

app.add_url_rule('/', '/', hello, methods=['GET', 'POST'])
app.add_url_rule('/followers', 'followers', followers, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

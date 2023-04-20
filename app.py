from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """Hello world <br>
<br> <a href="/1" style="color:rgb(255,0,0)">Goodbye world</a>"""
@app.route('/1')
def goodbye_world():
    return """Goodbye World <br>
    <br> <a href="/" style="color:rgb(0,255,0)">Hello world</a>"""
@app.route("/stuypy")
def stuypy():
    return render_template('index.html')

app.run()

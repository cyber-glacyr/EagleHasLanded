from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html', viability=is_viable())

def is_viable():
    return 'not viable'

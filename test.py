from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return "Test app for chrome issue"


@app.route("/same", methods=['GET', 'POST'])
def same():
    return render_template('same.html')


@app.route("/iframe_source")
def iframe_source():
    return render_template('iframe_source.html')


@app.route("/iframe_form")
def iframe_form():
    return render_template('iframe_form.html')


@app.route("/cross")
def cross():
    return render_template('cross.html')


@app.route("/cross_source")
def cross_source():
    return render_template('cross_source.html')

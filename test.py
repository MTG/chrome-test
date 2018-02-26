from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return "Test app for chrome issue"


@app.route("/test", methods=['GET', 'POST'])
def same():
    return render_template('microphone_test.html')


# Using iframe's source

@app.route("/iframe_src")
def iframe_src_same():
    return render_template('iframe_source.html')


@app.route("/iframe_src_diff")
def iframe_src_diff():
    return render_template('iframe_source_diff.html')


@app.route("/iframe_src_diff_allow")
def iframe_src_diff_allow():
    return render_template('iframe_source_diff_allow.html')


@app.route("/iframe_src_diff_header")
def iframe_src_diff_header():
    return render_template('iframe_source_diff_header.html')

# Using a form to fill the iframe


@app.route("/get_from_same")
def get_from_same():
    return render_template('get_from_same.html')


@app.route("/post_from_same")
def post_from_same():
    return render_template('post_from_same.html')


@app.route("/get_from_diff")
def get_from_diff():
    return render_template('get_from_diff.html')


@app.route("/post_from_diff")
def post_from_diff():
    return render_template('post_from_diff.html')

import flask
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
    return render_template('iframe_src_diff.html')


@app.route("/iframe_src_diff_allow")
def iframe_src_diff_allow():
    return render_template('iframe_src_diff_allow.html')


@app.route("/iframe_src_diff_header")
def iframe_src_diff_header():
    resp = flask.Response(render_template('iframe_src_diff.html'))
    resp.headers["Feature-Policy"] = "microphone 'self' http://localhost:5001"
    return resp

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


# iframe same domain loading js from different domain
@app.route("/iframe_src_js")
def iframe_src_js():
    return render_template('iframe_src_js.html')


# iframe loading from js xhr same domain
@app.route("/js_xhr_same")
def js_xhr_same():
    return render_template('js_xhr_same.html')


@app.route("/js_xhr_diff")
def js_xhr_diff():
    resp = flask.Response(render_template('js_xhr_diff.html'))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

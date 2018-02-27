import flask
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home_page.html')


@app.route("/test", methods=['GET', 'POST'])
def same():
    resp = flask.Response(render_template('microphone_test.html'))
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


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
    resp.headers["Feature-Policy"] = "microphone 'self' https://test2:8443"
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


@app.route("/get_from_diff_policy")
def get_from_diff_policy():
    resp = flask.Response(render_template('get_from_diff.html'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://test2:8443"
    return resp


@app.route("/post_from_diff_policy")
def post_from_diff_policy():
    resp = flask.Response(render_template('post_from_diff.html'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://test2:8443"
    return resp


@app.route("/post_from_diff_policy_allow")
def post_from_diff_policy_allow():
    """
    This view sets up the Feature Policy but then in the template the allow=microphone is set, probably
    overriding the permissions and not allowing the access to the microphone.
    :return:
    """
    resp = flask.Response(render_template('post_from_diff_allow.html'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://test2:8443"
    return resp


# iframe same domain loading js from different domain
@app.route("/iframe_src_js")
def iframe_src_js():
    return render_template('iframe_src_js.html')


@app.route("/microphone_load", methods=['GET', 'POST'])
def microphone_load():
    return render_template('microphone_load.html')


@app.route("/microphone.js")
def microphone_js():
    return render_template('microphone.js')



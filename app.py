from flask import Flask, render_template, Response

app = Flask(__name__)


MY_HOST = "host1"
OTHER_HOST = "host2"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/microphone_embed", methods=['GET', 'POST'])
def microphone_embed():
    return render_template('microphone_embed.html')


@app.route("/microphone_embed_js", methods=['GET', 'POST'])
def microphone_external():
    return render_template('microphone_with_external.html')


@app.route("/microphone.js")
def microphone_js():
    return render_template('microphone.js')


# Using iframe with src element

@app.route("/iframe_src")
def iframe_src_same():
    """ An iframe loading a page from the same host should succeed """
    return render_template('iframe.html', iframe_host=MY_HOST)


@app.route("/iframe_src_diff")
def iframe_src_diff():
    """ An iframe loading a page from a different host should fail """
    return render_template('iframe.html', iframe_host=OTHER_HOST)


@app.route("/iframe_src_diff_allow")
def iframe_src_diff_allow():
    """ An iframe loading a page from a different host with an allow attribute should succeed """
    return render_template('iframe_allow.html', iframe_host=OTHER_HOST)


@app.route("/iframe_src_diff_header")
def iframe_src_diff_header():
    """ An iframe loading a page from a different host with feature-policy header should succeed """
    resp = Response(render_template('iframe.html', iframe_host=OTHER_HOST))
    resp.headers["Feature-Policy"] = "microphone 'self' https://{}:8443".format(OTHER_HOST)
    return resp


# Using a form to fill the iframe

@app.route("/form_get_samehost")
def form_get_samehost():
    """ Using a form's target attribute to fill an iframe (same host, succeeds) """
    return render_template('form.html', iframe_host=MY_HOST, form_method='GET')


@app.route("/form_get_diffhost")
def form_get_diffhost():
    """ Using a form's target attribute to fill an iframe (different host, fails) """
    return render_template('form.html', iframe_host=OTHER_HOST, form_method='GET')


@app.route("/form_get_diff_policy")
def form_get_from_diff_policy():
    """ Using a form's target attribute to fill an iframe (different host with policy header, succeeds) """
    resp = Response(render_template('form.html', iframe_host=OTHER_HOST, form_method='GET'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://{}:8443".format(OTHER_HOST)
    return resp


@app.route("/post_from_diff_policy")
def form_post_from_diff_policy():
    """ Using a form's target attribute to fill an iframe with a post
        (different host with policy header, succeeds) """
    resp = Response(render_template('form.html', iframe_host=OTHER_HOST, form_method='POST'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://{}:8443".format(OTHER_HOST)
    return resp


@app.route("/post_from_diff_policy_allow")
def post_from_diff_policy_and_allow():
    """
    Using a form's target attribute to fill an iframe with a post
    Include a feature-policy header *and* allow=microphone attribute, fails
    """
    resp = Response(render_template('form_allow.html', iframe_host=OTHER_HOST, form_method='POST'))
    resp.headers["Feature-Policy"] = "microphone 'self' https://{}:8443".format(OTHER_HOST)
    return resp

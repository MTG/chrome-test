# Chrome iframe cross-domain media access permissions

Recent versions of chrome (&gt; 64) block media access from iframes loaded from a
cross domain unless permission is explicitly given:
https://sites.google.com/a/chromium.org/dev/Home/chromium-security/deprecating-permissions-in-cross-origin-iframes

This demo app shows various situations where this might succeed or fail, and how to fix it.

## Installation
Install [flask](http://flask.pocoo.org/) and [stunnel](https://www.stunnel.org/)

## Run
### 1. Create domains

We need two domains. The easiest way to do this is to edit `/etc/hosts` to point some domains
to somewhere on `localhost`. We defined two hosts in the application called `host1` and `host2`.
If you want to use different hosts, change these at the top of `app.py`

Create two domains on your machine called `host1` and `host2` by editing the `/etc/hosts` file:

    127.0.0.1       host1
    127.0.0.2       host2

### 2. Run stunnel

Chrome allows unrestricted access to the microphone if the host is `localhost`, but otherwise requires
you to access pages over https. We've provided an `stunnel` configuration with a self-signed certificate
which redirects port 8443 to port 5000 (Flask's default port)

Run it:

    stunnel stunnel/dev_https

### 3. Run flask
Just run

    FLASK_APP=app.py FLASK_DEBUG=1 flask run

### 4. Access https://host1:8443


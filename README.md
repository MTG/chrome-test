# chrome-test

## Installation
Install [flask](http://flask.pocoo.org/) and [stunnel](https://www.stunnel.org/)

## Run
### 1. Create domains
Create two domains on your machine called _test1_ and _test2_ by editing the /etc/hosts files:

    127.0.0.1       test1
    127.0.0.2       test2
    
### 2. Run stunnel
To be able to run the servers on https run:

    stunnel stunnel/dev_https
    
### 3. Run flask
Just run

    FLASK_APP=app.py FLASK_DEBUG=1 flask run
    
### 4. Access https://test1:8443
    

from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from twilio import twiml
import subprocess
import os

from cmd import cmds

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

ACCOUNT_SID = "AC4ac24bd3f16cbede13c47ab7a0bdc838" #os.environ['ACCOUNT_SID']
AUTH_TOKEN = "391505146d1652e0b076ec11033f5a92" #os.environ['AUTH_TOKEN']
APP_SID = "Twilix" #os.environ['APP_SID']
CALLER_ID = "+14389855700" #os.environ['CALLER_ID']
#CALLER_ID = "+18175985398" #os.environ['CALLER_ID']

@app.route("/")
def index():
    return "Hello, world, motherfucker!!!"

@app.route('/sms', methods=['POST'])
def sms():
    response = twiml.Response()
    user_input = request.form['Body']
    if '|' in user_input:
	pass
    else:
	args = user_input.lower().spit() 
        output = args[0](args[1:])
    response.sms(output)
    return str(response)

if __name__ == "__main__":
    #app.run(debug=True)
    app.debug = True
    app.run(host='0.0.0.0')
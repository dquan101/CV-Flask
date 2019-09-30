import yaml
from flask import Flask, jsonify, render_template, request
import os, optparse, sys
app = Flask(__name__)
developer = os.getenv("DEVELOPER", "Diego Quan")
environment = os.getenv("ENVIRONMENT", "development")


with open('info.yml') as f:
    Data = yaml.load(f, Loader=yaml.FullLoader)



@app.route("/")
def home():
    return render_template("home.html", developer=developer, data=Data)

@app.route("/academica")
def academica():
    return render_template("academica.html", developer=developer, data=Data)

@app.route("/laboral")
def laboral():
    return render_template("laboral.html", developer=developer, data=Data)

if __name__=="__main__":
    debug=True
    if environment == 'development' or environment == 'local':
        debug=True
    print('Local change')
    app.run(host="0.0.0.0", debug=debug)
from flask import Flask
from flask import render_template
# from shamovie_main import *

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
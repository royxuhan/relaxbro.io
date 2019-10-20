from flask import Flask, render_template, request
import json

from relax import main
import relax
# from shamovie_main import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/toggle', methods=['GET','POST'])
def listen():
    data = json.loads(request.data.decode('utf-8'))
    print('data is: ',data)
    if data['status'] == "Listen":
        print('listening')
        relax.cont = True
        main(data['number'])
    else:
        print('exiting')
        relax.cont = False
    return render_template('index.html')

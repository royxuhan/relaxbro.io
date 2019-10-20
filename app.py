from flask import Flask, render_template, request

from relax import main
import relax
# from shamovie_main import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/toggle', methods=['GET','POST'])
def listen():
    status = request.data.decode('utf-8')
    print(status)
    if status == "Listen":
        print('listening')
        relax.cont = True
        main()
    else:
        print('exiting')
        relax.cont = False
    return render_template('index.html')
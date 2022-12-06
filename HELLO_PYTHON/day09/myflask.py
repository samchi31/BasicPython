# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day09.dao_sample import DaoSample

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/param')
def param():
    # parameter_dict = request.args.to_dict()
    # if len(parameter_dict) == 0:
    #     return 'No parameter'
    #
    # parameters = ''
    # for key in parameter_dict.keys():
    #     parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    # return 'param : ' + parameters
    
    a= request.args.get('a','babo')
    return 'param : ' + a   

@app.route('/post', methods=["post"])
def post():
    # a = request.form.get('a')
    a = request.form['a']
    return 'post : ' + a

@app.route('/sample')
def sample():
    ds = DaoSample()
    dicts = ds.selects()
    return str(dicts)

@app.route('/view')
def view():
    a='홍길동'
    b=['바보','천재','미남']
    c=[
        {'col01':'1','col02':'1'},
        {'col01':'1','col02':'1'}
      ]
    return render_template('view.html', aa=a,bb=b,cc=c)

if __name__ == '__main__':
    app.run(debug=True)
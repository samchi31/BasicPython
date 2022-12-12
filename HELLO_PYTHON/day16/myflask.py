# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day14.dao_teacher import DaoTeacher



app = Flask(__name__)

@app.route('/')
@app.route('/three')
def hello():
    return render_template('three.html')




if __name__ == '__main__':
    app.run(debug=True)
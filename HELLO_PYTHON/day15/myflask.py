# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day14.dao_teacher import DaoTeacher



app = Flask(__name__)

@app.route('/')
@app.route('/thread')
def hello():
    return render_template('thread.html')

@app.route('/ajax_thread1', methods=['POST'])
def ajax_thread1():
    data = request.get_json()
    return jsonify(result = data)

@app.route('/ajax_thread2', methods=['POST'])
def ajax_thread2():
    data = request.get_json()
    return jsonify(result = data)



if __name__ == '__main__':
    app.run(debug=True)
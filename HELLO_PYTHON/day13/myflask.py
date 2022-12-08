# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day13.dao_student import DaoStudent


app = Flask(__name__)
dao = DaoStudent();

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax_list', methods=['POST'])
def ajax_list():
    result = dao.selects()
    # print(result)
    return jsonify(result = result)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    data = request.get_json()
    # print(data['id'])
    result = dao.select(data['id'])
    return jsonify(result= result)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    data = request.get_json()
    # print(data)
    result = dao.insert(data['id'], data['name'], data['mobile'], data['addr'])
    return jsonify(result = result)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    data = request.get_json()
    # print(data)
    result = dao.update(data['id'], data['name'], data['mobile'], data['addr'])
    return jsonify(result = result)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    data = request.get_json()
    # print(data)
    result = dao.delete(data['id'])
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(debug=True)
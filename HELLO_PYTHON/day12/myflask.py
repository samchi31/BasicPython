# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day10.dao_emp import DaoSample


app = Flask(__name__)
dao = DaoSample();

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    # data = request.get_json()
    # print(data['id'])
    # result = dao.select(data['id'])
    result = dao.selects()
    return jsonify(result = "success", result2= result)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    data = request.get_json()
    # print(data['id'])
    result = dao.select(data['id'])
    return jsonify(result = "success", result2= result)

@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    data = request.get_json()
    # print(data)
    result = dao.insert(data['id'], data['name'], data['sex'], data['addr'])
    return jsonify(result = "success", result2= result)

@app.route('/ajax_edit', methods=['POST'])
def ajax_edit():
    data = request.get_json()
    # print(data)
    result = dao.update(data['id'], data['name'], data['sex'], data['addr'])
    return jsonify(result = "success", result2= result)

@app.route('/ajax_delete', methods=['POST'])
def ajax_delete():
    data = request.get_json()
    # print(data)
    result = dao.delete(data['id'])
    return jsonify(result = "success", result2= result)

if __name__ == '__main__':
    app.run(debug=True)
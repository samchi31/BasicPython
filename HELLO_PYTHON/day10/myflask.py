# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day10.dao_emp import DaoSample


app = Flask(__name__)
dao = DaoSample();

@app.route('/')
@app.route('/emp_list')
def emp_list():
    list = dao.selects()
    return render_template('emp_list.html', list=list)

@app.route('/emp_detail')
def emp_detail():
    e_id = request.args.get('e_id')
    info = dao.select(e_id)
    return render_template('emp_detail.html', info=info)

@app.route('/emp_edit')
def emp_edit():
    e_id = request.args.get('e_id')
    info = dao.select(e_id)
    return render_template('emp_edit.html', info=info)

@app.route('/emp_update', methods=["post"])
def emp_update():
    e_id = request.form.get('e_id');
    e_name = request.form.get('e_name');
    sex = request.form.get('sex');
    addr = request.form.get('addr');
    res = dao.update(e_id, e_name, sex, addr)
    
    return render_template('emp_update.html',cnt=res)

@app.route('/emp_insert')
def emp_insert():
     return render_template('emp_add.html')
    
@app.route('/emp_add', methods=["post"])
def emp_add():
    e_id = request.form.get('e_id');
    e_name = request.form.get('e_name');
    sex = request.form.get('sex');
    addr = request.form.get('addr');
    res = dao.insert(e_id, e_name, sex, addr)
    
    return render_template('emp_update.html',cnt=res)


@app.route('/emp_delete')
def emp_delete():
    e_id = request.args.get('e_id')
    res = dao.delete(e_id)
    return render_template('emp_update.html', cnt=res)

if __name__ == '__main__':
    app.run(debug=True)
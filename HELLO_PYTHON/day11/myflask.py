# from flask import Flask , request, redirect
from flask import *
import psycopg2;
from day11.dao_mem import DaoMember


app = Flask(__name__)
dao = DaoMember();

@app.route('/')
@app.route('/mem_list')
def mem_list():
    list = dao.selects()
    return render_template('memList.html', list=list)

@app.route('/mem_detail')
def mem_detail():
    m_id = request.args.get('m_id')
    info = dao.select(m_id)
    return render_template('memDetail.html', info=info)

@app.route('/mem_edit')
def mem_edit():
    m_id = request.args.get('m_id')
    info = dao.select(m_id)
    return render_template('memUpdate.html', info=info)

@app.route('/mem_edit_act', methods=["post"])
def mem_edit_act():
    m_id = request.form.get('m_id');
    m_nm = request.form.get('m_nm');
    tel = request.form.get('tel');
    ymd = request.form.get('ymd');
    res = dao.update(m_id, m_nm, tel, ymd)
    
    return render_template('memComplete.html',cnt=res)

@app.route('/mem_add')
def mem_add():
     return render_template('memAdd.html')
    
@app.route('/mem_add_act', methods=["post"])
def mem_add_act():
    m_id = request.form.get('m_id');
    m_nm = request.form.get('m_nm');
    tel = request.form.get('tel');
    ymd = request.form.get('ymd');
    res = dao.insert(m_id, m_nm, tel, ymd)
    
    return render_template('memComplete.html',cnt=res)


@app.route('/mem_delete')
def mem_delete():
    m_id = request.args.get('m_id')
    res = dao.delete(m_id)
    return render_template('memComplete.html', cnt=res)

if __name__ == '__main__':
    app.run(debug=True)
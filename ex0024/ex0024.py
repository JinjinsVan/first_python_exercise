import sqlite3,os,time
from flask import Flask,request,session,g,redirect,url_for,\
abort,render_template,flash
from contextlib import closing
from datetime import datetime

import utils


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT,'tmp','todo.db')
DEBUG = True
SECRET_KEY = "EX0024_SECRET_KEY"

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read().decode())
	db.close


@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/register',methods=['POST'])
def register():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		cursor = g.db.execute('select count(*) from user where username = ?',[username])
		if cursor.rowcount() != 0:
			error = 'This name has been used,  please change another one :)'
			return render_template('register.html',error=error)
		else:
			g.db.execute('insert into user (username,password) values (?,?)',[username,utils.encrypt_password(request.form['password'],None)])
	        g.db.commit()
	        return redirect(url_for('show_list'))

@app.route('/login',methods=['POST'])
def login():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		cursor = g.db.execute('select * from user where username = ?',[username])
		if cursor.hasNext():
			pass:
			pass


@app.route('/add',methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	else:
		g.db.execute('insert into todolist (title,date,status,user_id) values (?,?,?,?)',[request['title'],str(datetime.now()),'0',session.get('user_id')])
		g.db.commit()
		flash('Succesfully posted')
		return redirect(url_for('show_list'))




	




# init_db()
import sqlite3,os,time
from flask import Flask,request,session,g,redirect,url_for,\
abort,render_template,flash
from contextlib import closing
from datetime import datetime

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
		else:
			g.db.execute('insert into user (username,password) values (?,?)',[username,encrypt_psw(request.form['password'])])
	        g.db.commit()
	return render_template('show_entries.html')	




# init_db()
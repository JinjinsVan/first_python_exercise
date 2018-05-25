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
TODOLIST_PREFIX = "todolist_"
PAGE_LIMIT = 5

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read().decode())
	db.close()

def create_table(userid):
	with closing(connect_db()) as db:
		sql = "create table if not exists " +  TODOLIST_PREFIX + str(userid) + '''
  					(id integer primary key autoincrement,
  					title string not null,
  					date string not null,
  					status string not null
					);
			  '''
		db.cursor().executescript(sql)
	db.close()

def get_table_name():
	return TODOLIST_PREFIX + str(session['userid'])

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/register',methods=['POST','GET'])
def register():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username.strip() == '' or password.strip() == '':
			error = 'username or password cannot be empty'
		else:
		    cursor = g.db.execute('select * from user where username = ?',[username])
		    if cursor.fetchone() != None:
			    error = 'This name has been used, please change another one :) '
		    else:
			    g.db.execute('insert into user (username,password) values (?,?)',[username,utils.encrypt_password(request.form['password'],None)])
			    g.db.commit()
			    select_cur = g.db.execute('select * from user where username = ?',[username])
			    create_table(select_cur.fetchone()[0])
			    return render_template('login.html')
	return render_template('register.html',error=error)


@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username.strip() == '' or password.strip() == '':
			error = 'username or password cannot be empty'
		else:
		    cursor = g.db.execute('select * from user where username = ?',[username])
		    if cursor.fetchone() != None:
			    if(utils.validate_password(password,cursor.fetchone()[2])):
				    session['logged_in'] = True
				    session['username'] = username
				    cursor = g.db.execute('select * from user where username = ?',[username])
				    # print(cursor.fetchone()[2])
				    session['userid'] = cursor.fetchone()[0]
				    return redirect(url_for('show_list'))
			    else:
				    error = 'invalid password'
		    else:
			    error = 'there is no account named '+ username
	return render_template('login.html',error=error)


@app.route('/logout')
def logout():
	if session['logged_in'] == True:
		session.pop('logged_in',None)
		session.pop('username',None)
		session.pop('userid',None)
		flash('You were logged out')
	return redirect(url_for('show_list'))


@app.route('/add',methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	else:
		g.db.execute('insert into '+ get_table_name() +' (title,date,status) values (?,?,?)',[request.form['title'],str(datetime.now()),'0'])
		g.db.commit()
		flash('Succesfully posted')
		return redirect(url_for('show_list'))



@app.route('/delete',methods=['POST'])
def delete_entry():
	g.db.execute('update '+ get_table_name() +' set status = -1 where id =?',[request.form['id']])
	g.db.commit()
	flash("Succesfully delete")
	cursor = g.db.execute('select * from '+ get_table_name() +' where status!=-1')
	entries = [dict(id=row[0],title=row[1],date=row[2],status=row[3]) for row in cursor.fetchall()]
	return render_template('show_entries.html',entries=entries)


@app.route('/done',methods=['POST'])
def done_entry():
	g.db.execute('update '+ get_table_name() +' set status = 1 where id =?',[request.form['id']])
	g.db.commit()
	flash("done it")
	cursor = g.db.execute('select * from '+ get_table_name() +' where status=0')
	entries = [dict(id=row[0],title=row[1],date=row[2],status=row[3]) for row in cursor.fetchall()]
	return render_template('show_entries.html',entries=entries)


@app.route('/')
def show_list():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	index = request.args.get('index',default=1,type=int)
	cursor = g.db.execute('select count(*) from '+ get_table_name() +' where status=0 ')
	count = cursor.fetchall()[0][0]
	totalpage = int(count/PAGE_LIMIT)
	if count%PAGE_LIMIT != 0:
	    totalpage = totalpage + 1
	cursor = g.db.execute('SELECT * FROM '+ get_table_name() +' WHERE status=0 ORDER BY date ASC LIMIT ? OFFSET ?',[PAGE_LIMIT,(index-1*PAGE_LIMIT)])
	entries = [dict(id=row[0],title=row[1],date=row[2],status=row[3]) for row in cursor.fetchall()]
	return render_template('show_entries.html',entries=entries,count=count,thispage=index,totalpage=totalpage)



if __name__ == '__main__':
	app.debug = True
	app.run()

# init_db()
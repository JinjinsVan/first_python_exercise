import sqlite3,os,time
from flask import Flask,request,session,g,redirect,url_for,\
abort,render_template,flash
from contextlib import closing
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT,'tmp','guestbook.db')
SECRET_KEY = "development key"
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read().decode())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()

@app.route('/add',methods=['POST'])
def add_entry():

	g.db.execute('insert into guestbook (username,text,timestr) values (?,?,?)',[request.form['username'],request.form['text'],str(datetime.now())])
	g.db.commit()
	flash('Succesfully posted')
	return redirect(url_for('show_entries'))

@app.route('/')
def show_entries():
	cursor = g.db.execute('select username,text,timestr from guestbook order by id desc')
	entries = [dict(username=row[0],text=row[1],time=row[2]) for row in cursor.fetchall()]
	return render_template('show_entries.html',entries=entries)

if __name__ == '__main__':
	app.debug = True
	app.run()

# init_db()
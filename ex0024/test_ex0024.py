import os
import ex0024
import unittest
import tempfile
from flask import Flask,request

class ex0024TestCase(unittest.TestCase):
	def setUp(self):
		self.db_fd,ex0024.app.config['DATABASE']  = tempfile.mkstemp()
		ex0024.app.config['TESTING']  = True
		self.app = ex0024.app.test_client()
		ex0024.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(ex0024.app.config['DATABASE'])	

	def test_register(self):
		rv = self.app.post('/register',data=dict(username='test',password='psw'),follow_redirects=True)
		print(rv)

if __name__ == '__main__':
	unittest.main()

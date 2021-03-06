#coding=utf-8
import os,uuid,hmac,base64
import hashlib,random
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import InputRequired

def encrypt_password(psw,salt):
	if salt == None:
		salt = os.urandom(8)
	result = psw.encode()
	alog = hashlib.sha256
	for x in range(8):
		result = hmac.new(result,salt,alog).digest()
	
	return result+salt

def validate_password(psw,secret_psw):
	return secret_psw == encrypt_password(psw,secret_psw[-8:])




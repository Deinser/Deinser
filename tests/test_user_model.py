import unittest
import time
from datetime import datetime
from app import create_app,db
from app.models import User,Role

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.app=create_app('testing')
		self.app_context=self.app.app_context()
		self.app_context.push()
		db.create_all()
		Role.insert_roles()
		
	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()
		
	def test_password_setter(self):
		u=User(password='apple')
		self.assertTrue(u.password_hash in not None)
		
	def test_no_password_getter(self):
		u=User(password='apple')
		with self.assertRaises(AttributeError):
			u.password()
	def test_password_check(self):
		u=User(password='apple')
		self.assertTrue(u.check_password('apple'))
		self.assertFalse(u.check_password('banana'))
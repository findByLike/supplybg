'''
Created on 2017年6月29日

@author: Administrator
'''
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255), unique=True)
    pwd = db.Column(db.String(255), unique=True)

    def __init__(self, account, pwd):
        self.account = account
        self.pwd = pwd

    def __repr__(self):
        return '<User %r>' % self.account

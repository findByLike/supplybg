'''
Created on 2017年6月29日

@author: Administrator
'''
from flask import Flask,abort, redirect, url_for,current_app,g
from routes.users import main as routes_users
from routes.supply_order import main as supply_order
app = Flask(__name__)

def register_routes(app):
    app.register_blueprint(routes_users)
    app.register_blueprint(supply_order,url_prefix='/so')
    
    
if(__name__ == '__main__'):
    register_routes(app)
    app.run(debug=True)

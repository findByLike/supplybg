'''
Created on 2017年6月29日

@author: Administrator
'''
from flask import Flask,abort, redirect, url_for,current_app,g,render_template
from routes.users import main as routes_users
from routes.supply_order import main as supply_order
# from flask_sqlalchemy import SQLAlchemy
from models.users import User
from models import db
app = Flask(__name__)




def register_routes(app):
    app.register_blueprint(routes_users)
    app.register_blueprint(supply_order,url_prefix='/so')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/supplybg'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    
@app.route('/')
def index():
    print(User.query.all())
    return render_template('index.html')
    
if(__name__ == '__main__'):
    register_routes(app)
    app.run(debug=True)

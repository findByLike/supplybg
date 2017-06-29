'''
Created on 2017年6月29日

@author: Administrator
'''
from routes import *

main = Blueprint('users', __name__)


# @main.route('/')
# def login_view():
#     return render_template('login.html')


@main.route('/')
def index():
    return render_template('index.html')
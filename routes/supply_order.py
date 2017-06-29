'''
Created on 2017年6月29日

@author: Administrator
'''
from routes import *

main = Blueprint('supply_order', __name__)


@main.route('')
def index():
    return render_template('tt.html')
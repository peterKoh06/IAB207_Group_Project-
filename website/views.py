from flask import Blueprint, render_template
from flask_login import login_required


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')




@main_bp.route('/event/<int:id>')
def event():
    return render_template('event.html')


# History shouldn't be accessible when you aren't logged in- session 
@main_bp.route('/history')
def history():
    return render_template('history.html')

# For the payment page it should be .../eventID/payment and not just /payment 
"""
@main_bp.route('/event/<int:id>/payment')
@login_required
def payment():
    return render_template('payment.html')

"""

# You shouldn't be able to create an event when you don't have an account
@main_bp.route('/create')
@login_required
def create():
    return render_template('create.html')


@main_bp.route('/account')
def account():
    return render_template('user.html')
 


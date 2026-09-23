from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/event')
def event():
    return render_template('event.html')


# History shouldn't be accessible when you aren't logged in- session 
@main_bp.route('/history')
def history():
    return render_template('history.html')

# For the paynment page it should be .../eventID/payment and not just /payment 

#@main_bp.route('/event/payment')
#def payment():
#    return render_template('payment.html')

# You shouldn't be able to create an event when you don't have an account
@main_bp.route('/create')
def create():
    return render_template('create.html')


@main_bp.route('/newaccount')
def newaccount():
    return render_template('user.html')



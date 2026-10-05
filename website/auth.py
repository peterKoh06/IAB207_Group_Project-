from flask import (
    Blueprint, flash, render_template,
    request, url_for, redirect
)
from flask_bcrypt import check_password_hash
from flask_login import login_user, logout_user

from .models import User
from .forms import LoginForm, RegisterForm
from . import db


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(
            db.select(User).where(User.name == form.username.data)
        )

        if user is None:
            flash('Incorrect user name or password.')
        elif not check_password_hash(
            user.password_hash, form.password.data
        ):
            flash('Incorrect user name or password.')
        else:
            login_user(user)

            nextp = request.args.get('next')

            if (
                not nextp
                or not nextp.startswith('/')
                or nextp.startswith('//')
                or '\\' in nextp
            ):
                return redirect(url_for('main.index'))

            return redirect(nextp)

    return render_template(
        'user.html',
        form=form,
        heading='Login'
    )


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash(
            'Form validated successfully. '
            'Account creation is not connected yet.'
        )

    return render_template(
        'register.html',
        form=form
    )


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
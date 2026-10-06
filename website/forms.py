from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(max=100)]
    )
    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(max=100)]
    )
    email = StringField(
        'Email',
        validators=[InputRequired(), Email(), Length(max=100)]
    )
    phone_number = StringField(
        'Phone Number',
        validators=[InputRequired(), Length(max=20)]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=8, max=72)]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            InputRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired()]
    )
    submit = SubmitField('Login')
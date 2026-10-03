from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length 



class RegisterForm(FlaskForm):
  username = StringField('User Name', validators=[InputRequired(), Length(min=3, max=12)])
  email = StringField('Email ID', validators=[InputRequired(),Email() ])
  password = PasswordField('Password', validators=[InputRequired(),Length(min=8, max=12)])
  confirm = PasswordField('Confirm Password', 
          validators=[InputRequired(), EqualTo('password', message='Password must match')])
  submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

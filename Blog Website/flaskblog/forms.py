#This contains the structures of various forms to be filled inside the blog.
from flask_wtf import FlaskForm
from flask_wtf.file import  FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username): #Validate Username so that no two users have the same usernames
        
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Thats Username is Already Taken. Use Creativity and Create New One.')

    def validate_email(self, email): #Validate Email so that no two users have the same emails too.
        
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Thats Email is Already Taken. Use Creativity Here Too and Create New One.')        

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    


class UpdateAccountForm(FlaskForm):
    username = StringField('Username' , validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Your Account')

    def validate_username(self, username): #Validate Username so that no two users have the same usernames
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Thats Username is Already Taken. Use Creativity and Create New One.')

    def validate_email(self, email): #Validate Email so that no two users have the same emails too.
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Thats Email is Already Taken. Use Creativity Here Too and Create New One.')        


class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(self, email): #Validate Email so that no two users have the same emails too.
        
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with that Email. You Must Have To Register First.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Your Old Password')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp

from ..models import User, Role


class EditProfileAdminForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp(
            r"^[a-zA-Z]+[a-zA-Z0-9._]*$", 0, 'Username must have only letters, figures, dotts or underscores')
    ])
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()
    ])
    role = SelectField('Role', coerce=int)
    confirmed = BooleanField('Confirmed')
    name = StringField('Real name', validators=[Length(0, 32)])
    location = StringField('Location', validators=[Length(0, 32)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Edit profile')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.all()]
        self.user = user

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use')

    def validate_emal(self, field):
        if field.data != self.user.emal and User.query.filter_by(emal=field.data).first():
            raise ValidationError('Email is already registered')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 32)])
    location = StringField('Location', validators=[Length(0, 32)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Edit profile')

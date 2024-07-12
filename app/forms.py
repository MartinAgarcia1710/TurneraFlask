from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrarse')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')
    
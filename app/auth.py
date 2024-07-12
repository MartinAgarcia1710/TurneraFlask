from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Usuario, Datos_Personales
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .forms import RegistroForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/registrarse', methods=['GET', 'POST'])
def registro():
     form = RegistroForm()
     if form.validate_on_submit():
         usuario = Usuario(email = form.email.data)
         usuario.set_password(form.password.data)
         db.session.add(usuario)
         db.session.commit()
         datos_personales = Datos_Personales(nombre = form.nombre.data, apellido = form.apellido.data, fecha_nacimiento = form.fecha_nacimiento.data, telefono = form.telefono.data, usuario_id = usuario.id)
         db.session.add(datos_personales)
         db.session.commit()
         login_user(usuario)
         return redirect(url_for('views.loading'))
     return render_template('registro.html', form = form)
 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form.email.data).first()
        if usuario and usuario.check_password(form.password.data):
            login_user(usuario)
            flash('Login exitoso', category='success')
            return redirect(url_for('views.loading'))
        else:
            flash('Email o contraseña incorrectos.', category='error')
    return render_template('login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.loading'))
    
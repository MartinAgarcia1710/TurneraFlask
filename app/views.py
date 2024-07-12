from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from . import db
from .models import Datos_Personales, Usuario

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@views.route("/loading")
def loading():
    return render_template('loading.html', user=current_user)

@views.route("/<string:nombre>_<string:apellido>/perfil")
@login_required
def perfil(nombre, apellido):
    datos_personales = Datos_Personales.query.filter_by(nombre = nombre, apellido = apellido).first()
    return render_template('perfil.html', user = current_user, datos_personales = datos_personales)

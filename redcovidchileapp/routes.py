from flask import render_template, url_for, flash, redirect
from redcovidchileapp import app, db, bcrypt
from redcovidchileapp.forms import HospitalForm, LoginForm
from redcovidchileapp.models import User, Hospital
from flask_login import login_user, current_user


@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html', title='Ayuda')


@app.route('/donacion')
def donacion():
    return render_template('donaciones.html', title='Donaciones')


@app.route('/planos')
def planos():
    return render_template('planos.html', title='Planos')


@app.route('/hospitales')
def hospitales():
    hospitals = Hospital.query.all()
    return render_template('hospitales.html', title='Hospitales', hospitales = hospitals)

# Admin routes
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_authenticated:
        return redirect(url_for('inputs'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('inputs'))
        else:
            flash('No se pudo acceder. Por favor revisa tu email o contrasena.', 'danger')
    return render_template('admin_login.html', title='Admin Log In', form=form)


@app.route('/inputs', methods=['GET', 'POST'])
def inputs():
    if current_user.is_authenticated:
        form = HospitalForm()
        if form.validate_on_submit():
            hospital = Hospital(hospitalname=form.hospitalname.data, necesita=form.necesita.data, detalles=form.detalles.data, contacto=form.contacto.data)
            db.session.add(hospital)
            db.session.commit()
            flash('Datos Ingresados Correctamente para ' +
                    str(form.hospitalname.data), 'success')
            return redirect(url_for('inputs'))
        return render_template('inputs.html', title='Input', form=form)
    else:
        return redirect(url_for('admin'))
        
# Home
@app.route('/')
def index():
    hospitals = Hospital.query.all()
    return render_template('home.html', title='Home', hospitales=hospitals)

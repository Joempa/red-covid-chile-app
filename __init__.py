from flask import Flask, render_template, flash, redirect, url_for
from forms import HospitalForm, LoginForm

class Application(Flask):
    def __init__(self, name):
        self.logged_in = False
        Flask.__init__(self, name)

# Setup
app = Application(__name__)
app.config.from_object('config')

# Routes
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
    return render_template('hospitales.html', title='Hospitales')

# Admin routes
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@redcovidchile.cl' and form.password.data=='123456':
            app.logged_in = True
            return redirect(url_for('inputs'))
        else:
            flash('No se pudo acceder. Por favor revisa tu email o contraseña.', 'danger')
    return render_template('admin_login.html', title='Admin Log In', form=form)

@app.route('/inputs', methods=['GET', 'POST'])
def inputs():
    form = HospitalForm()
    if app.logged_in:
        if form.validate_on_submit():
            # form.hospitalname.data
            # form.necesita.data
            # form.detalles.data
            # form.contacto.data
            flash('Datos Ingresados Correctamente para ' + str(form.hospitalname.data), 'success')
            return redirect(url_for('inputs'))
        return render_template('inputs.html', title='Input', form=form)
    else:
        return redirect( url_for('index') )

# Home
@app.route('/')
def index():
    return render_template('home.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)
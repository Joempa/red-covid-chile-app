from flask import Flask, render_template


# Setup
app = Flask(__name__)
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


# Home
@app.route('/')
def index():
    return render_template('home.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)
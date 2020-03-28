from redcovidchileapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospitalname = db.Column(db.String(60), nullable=False)
    necesita = db.Column(db.String(60), nullable=False)
    detalles = db.Column(db.String(120), nullable=False)
    contacto = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Post('{self.hospitalname}', '{self.necesita}', '{self.detalles}', '{self.contacto}')"

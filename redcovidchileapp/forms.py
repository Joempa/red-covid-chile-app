from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class HospitalForm(FlaskForm):
    hospitalname = StringField('Hospitalname',
                               validators=[DataRequired(), Length(min=2, max=40)])
    necesita = StringField('Necesita',
                           validators=[DataRequired()])
    detalles = StringField('Detalles',
                           validators=[])
    contacto = StringField('Contacto',
                           validators=[DataRequired()])

    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])

    remember = BooleanField('Recuérdame')

    submit = SubmitField('Acceder')

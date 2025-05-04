

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

from flask import *
from public import public
from admin import admin
from pet_shop import petshop
from doctor import doctor
from pet_sitting import pet_sitting
from api import api

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(petshop)
app.register_blueprint(doctor)
app.register_blueprint(pet_sitting)
app.register_blueprint(api)
app.secret_key="fghjkl"

app.run(debug=True,host="0.0.0.0",port=5000)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'hariharan0987pp@gmail.com'
app.config['MAIL_PASSWORD'] = 'rjcbcumvkpqynpep'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

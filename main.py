from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5438/bookexampledb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'!\xc8\x02\x9f\x83k\xf7\x03w2dgX\xf1D\xb5\xb6\x97\x8b\xe8\x97\xd8\xd6\xdc'
db = SQLAlchemy(app)

import models

from admin import admin_page
app.register_blueprint(admin_page)
app = Flask(__name__)
@app.route("/")
def home():
 return '''My name is Omotilewa Omolayo. This is my CA2 work.
 My GitHub URL is https://github.com/Omotilewa1'''

@app.route("/")
def home():
     return render_template('home.html', title="Home")
@app.route("/signup/")
def signup():
 return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")

@app.route("/process-signup/", methods=['POST'])
def process_signup():

 firstname = request.form['firstname']
 Surname = request.form['Surname']
 Dateofbirth = request.form['Dateofbirth']
 Nationality = request.form['Nationality']
 ResidentialAddress = request.form['Residential Address']
 NIN = request.form['NIN']

 password = request.form['password']
 #
 try:
    user = models.User(firstname=firstname, Surname=Surname, Dateofbirth=Dateofbirth, Nationality=Nationality, NIN=NIN, ResidentialAddress=ResidentialAdress, password=password)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

 except Exception as e:
    # Error caught, prepare error information for return
    information = 'Could not submit. The error message is {}'.format(e.__cause__)
    return render_template('signup.html', title="SIGN-UP", information=information)


 information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, lastname, email)

 return render_template('signup.html', title="SIGN-UP", information=information)



if __name__ == "__main__":
 app.run(port=5005)
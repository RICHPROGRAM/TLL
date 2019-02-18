from flask import Flask, render_template, flash, request, session, url_for, Markup, redirect, send_from_directory, json
from werkzeug.utils import secure_filename
import os
import json
from models import *
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tll'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'qwertyuioplkjhgfdsazxcvbnm'

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("basic.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/how_it_works")
def howitworks():
    return render_template("how_it_works.html")

@app.route("/connect")
def connect():
    consultants = Consultants.query.all()
    return render_template("connect.html", consultants= consultants)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/consultant", methods=['GET', 'POST'])
def consultant():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        bio = str(request.form.get('bio'))
        qualification = str(request.form.get('qualification'))
        expertise = str(request.form.get('expertise'))
        posts = Consultants(name=name, bio=bio, qualification=qualification, expertise=expertise)
        db.session.add(posts)
        db.session.commit()
    return render_template("advisor.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__== "__main__":
 app.run()

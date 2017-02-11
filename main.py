import os
from peewee import *
from flaskr.connectdatabase import ConnectDatabase
from flaskr.models import Entries
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app
from models import *


app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('list'))

@app.route('/and/list')
def list():
    sprinters = Sprinter.select().order_by(Sprinter.id)
    return render_template("list.html", sprinters = sprinters)

@app.route('/story')
def story():
    return render_template("form.html")

if __name__  == "__main__":
    app.run(debug = True)
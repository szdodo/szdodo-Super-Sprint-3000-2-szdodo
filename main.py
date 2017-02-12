import os
from peewee import *
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

@app.route('/story/<id>', methods=['POST', 'GET'])
def story(id):
    print(id)
    return render_template("form.html")

@app.route('/delete/<id>')
def delete(id):
    row = Sprinter.get(Sprinter.id == id)
    row.delete_instance()
    return redirect(url_for('list'))

@app.route('/add_story', methods=['POST'])
def add_story():
    Sprinter.create(title=request.form['title'],
                    story=request.form['story'],
                    acceptance_criteria=request.form['criteria'],
                    business_value=request.form['value_in'],
                    estimation=request.form['estimation_in'],
                    status=request.form['status'])
    flash('New story was successfully posted')
    return redirect(url_for('list'))

if __name__  == "__main__":
    app.run(debug = True)
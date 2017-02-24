import os
from peewee import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app
from models import *


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='development key'
))


@app.route('/')
def index():
    return redirect(url_for('list'))

@app.route('/list')
def list():
    sprinters = Sprinter.select().order_by(Sprinter.id)
    return render_template("list.html", sprinters = sprinters)

@app.route('/story/<id>', methods=['GET','POST'])
def story(id):
    if Sprinter.select().where(Sprinter.id == id).exists():
        user_story = Sprinter.get(Sprinter.id == id)
    else:
        user_story=None
    return render_template("form.html",user_story=user_story)

@app.route('/delete/<id>')
def delete(id):
    row = Sprinter.get(Sprinter.id == id)
    row.delete_instance()
    return redirect(url_for('list'))

@app.route('/add_story', methods=['GET','POST'])
def add_story():
    title=request.form['title']
    story=request.form['story']
    ac_cr=request.form['criteria']
    bu_va=request.form['business_value']
    est=request.form['estimation']
    sta=request.form['status']
    new_story = Sprinter.create(title=title,
                    story=story,
                    acceptance_criteria=ac_cr,
                    business_value=bu_va,
                    estimation=est,
                    status=sta)
    new_story.save()
    flash('New story was successfully posted')
    return redirect(url_for('list'))

@app.route('/update_story', methods=['GET','POST'])
def update_story():
    id = request.form['id']
    title = request.form['title']
    story = request.form['story']
    ac_cr = request.form['criteria']
    bu_va = request.form['business_value']
    est = request.form['estimation']
    sta = request.form['status']
    user_story=Sprinter.update(title=title,
                               story=story,
                               acceptance_criteria=ac_cr,
                               business_value=bu_va,
                               estimation=est,
                               status=sta).where(Sprinter.id == id)
    user_story.execute()
    return redirect(url_for('list'))

if __name__  == "__main__":
    app.run(debug = True)
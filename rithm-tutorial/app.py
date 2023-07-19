""" flask project

Run using `flask run`
"""
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_modus import Modus  # required for form to take PATCH requests
from toy import Toy

app = Flask(__name__)
modus = Modus(app)  # required for form to take PATCH requests

duplo = Toy(name='duplo')
lego = Toy(name='lego')
knex = Toy(name='knex')

toys = [duplo, lego, knex]

# listen for a route to '/' (root route)
@app.route('/')
def hello():
  return "Hello!"

@app.route('/toys', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    toys.append(Toy(request.form['name']))
    return redirect(url_for('index'))

  return render_template("index.html", toys=toys)

@app.route('/toys/new')
def new():
  return render_template("new.html")

@app.route('/toys/<int:id>', methods=["GET", "PATCH"])
def show(id):
  found_toy = next((t for t in toys if t.id == id), None)
  return render_template("show.html", toy=found_toy)

@app.route('/toys/<int:id>/edit')
def edit(id):
  found_toy = next((t for t in toys if t.id == id), None)
  return render_template("edit.html", toy=found_toy)
""" flask project

Run using `flask run`
"""
from flask import Flask
from flask import render_template
from toy import Toy

app = Flask(__name__)

duplo = Toy(name='duplo')
lego = Toy(name='lego')
knex = Toy(name='knex')

toys = [duplo, lego, knex]

# listen for a route to '/' (root route)
@app.route('/')
def hello():
  return "Hello!"

@app.route('/toys')
def index():
  return render_template("index.html", toys=toys)
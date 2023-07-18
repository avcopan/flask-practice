""" flask project

Run using `flask run`
"""
from flask import Flask

app = Flask(__name__)

# listen for a route to '/' (root route)
@app.route('/')
def hello():
  return "Hello you!"

@app.route('/name')
def welcome():
  return "Welcome to our application!"

@app.route('/welcome')
def welcome1():
  return "Welcome"

@app.route('/welcome/home')
def welcome2():
  return "Welcome home."

@app.route('/welcome/back')
def welcome3():
  return "Welcome back!"

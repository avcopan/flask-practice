""" flask project

Run using `flask run`
"""
from flask import Flask
import operator

app = Flask(__name__)

# listen for a route to '/' (root route)
@app.route('/')
def hello():
  return "Hello!"

@app.route('/name/<person>')
def say_name(person):
  return f"The name is {person}"

@app.route('/name/<int:num>')
def favorite_number(num):
  return f"Your favorite number is {num}, which is half of {num * 2}"

@app.route('/math/<operation>/<int:num1>/<int:num2>')
def math(operation, num1, num2):
  op_dct = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': operator.floordiv,
  }
  op_key = operation.lower()[:3]
  return str(op_dct[op_key](num1, num2))

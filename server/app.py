#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    numbers_str = '\n'.join(str(num) for num in numbers)
    numbers_str += '\n'

    return numbers_str

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return "Invalid operation", 400
    except ValueError as e:
        return str(e), 400

    return str(result)

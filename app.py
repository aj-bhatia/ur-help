from flask import Flask, render_template
import os


app = Flask(__name__)
IS_DEV = app.env == 'development'

@app.route('/')
@app.route('/index/')
def main():
    return render_template('index.html')

@app.route('/project/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/aboutus/')
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/join/')
def about():
    return '<h3>This is a Flask web application.</h3>'

    
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)
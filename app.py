# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/learninghub')
def learningHub():
    return render_template('learning_hub.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')


@app.route('/product_list')
def products():
    return render_template('product_list.html')

if __name__ == '__main__':
    app.run(debug=True)

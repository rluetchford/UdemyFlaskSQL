from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Create instance of Flask class
app = Flask(__name__)

#Specify database connection
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:TheOracle1981@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qlczlmggtcjhun:a78662b78eb964525d23ebd10a187f5976a1416f5d760ef96b20ebb6eb9b7615@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com:5432/d3vkm1bpgmi3i2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Create instance of SQLAlchemy
db = SQLAlchemy(app)

#Create table in DB
class Favequotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favequotes.query.all()
    return render_template('index.html', result = result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favequotes(author = author, quote = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
# wsgi.py
from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    isvalid = game.isvalid(word)
    return render_template('check.html', isvalid=isvalid, grid=game.grid, word=word)

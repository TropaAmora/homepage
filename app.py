from flask import Flask,render_template,session,redirect,url_for,jsonify,send_from_directory
import os

app = Flask(__name__)


@app.route("/",methods=["GET"])
def index():
    file = 'home'
    return render_template("home.html", file=file)

@app.route("/about", methods=["GET"])
def about():
    file = 'about'
    return render_template("about.html", file=file)

@app.route("/skills", methods=["GET"])
def skills():
    file = 'skills'
    return render_template("skills.html", file=file)

@app.route("/portfolio", methods=["GET"])
def portfolio():
    file = 'portfolio'
    return render_template("portfolio.html", file=file)

@app.route("/contact", methods=["GET"])
def contact():
    file = 'contact'
    return render_template("contact.html", file=file)
from flask import Flask,render_template,session,redirect,url_for,jsonify,send_from_directory

app = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")
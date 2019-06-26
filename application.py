import os

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if session.get("logged_in"):
        # return render_template("flack.html", username=session["user_name"])
        return "Welcome"
    else:
        return redirect(url_for("sign_in"))


@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")


@app.route("/login", methods=["POST"])
def login():
    # Get form information.
    username = request.form.get("username")

    session["user_name"] = username
    session["logged_in"] = True
    # return render_template("search.html")
    return "Welcome"


@app.route("/logout")
def logout():
    session["user_name"] = None
    session["logged_in"] = False
    session.clear()
    # return render_template("welcome.html")
    return redirect(url_for("index"))


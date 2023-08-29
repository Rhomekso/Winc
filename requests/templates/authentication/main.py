import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = get_users()  # Get the dictionary of users and hashed passwords
        
        if username in users and users[username] == hash_password(password):
            # Successful login
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            # Failed login
            return redirect(url_for("login", error=True))
    
    # If it's a GET request or login failed
    error = request.args.get("error")
    return render_template("login.html", title="Login", error=error)


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        
        if username == "Alice":
            greeting = "Hello, Alice! Welcome to your dashboard."
            extra_content = "Here's some personalized content for you."
        elif username == "Bob":
            greeting = "Hey there, Bob! This is your dashboard."
            extra_content = "Enjoy the customized content we have for you."
        else:
            greeting = f"Welcome, {username}! This is your dashboard."
            extra_content = "Explore the personalized features available to you."
        
        return render_template("dashboard.html", title="Dashboard", greeting=greeting, extra_content=extra_content)
    else:
        return redirect(url_for("login"))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None)  # Remove the 'username' entry from the session
    return redirect(url_for("index"))  # Redirect to the home page

if __name__ == "__main__":
    app.run(debug=True)

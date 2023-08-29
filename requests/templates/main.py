from flask import Flask, render_template, redirect

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)

@app.route("/home")
def home():
    return redirect("/")

@app.route("/")
def index():
    title = "Index"
    return render_template("index.html", page_title=title)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", page_title=title)

@app.route('/third')
def contact():
    title = "Third Page"
    return render_template('third.html', page_title=title)


if __name__ == '__main__':
    app.run(debug=True)

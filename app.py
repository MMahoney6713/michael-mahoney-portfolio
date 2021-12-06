from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/projects")
def projects():

    return render_template("projects.html")

@app.route("/about")
def about():

    return render_template("about-me.html")

@app.route("/resume")
def resume():

    return render_template("resume.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
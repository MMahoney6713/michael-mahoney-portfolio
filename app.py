from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route("/")
def homepage():
    return render_template("index.html")


########################################################
##### Project Routes   #################################
########################################################

@app.route("/projects")
def projects():
    return render_template("projects/projects.html")

@app.route("/projects/rpi-server")
def projects_server():
    return render_template("projects/rpi-server.html")

@app.route("/projects/capstone1")
def projects_capstone1():
    return render_template("projects/capstone1.html")

@app.route("/projects/warbler")
def projects_warbler():
    return render_template("projects/warbler.html")



########################################################
##### About Me / Resume Routes  ########################
########################################################

@app.route("/about")
def about():
    return render_template("about-me.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
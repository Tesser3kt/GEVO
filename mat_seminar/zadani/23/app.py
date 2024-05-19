from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("home_page.html")


@app.route("/page1")
def page1():
    items = ["Věc 1", "Věc 2", "Věc 3"]

    # Tady chcete vykreslit sablonu page1.html a předat jí proměnnou items.

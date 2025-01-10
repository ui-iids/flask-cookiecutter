from flask import Blueprint, render_template
from werkzeug import exceptions

pages = Blueprint("pages", __name__)


@pages.route("/", methods=["GET", "POST"])
def index():
    return render_template("pages/index.html")


@pages.route("/page")
def example_page():
    return render_template("pages/example_page.html")

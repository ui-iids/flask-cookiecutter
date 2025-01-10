from .example import example_api_v1
from flask import Flask


def register_apis(app: Flask):
    app.register_blueprint(example_api_v1)

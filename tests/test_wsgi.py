from unittest.mock import patch
from project_name.wsgi import app
from flask import Flask


def test_wsgi():
    assert isinstance(app, Flask)
    assert app.name == "project_name.app"

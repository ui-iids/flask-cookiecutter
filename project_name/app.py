from flask import Flask, render_template, send_file
from tomllib import load as tomlload
from werkzeug import exceptions
from collections import namedtuple

from .pages import pages
from .api import register_apis


def create_app(config_filename="config.toml", config_override={}):
    app = Flask(__name__)

    app.register_blueprint(pages)

    @app.errorhandler(exceptions.NotFound)
    def page_not_found(e):
        return render_template("pages/404.html"), 404

    @app.errorhandler(exceptions.InternalServerError)
    def server_error(e):
        return render_template("pages/error.html"), 500

    app.config.from_file(config_filename, load=tomlload, text=False, silent=True)
    app.config.from_object(namedtuple("Config", config_override)(**config_override))
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    # For debug purposes, we compile CSS every time it changes
    if app.debug:
        from sassutils.wsgi import SassMiddleware

        app.wsgi_app = SassMiddleware(
            app.wsgi_app,
            {
                "project_name": {
                    "sass_path": "static/sass",
                    "css_path": "static/css",
                    "wsgi_path": "/static/css",
                    "strip_extension": True,
                }
            },
        )

    register_apis(app)

    if app.config.get("SERVE_PWA"):

        @app.route("/manifest.json", methods=["GET"])
        def route_app_manifest():
            return send_file(
                "static/manifest.json", mimetype="application/manifest+json"
            )

        @app.route("/sw.js", methods=["GET"])
        def route_sw_root():
            return send_file("static/js/sw.js", mimetype="application/javascript")

    return app

from flask_smorest import Api, Blueprint, abort
from flask.views import MethodView
import marshmallow as ma
from flask import Flask

api_prefix = "example"
api_title = "Example API"
api_version = "1"


blp = Blueprint(
    api_prefix,
    api_prefix,
    url_prefix=f"/{api_prefix}/{api_version}",
    description="Example API in this Flask app.",
)


class loremSchema(ma.Schema):
    body = ma.fields.String()


@blp.route("/lorem")
class Lorem(MethodView):
    @blp.response(200, loremSchema, example={"body": "Lorem Ipsum Dolor Sit Amet"})
    def get(self):
        "Return a short Lorem Ipsum text."
        return {"body": "Lorem Ipsum Dolor Sit Amet"}


def register_api(app: Flask):
    config_prefix = f"{api_prefix}_{api_version.replace('.','-')}_"
    api_config = {
        "api_version": api_version,
        "openapi_version": "3.1.1",
        "api_title": api_title,
        "openapi_url_prefix": f"/{api_prefix}/{api_version}/docs/",
        "openapi_swagger_ui_path": "ui",
        "openapi_json_path": "openapi.json",
        "openapi_swagger_ui_version": "5.18.2",
        "openapi_swagger_ui_url": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.18.2/",
    }
    prefixed_config = {
        f"{config_prefix}{key}".upper(): val for key, val in api_config.items()
    }

    app.config.update(prefixed_config)
    api = Api(
        app,
        config_prefix=config_prefix,
    )
    api.register_blueprint(blp)

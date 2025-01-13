from tempfile import NamedTemporaryFile
from application_name import create_app


def test_create_app_handles_no_file():
    app = create_app("nonexistent.file")
    app.config.update({"TESTING": True})


def test_create_app_handles_config():
    with NamedTemporaryFile() as config_file:
        config_file.write(b"PYTEST_EXAMPLE_CONFIG=true\nOVERRIDED_PARAM=0")
        config_file.flush()
        app = create_app(config_file.name, {"OVERRIDED_PARAM": 1, "OTHER_PARAM": 2})
        print(app.config)
        assert app.config.get("PYTEST_EXAMPLE_CONFIG") == True
        assert app.config.get("OTHER_PARAM") == 2
        assert app.config.get("OVERRIDED_PARAM") == 1

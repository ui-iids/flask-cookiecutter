# project_name

project_description

## Install

This package uses `poetry` as its build system and package manager.

To install the project, install `poetry >= 2.0` through your local package manager or `pip`. 

Certain tools, such as `vscode` or `pycharm`, would like the virtual environment to live in the directory, so configure poetry:

```
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
```

Then run

```
poetry install
```

in the root directory.

## Run

To run the project as a developer, run:

```bash
poetry run flask --app project_name run --debug
```

To run the project as a standalone server, run:
```bash
gunicorn
```

To run the project in a container, after installing docker, run:
```bash
docker build -t project_name -f Containerfile .
docker run -d --name project_name -p 8005:8000 project_name
python -m webbrowser http://localhost:8005
```

And to delete, run:
```bash
docker stop project_name
docker container rm project_name
docker image rm project_name
```

## Deploy

## Updating

## Authors

Clinton Bradford, cbradford@uidaho.edu

Based on the [IIDS Flask Cookiecutter](https://github.com/northwest-knowledge-network/iids-flask-cookiecutter)
import json


def test_home_correct(client):
    response = client.get("/example/1/lorem")
    assert response.status_code == 200
    assert json.loads(response.data) == {"body": "Lorem Ipsum Dolor Sit Amet"}


def test_home_rejects_post(client):
    response = client.post("/example/1/lorem")
    assert response.status_code == 405


def test_error(client):
    response = client.get("/example/1/NOT_AN_API")
    assert response.status_code == 404

#import pytest

from flaskr import create_app

app = create_app()

def test_hello():
    response = app.test_client().get('/hello')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

def test_tell_me_sth():
    response = app.test_client().get('/tell-me-sth')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '{"are_you_sure":"GET"}\n'

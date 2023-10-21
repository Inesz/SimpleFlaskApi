#import pytest

from flaskr import create_app

app = create_app()

def test_index_route():
    response = app.test_client().get('/hello')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'

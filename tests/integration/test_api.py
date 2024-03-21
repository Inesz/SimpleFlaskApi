import pytest

from flaskr import create_app, SomeInput
from flaskr.api_input import Gender

app = create_app()

TELL_ME_STH = '/tell-me-sth'
VALIDATION = '/validation'
def test_hello():
    response = app.test_client().get('/hello')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, World!'


def test_tell_me_sth_get():
    response = app.test_client().get(TELL_ME_STH)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '{"are_you_sure":"GET"}\n'


@pytest.mark.parametrize("body,content_type,rsp_msg", [
    ('{"sentence": "It all depends on how much it cost"}', "application/json",
     '{"i_see":"b\'{\\"sentence\\": \\"It all depends on how much it cost\\"}\'"}\n'),
    ('something is too much', "text/plain", '{"i_see":"b\'something is too much\'"}\n')
])
def test_tell_me_sth_post(body, content_type, rsp_msg):
    response = app.test_client().post(TELL_ME_STH, data=body, mimetype=content_type)

    assert response.status_code == 200
    assert response.data.decode('utf-8') == rsp_msg


def test_tell_me_sth_err():
    out = app.test_client().put(TELL_ME_STH)

    assert out.status_code == 405
    assert out.data.decode('utf-8') == '{"code":"The method is not allowed for the requested URL.","str":405}\n'


def test_validation():
    body = SomeInput(name="abc", age=19, acceptance=False, gender=Gender.F, preferences="yellow")
    json_body = body.model_dump_json()

    with app.app_context():
        out = app.test_client().post(VALIDATION, data=json_body, mimetype="application/json")

    assert out.status_code == 200
    assert out.data.decode('utf-8')[2:-3] == json_body[2:-2].replace(" ", "")

def test_give():
    response = app.test_client().get('/give-serialized/123')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '{"name":"abc","age":123,"accepted":true,"option":null,"gender":"f","preferences":"yellow"}\n'


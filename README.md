# Simple Flask server for tests

## How to start
* import dependencies: pip install -r requirements.txt
* run from terminal: flask --app flaskr run --debug
* run from main function: flaskr/main.py

## Endpoints
Server is running on http://127.0.0.1:5000

* /hello - simple hello message
* /tell_me_sth - simple get and post message
* /validation - input with pydantic validation

## tests
pytest tests/integration/test_api.py

## project structure
* [api](flaskr)
* [tests](tests)

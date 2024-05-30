import bottle_app


def test_hello_world():
    assert bottle_app.hello_world() == 'Hello from Python0'

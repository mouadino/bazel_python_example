import pytest
from pyramid.testing import testConfig

from backend.routes import echo


def test_echo():
    with testConfig() as config:
        config.add_route('echo', '/echo/{name}')
        req = DummyRequest(path='/echo/hello')
        resp = echo(req)

        assert resp.body == 'hello'

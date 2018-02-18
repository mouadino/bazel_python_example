import grpc

from echo import EchoServer, EchoService

from echo.proto import echo_pb2_grpc, echo_pb2_grpc


_server = _client = None


def _get_random_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def setup_module(module):
    module._server = EchoServer(EchoService(), _get_random_port())
    module._server.start()
    channel = grpc.insecure_channel('localhost:{port}'.format(port=TEST_PORT))
    module._client = proto.echo.EchoStub(channel)


def teardown_module(module):
    module._server.stop()


def test_echo():
    reply = _client.Echo(echo_pb2.EchoReply(name='you'))
    assert reply.message == 'you!'

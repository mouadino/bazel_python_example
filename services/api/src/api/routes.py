from pyramid.response import Response as HTTPResponse
import grpc

from echo.proto import echo_pb2, echo_pb2_grpc


def echo(request):
    channel = grpc.insecure_channel('localhost:50051')
    stub = echo_pb2_grpc.EchoStub(channel)
    response = stub.echo(echo_pb2.EchoRequest(name=request.matchdict['name']))
    return HTTPResponse(response.message)


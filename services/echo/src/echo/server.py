import grpc
import time

from concurrent import futures
from proto.echo import echo_pb2, echo_pb2_grpc


class EchoServer(object):

    def __init__(self, echo_service, server_port):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_EchoServicer_to_server(echo_service, self.server)
        self.server.add_insecure_port('[::]:{server_port}'.format(server_port=server_port))

    def start(self):
        self.server.start()

    def stop(self):
        self.server.stop(0)

    def await_termination(self):
        """
        server.start() doesn't block so we explicitly block here unless someone keyboard-exits us.
        :return:
        """
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            self.server.stop(0)
        pass


class EchoService(echo_pb2_grpc.echoServicer):

    def echo(self, request, context):
        reply = echo_pb2.EchoReply()
        reply.message = 'Hello {name}'.format(name=request.name)
        return reply

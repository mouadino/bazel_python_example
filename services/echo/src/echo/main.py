#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .server import EchoServer, EchoService


def main():
    server = EchoServer(EchoService(), 50051)
    server.start()
    server.await_termination()


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from wsgiref.simple_server import make_server

from pyramid.config import Configurator

from . import routes


def setup_logging():
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level='DEBUG', stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    setup_logging()

    with Configurator() as config:
        config.add_route('echo', '/echo/{name}')
        config.add_view(routes.echo, route_name='echo')
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()


def run():
    main()


if __name__ == "__main__":
    run()

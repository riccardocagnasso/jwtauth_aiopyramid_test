import logging.config

from pyramid.config import Configurator
import pyramid_jwtauth

from pyramid.security import Allow, Everyone, Authenticated


class RootFactory(object):
    __acl__ = [(Allow, Authenticated, 'user'),
               (Allow, 'admin', ('admin'))]

    def __init__(self, request):
        pass


def groupfinder(username, request):
    """Placeholder groupfinder"""
    return ["admin"]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # support logging in python3
    logging.config.fileConfig(
        settings['logging.config'],
        disable_existing_loggers=False
    )

    config = Configurator(settings=settings)
    config.set_root_factory(RootFactory)

    config.add_route('index', '/')
    config.add_route('secure', '/secure')
    config.scan()

    return config.make_wsgi_app()

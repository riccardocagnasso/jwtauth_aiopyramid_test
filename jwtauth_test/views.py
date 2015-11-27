import asyncio

from pyramid.interfaces import IAuthenticationPolicy
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPForbidden

USERNAME = "foo"


@view_config(route_name="index", renderer='template.pt')
def index(request):
    policy = request.registry.queryUtility(IAuthenticationPolicy)
    token = policy.encode_jwt(request, claims={"sub": USERNAME})

    return {
        "token": token.decode("utf-8"),
        "username": USERNAME
        }


@view_config(route_name="secure", renderer="json")
def secure(request):
    if not request.has_permission('admin'):
        return HTTPForbidden()
    else:
        return {"success": True}

from zope.interface import Interface as I

from bit.bot.common.interfaces import ISocketRequest


class IHTTPSocketRequest(ISocketRequest):
    """ an HTTP request object """

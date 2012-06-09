from zope.component import getUtility

from twisted.web import server

from bit.core.interfaces import IConfiguration


def getWSPort():
    return int(getUtility(IConfiguration).get('ws', 'port') or 0)


def getWSSPort():
    return int(getUtility(IConfiguration).get('wss', 'port') or 0)


def getFlashPolicyPort():
    return 8043

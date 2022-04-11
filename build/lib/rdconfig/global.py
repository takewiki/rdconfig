from .private import __varName__
from .private import __varCaption
from .protect import _varTag_
from .protect import _varTitle


def getName():
    print(__varName__)


def getCaption():
    print(__varCaption)


def __getCaption():
    print(__varCaption)

def getTag():
    print(_varTag_)

def getTitle():
    print(_varTitle)

def __getTitle():
    print(_varTitle)


class glb_testPrivate():
    def __getCaption():
        print(__varCaption)

    def getName():
        print(__varName__)
class glb_testProtect():
    def getTitle():
        print(_varTitle)

    def __getTitle():
        print(_varTitle)
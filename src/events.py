import typing
from types import ModuleType
plugs: typing.Dict[str, ModuleType] = {} #: Contains the plugs
info: typing.Dict[str, any] = {
    "bookmarks": [],
    "current_url": "",
    "change_url_call": None,
    "update_url_bar_call": None,
    "refresh_call": None,
    "reload_bookmarks": None
} #: Contains info about the browser
def callLoadEvent():
    """Called after the browser is initialized"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "onload"):
            info = plugs[i].onload(info)
def callPreLoad():
    """Called before the browser is initialized"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "preload"):
            info = plugs[i].preload(info)
def callBookmarkClicked(bookmark):
    """Called when a bookmark is clicked"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "bookmark_clicked"):
            info = plugs[i].bookmark_clicked(info, bookmark)
def callUrlBarEnter(url):
    """Called when a url is submitted via the URL bar"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "return_url_bar"):
            info = plugs[i].return_url_bar(info, url)
def callUrlChanged(url):
    """Called with the URL has changed"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "url_changed"):
            info = plugs[i].url_changed(info, url)
def callRefresh():
    """Called when the page is refreshed"""
    global info
    for i in plugs:
        if hasattr(plugs[i], "refresh"):
            info = plugs[i].refresh(info)
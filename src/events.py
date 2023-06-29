import typing
from types import ModuleType
plugs: typing.Dict[str, ModuleType] = {}
info: typing.Dict[str, any] = {
    "bookmarks": [],
    "current_url": "",
    "change_url_call": None,
    "update_url_bar_call": None,
    "refresh_call": None
}
# Called after the browser is initialized
def callLoadEvent():
    global info
    for i in plugs:
        if hasattr(plugs[i], "onload"):
            info = plugs[i].onload(info)
# Called before the browser is initialized
def callPreLoad():
    global info
    for i in plugs:
        if hasattr(plugs[i], "preload"):
            info = plugs[i].preload(info)
# Called when a bookmark is clicked
def callBookmarkClicked(bookmark):
    global info
    for i in plugs:
        if hasattr(plugs[i], "bookmark_clicked"):
            info = plugs[i].bookmark_clicked(info, bookmark)
# Called when a url is submitted via the URL bar
def callUrlBarEnter(url):
    global info
    for i in plugs:
        if hasattr(plugs[i], "return_url_bar"):
            info = plugs[i].return_url_bar(info, url)
# Called with the URL has changed
def callUrlChanged(url):
    global info
    for i in plugs:
        if hasattr(plugs[i], "url_changed"):
            info = plugs[i].url_changed(info, url)
# Called when the page is refreshed
def callRefresh():
    global info
    for i in plugs:
        if hasattr(plugs[i], "refresh"):
            info = plugs[i].refresh(info)
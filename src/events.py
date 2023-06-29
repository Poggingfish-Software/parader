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
def callLoadEvent():
    global info
    for i in plugs:
        if hasattr(plugs[i], "onload"):
            info = plugs[i].onload(info)
def callPreLoad():
    global info
    for i in plugs:
        if hasattr(plugs[i], "preload"):
            info = plugs[i].preload(info)
def callBookmarkClicked(bookmark):
    global info
    for i in plugs:
        if hasattr(plugs[i], "bookmark_clicked"):
            info = plugs[i].bookmark_clicked(info, bookmark)
def callUrlBarEnter(url):
    global info
    for i in plugs:
        if hasattr(plugs[i], "return_url_bar"):
            info = plugs[i].return_url_bar(info, url)
def callUrlChanged(url):
    global info
    for i in plugs:
        if hasattr(plugs[i], "url_changed"):
            info = plugs[i].url_changed(info, url)
def callRefresh():
    global info
    for i in plugs:
        if hasattr(plugs[i], "refresh"):
            info = plugs[i].refresh(info)
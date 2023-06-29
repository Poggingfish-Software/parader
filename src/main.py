import hy
import sys
import src.plug
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QUrl
from time import perf_counter
import src.events as events
from PyQt5.QtCore import Qt
from typing import Dict
rl = 0
def load_plugs():
    """Load plugins"""
    global rl
    events.plugs = {}
    events.info["bookmarks"] = []
    events.info["ctx"] = []
    for i in src.plug.plugs:
        f = importlib.import_module(i[1])
        f = importlib.reload(f)
        events.plugs.update({i[0]: f})
    if rl != 0:
        events.onReloadPlugs()
    rl+=1
class Window(QMainWindow):
    """The main window for the browser."""
    def change_url(self):
        "Changes the URL of the webview to the current ``events.info[\"current_url\"]``"
        self.webview.load(QUrl(events.info["current_url"]))
    def update_url_bar_call(self):
        "Updates the URL bar to the current ``events.info[\"current_url\"]``"
        self.URLBar.setText(events.info["current_url"])
    def refresh_call(self):
        "Reloads the current page on the webview"
        self.webview.reload()
    def reload_bookmarks(self):
        "Reloads the bookmarks"
        self.actionbar.clear()
        for i in events.info["bookmarks"]:
            self.bmv.update({i[0]: QAction(i[0], self)})
            self.bmv[i[0]].triggered.connect(lambda _, value=i[1]: events.callBookmarkClicked(value))
            self.actionbar.addAction(self.bmv[i[0]])
    def showCtx(self, point):
        "Displays the context menu"
        menu = QMenu()
        for i in events.info["ctx"]:
            action = QAction(i[0], self)
            action.triggered.connect(lambda _, f=i[1]: events.call(f))
            menu.addAction(action)
        menu.exec(self.mapToGlobal(point))
    def run_js(self, js: str):
        """Runs javascript"""
        self.webview.page().runJavaScript(js, 0)
    def __init__(self, *args, **kwargs):
        events.info["change_url_call"] = lambda: self.change_url()
        events.info["update_url_bar_call"] = lambda: self.update_url_bar_call()
        events.info["refresh_call"] = lambda: self.refresh_call()
        events.info["run_js"] = lambda js: self.run_js(js)
        events.info["reload_plugs"] = lambda: load_plugs()
        super(Window, self).__init__(*args, **kwargs)
        self.actionbar: QToolBar = QToolBar("actionbar", self) #: Bookmarks bar.
        self.navbar: QToolBar = QToolBar("navbar", self) #: Navbar, Contains URL bar and Refresh button
        self.addToolBar(Qt.TopToolBarArea, self.navbar)
        self.URLBar: QLineEdit = QLineEdit() #: URl Bar, child of navbar
        self.Refresh: QPushButton = QPushButton("Refresh") #: Refresh button, child of navbar
        self.RefreshKey: QShortcut = QShortcut(self) #: Makes F5 call the refresh event
        self.RefreshKey.setKey(QKeySequence(Qt.Key.Key_F5))
        self.RefreshKey.activated.connect(lambda: events.callRefresh())
        self.Refresh.clicked.connect(lambda: events.callRefresh())
        self.URLBar.returnPressed.connect(lambda: events.callUrlBarEnter(self.URLBar.text()))
        self.navbar.addWidget(self.URLBar)
        self.navbar.addWidget(self.Refresh)
        self.addToolBarBreak()
        self.addToolBar(Qt.TopToolBarArea, self.actionbar)
        self.bmv: Dict[str, str] = {} #: Bookmark items in the Action Bar
        self.reload_bookmarks()
        self.actionbar.update()
        self.webview = QWebEngineView()
        self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.webview.customContextMenuRequested.connect(self.showCtx)
        self.webview.load(QUrl("https://example.com"))
        self.webview.urlChanged.connect(lambda: events.callUrlChanged(self.webview.url().url()))
        self.setCentralWidget(self.webview)
        self.show()
        load_end = perf_counter()
        events.info["load_time"] = load_end-events.info["load_time"]
        events.callLoadEvent()
def main():
    """Runs the browser!"""
    load_plugs()
    events.info["load_time"] = perf_counter()
    events.callPreLoad()
    app = QApplication(sys.argv)
    app.setApplicationName("Parader")
    window = Window()
    app.exec_()
if __name__ == "__main__":
    main()
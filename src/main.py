refs = locals()
import src.render_xhtml
import hy
import sys
import src.plug
import importlib
import random
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QUrl
from types import ModuleType
from time import perf_counter
import src.events as events
from PyQt5.QtCore import Qt
class Window(QMainWindow):
    def change_url(self):
        self.webview.load(QUrl(events.info["current_url"]))
    def update_url_bar_call(self):
        self.URLBar.setText(events.info["current_url"])
    def refresh_call(self):
        self.webview.reload()
    def __init__(self, *args, **kwargs):
        events.info["change_url_call"] = lambda: self.change_url()
        events.info["update_url_bar_call"] = lambda: self.update_url_bar_call()
        events.info["refresh_call"] = lambda: self.refresh_call()
        super(Window, self).__init__(*args, **kwargs)
        self.actionbar = QToolBar("actionbar", self)
        self.navbar = QToolBar("navbar", self)
        self.addToolBar(Qt.TopToolBarArea, self.navbar)
        self.URLBar = QLineEdit()
        self.Refresh = QPushButton("Refresh")
        self.RefreshKey = QShortcut(self)
        self.RefreshKey.setKey(QKeySequence(Qt.Key.Key_F5))
        self.RefreshKey.activated.connect(lambda: events.callRefresh())
        self.Refresh.clicked.connect(lambda: events.callRefresh())
        self.URLBar.returnPressed.connect(lambda: events.callUrlBarEnter(self.URLBar.text()))
        self.navbar.addWidget(self.URLBar)
        self.navbar.addWidget(self.Refresh)
        self.addToolBarBreak()
        self.addToolBar(Qt.TopToolBarArea, self.actionbar)
        self.bmv = {}
        for i in events.info["bookmarks"]:
            self.bmv.update({i[0]: QAction(i[0], self)})
            self.bmv[i[0]].triggered.connect(lambda _, value=i[1]: events.callBookmarkClicked(value))
            self.actionbar.addAction(self.bmv[i[0]])
        self.actionbar.update()
        self.webview = QWebEngineView()
        self.webview.load(QUrl("https://example.com"))
        self.webview.urlChanged.connect(lambda: events.callUrlChanged(self.webview.url().url()))
        self.setCentralWidget(self.webview)
        self.show()
        load_end = perf_counter()
        events.info["load_time"] = load_end-events.info["load_time"]
        events.callLoadEvent()
def main():
    events.info["load_time"] = perf_counter()
    for i in src.plug.plugs:
        f = importlib.import_module(i[1])
        events.plugs.update({i[0]: f})
    events.callPreLoad()
    app = QApplication(sys.argv)
    app.setApplicationName("Parader")
    window = Window()
    app.exec_()
if __name__ == "__main__":
    main()
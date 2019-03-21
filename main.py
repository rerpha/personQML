from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
from PySide2.QtQml import qmlRegisterType
from person import Person

VERSION_MAJOR = 1
VERSION_MINOR = 0

# Register our Person object as part of a module so it can be used in QML.
qmlRegisterType(Person, "MyModule", VERSION_MAJOR, VERSION_MINOR, "Person")

app = QApplication([])

view = QQuickView()
url = QUrl("view.qml")
view.setSource(url)
view.show()

app.exec_()

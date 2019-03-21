from PySide2.QtCore import QObject, Signal, Property


class Person(QObject):
    def __init__(self):
        super().__init__()
        self.current_mood = "Happy"

    notifier = Signal(str)

    def getMood(self):
        return self.current_mood

    def setMood(self, mood):
        self.current_mood = mood

    mood = Property(str, getMood, setMood, notify=notifier)

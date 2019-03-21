from PySide2.QtCore import QObject, Signal, Property


class Person(QObject):
    def __init__(self):
        super().__init__()
        self.current_mood = "Happy"

    def getMood(self):
        return self.current_mood

    def setMood(self, mood):
        if mood != self.current_mood:
            self.current_mood = mood
            self.moodChanged.emit()

    moodChanged = Signal()
    mood = Property(str, getMood, setMood, notify=moodChanged)

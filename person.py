from PySide2.QtCore import QObject, Signal, Property


class Person(QObject):
    def __init__(self):
        super().__init__()
        self.current_mood = "Happy"

    def getMood(self):
        return self.current_mood

    def setMood(self, mood):
        if mood != self.current_mood and mood != "":
            self.current_mood = mood
            # Call the notifying signal. We are not passing data here so don't need to emit anything in particular.
            self.moodChanged.emit()

    # Notifying signal - to be used in qml as "onMoodChanged"
    moodChanged = Signal()

    # Mood property to be accessed to and from QML and Python.
    mood = Property(str, getMood, setMood, notify=moodChanged)

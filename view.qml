import QtQuick 2.3
import MyModule 1.0
import QtQuick.Controls 2.0


Rectangle {
    id: page
    width: 300
    height: 300

    Person {
        id: person
        onMoodChanged: {
            // Set the text's "mood" property to Person's
            currentMood.mood = person.mood
        } // onMoodChanged
    } // Person

    Text {
        // Initially set to the person's default mood.
        // Note: this is a one-directional binding.
        // If this needed to be a two-directional binding,
        // we would use an alias instead of a var
        property var mood: person.mood
        id: currentMood
        anchors.top: parent.top
        text: "Current mood: " + mood
    } // Text

    Label {
        id:label
        anchors.bottom: parent.bottom
        text: "Mood \:"

        TextField {
            id: field
            focus: true
            anchors.bottom: parent.bottom
            anchors.left: parent.right

            Button {
                id: button
                text: "submit"
                anchors.bottom: parent.bottom
                anchors.left: field.right
                onClicked: {
                    person.mood=field.text
                } // onClicked
            } // Button
        } // TextField
    } // Label

} // Rectangle

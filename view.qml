import QtQuick 2.3
import MyModule 1.0
import QtQuick.Controls 2.0


Rectangle {
    id: page
    width: 300
    height: 300

    Person {
        id: person
        onMoodChanged:{
            currentMood.mood = person.mood
        }
    }

    Text {
        property alias mood: person.mood
        id: currentMood
        anchors.top: parent.top
        text: "Current mood: " + mood

    }

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
                anchors.bottom: parent.bottom
                anchors.left: field.right
                onClicked: {
                    person.mood=field.text
                }
            }

        }
    }

}


#!/usr/bin/python3

# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Close":
        app.stop()
    elif button == "Set Path":
        # Set dir to work
        app.directoryBox(title="Set Path", dirName=None)
        # Update file_path
    #else:
        # Call function fileTransfer()

# create a GUI variable called app
app = gui("PyPORG", "300x300")
app.setBg("lightgray")

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Python Picture Organizer")
app.setLabelBg("title", "lightgray")
app.setLabelFg("title", "black")

# Separator
app.addHorizontalSeparator(1,0,4, colour="lightblue")

# Add extension type chkboxes
app.addCheckBox(".jpg")
app.addCheckBox(".jpeg")
app.addCheckBox(".png")

app.setCheckBox(".jpg")

# Get the status of chkboxes
#app..getCheckBox(.jpg)...

# Add delete duplicate radio
app.addRadioButton("no_duplicate", "Save duplicate files")
app.addRadioButton("no_duplicate", "Delete duplicate files")

# Get the status of radiobtn
#app..getRadioButton(no_duplicate)

# Log
app.setFont(12)
app.addMessage("mess", """Ready.""")

# Meter
app.addMeter("progress")
app.setMeterFill("progress", "blue")

# link the buttons to the function called press
app.addButtons(["Start", "Set Path", "Close"], press)


# start the GUI
app.go()
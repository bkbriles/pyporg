#!/usr/bin/python3

# from tkinter import *

# # Create window obj
# window = Tk()
# frame = Frame(window, width = 300, height = 250)

# chk_no_duplicate = Checkbutton(window, text = "Delete duplicates")
# chk_type_jpg = Checkbutton(window, text = ".jpg")
# chk_type_jpeg = Checkbutton(window, text = ".jpeg")
# chk_type_png = Checkbutton(window, text = ".png")
# chk_type_img = Checkbutton(window, text = ".img") 
# btn_start = Button(text = "Start", fg = "BLACK")
# btn_close = Button(text = "Close", fg = "BLACK")

# chk_type_jpeg.grid(row = 0, column = 0)
# chk_type_jpg.grid(row = 0, column = 1)
# chk_type_png.grid(row = 1, column = 0)
# chk_type_img.grid(row = 1, column = 1)
# chk_no_duplicate.grid(columnspan = 2)
# btn_start.grid(row = 5, column = 0)
# btn_close.grid(row = 5, column = 1)

# window.mainloop()

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
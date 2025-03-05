# All the code needed to define interface components

# widgets are all sorts of interface components
from PyQt5 import QtWidgets as qtw

# the vertical hello box is a box with a text box and a button
# Defining just a generic box

class WindowWithVerticalSlots(qtw.QWidget):
    '''
    A window with a title and an empty vertical container 

    Intended use of this class is to 
    inherit and extend.
    
    This is now an object you would directly use
    '''
    def __init__(self, title: str):
        super().__init__()

        # Set the window title
        self.setWindowTitle(title)

        # Create an empty vertical layout container
        self.my_layout = qtw.QVBoxLayout(self)
        return
    

class InputPopup(qtw.QDialog):
    '''
    A popup window with a textbox and an OK button
    to allow the user to enter freeform text.
    '''

    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)

        # place to enter some text
        self.text_entry = qtw.QLineEdit(self)

        # OK button to click
        self.ok_button = qtw.QPushButton('Ok', self)

        # When the button is clicked, it calls the accept() method
        # of the QDialog which lets the application know that 
        # the interaction with the dialog is complete.
        self.ok_button.clicked.connect(self.accept) # accept is a function that came with QDialog

        # Create a vertical layout and add the widgets
        self.my_layout = qtw.QVBoxLayout(self)
        self.my_layout.addWidget(self.text_entry)
        self.my_layout.addWidget(self.ok_button)
        return
    
    def get_text(self):
        return self.text_entry.text()
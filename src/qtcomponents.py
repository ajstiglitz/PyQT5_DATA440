# All the code needed to define interface components

# widgets are all sorts of interface components
from PyQt5 import QtWidgets as qtw
import sys

# Your application will ocntain exactly one instance
# of a QApplication object (or derived subclass)
class SayHelloApp(qtw.QApplication):

    '''
    Contains a VerticalHelloBox to 
    prompt the user for their name and 
    say hello!
    '''


    def __init__(self):
        # Call the constuctor for the parent class
        # The one required argument is usually sys.argv
        # which are command line parameters. We don't need
        # any now so hence the empty list we pass
        super().__init__([])

        # Add the vertical hello box
        self.main_widget = VerticalHelloBox() # type: ignore

        # Run the application
        self.main_widget.show()
        sys.exit(self.exec_())
        return


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
    
    class VerticalHelloBox(WindowWithVerticalSlots): # type: ignore
        '''
        Contains a text box and a button that the user can press
        which opens up another windo for them to enter
        their name.
        '''
        def __init__(self):
            super().__init__(title ='Example Interface using PyQT5')
            self.configure()
            return
        
        # returning none and type hinting as none to be as explicit as possible
        def configure(self) -> None:
            self.greeting_box = qtw.QLabel(self)
            self.hello_button = qtw.QPushButton('Who are you?', self)

            # Bind the button to a function so that when the button is pressed
            # the function is called
            self.hello_button.clicked.connect(self.hello_button_clicked)

            # Add the two objects to the layout
            self.my_layout.addWidget(self.greeting_box)
            self.my_layout.addWidget(self.hello_button)
            return None
        
        def hello_button_clicked(self) -> None:
            # Create a new InputPopup
            name_getter = InputPopup('Your name: ')

            # run the dialog box and wait for the user to click the button
            if name_getter.exec_() == qtw.QDialog.accepted:
                # Set the text in the main window to whatever the user input
                self.greeting_box.setText(f'Hello{name_getter.get_text()}')
            return None

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
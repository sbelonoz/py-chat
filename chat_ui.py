from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChatUI():
    """This class encapsulates out application"""

    def __init__(self):

        # Counter of number of clicks
        self.button_clicks = 0

        initial_history = """Welcome to hackchat
Batman: hi
You: Hi
Batman: Crime"""

        # Create a GUI application
        app = QApplication([])

        # Style app
        app.setStyle('Windows')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.red)
        app.setPalette(palette)

        # Create our root window
        window = QWidget()

        # Create a vertical layout and embed it in the root window
        layout = QVBoxLayout()
        window.setLayout(layout)


        # Creeate a text display
        lbl_message = QLabel('Type your message')

        # Make it visible
        lbl_message.show()

        # txt_ is a multi line text box
        # imp_ is an input box
        # btn_ is a button
        # lbl_ is a label

        txt_history = QTextEdit()
        txt_history.setPlainText(initial_history)
        txt_history.setReadOnly(True)

        # Create an input box
        inp_message = QLineEdit()

        inp_message.returnPressed.connect(self.send)

        # Create a button
        # button = QPushButton('Send')
        # button.clicked.connect(self.button_clicked)

        # Add widgets to the layout
        layout.addWidget(txt_history)
        layout.addWidget(lbl_message)
        layout.addWidget(inp_message)
    #   layout.addWidget(button)

        window.show()

        self.app = app
        self.window = window
        self.layout = layout
        self.inp_message = inp_message
        self.txt_history = txt_history
    #   self.button = button

    def button_clicked(self):
        self.button_clicks += 1
        self.label.setText("Button was clicked " + str(self.button_clicks) + " times")

    def run(self):
        self.app.exec_()

    def send(self):
        user_typed = self.inp_message
        display = 'You: ' + user_typed.text()
        self.txt_history.append(display)
        self.inp_message.setText('')
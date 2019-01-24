from PyQt5.QtWidgets import *

class ChatUI():
    """This class encapsulates out application"""

    def __init__(self):

        # Counter of number of clicks
        self.button_clicks = 0

        # Create a GUI application
        app = QApplication([])

        # Create our root window
        window = QWidget()

        # Create a vertical layout and embed it in the root window
        layout = QVBoxLayout()
        window.setLayout(layout)


        # Creeate a text display
        label = QLabel('Hello, Cyber')

        # Make it visible
        label.show()

        # Create a button
        button = QPushButton('Click me')

        button.clicked.connect(self.button_clicked)

        # Add widgets to the layout
        layout.addWidget(label)
        layout.addWidget(button)

        window.show()

        self.app = app
        self.window = window
        self.layout = layout
        self.label = label
        self.button = button

    def button_clicked(self):
        self.button_clicks += 1
        self.label.setText("Button was clicked " + str(self.button_clicks) + " times")

    def run(self):
        self.app.exec_()
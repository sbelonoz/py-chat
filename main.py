#!/usr/bin/python3

from PyQt5.QtWidgets import *

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

# Add widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.show()

app.exec_()
#!/usr/bin/python3

from PyQt5.QtWidgets import *

# Counter of number of clicks
button_clicks = 0

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

def on_button_clicked():
    global button_clicks
    button_clicks += 1

    label.setText("Button was clicked " + str(button_clicks) + " times")

button.clicked.connect(on_button_clicked)

# Add widgets to the layout
layout.addWidget(label)
layout.addWidget(button)

window.show()

app.exec_()
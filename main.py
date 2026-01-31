# Install first: pip install nicegui

from nicegui import ui

# Title
ui.label('Hello! Welcome to NiceGUI!')

# Button
def clicked():
    ui.notify('You clicked the button!')

ui.button('Click Me', on_click=clicked)

# Input box
def submit_name():
    ui.notify(f'Hello, {name_input.value}!')

name_input = ui.input('Your Name')
ui.button('Say Hello', on_click=submit_name)

# Run app
ui.run(title='My NiceGUI App', port=8080)

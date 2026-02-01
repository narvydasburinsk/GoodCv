from nicegui import ui, Button, Text
from Imports.UI_visible import Column, Row
# from Imports.Utils import *

def AppStart():
    Column(
        Row(
            Text("Title"),
            Button("Notify", code="ui.notify('Hello world!')")  # works
        ),
        Row(
            Text("Hi everybody this is my web cv, i made this entirely out of python. I know it may seem dumb. But i like it. I hope you to.")
        )
    )
    ui.label("App is starting...")
    ui.button("Click me", on_click=lambda: ui.notify("Hello!"))

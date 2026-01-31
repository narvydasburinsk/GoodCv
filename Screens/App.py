from nicegui import *
from Imports.UI_visible import *
from Imports.Utils import *

def AppStart():
    ui.label("App is starting...")
    ui.button("Click me", on_click=lambda: ui.notify("Hello!"))
    ui.run()

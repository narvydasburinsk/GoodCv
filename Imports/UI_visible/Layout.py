from nicegui import ui

# Row helper: horizontal center by default
def Row(*elements):
    with ui.row(justify='center'):   # center horizontally
        for el in elements:
            el()  # call the element function

# Column helper: vertical center by default
def Column(*elements):
    with ui.column(align='center'):  # center vertically
        for el in elements:
            el()  # call the element function


def Text(content: str, size: int = 16, weight: str = 'normal', color: str = 'black'):
    """
    Creates a text label.
    
    :param content: string, the text to show
    :param size: int, font size in px
    :param weight: 'normal', 'bold', etc.
    :param color: text color
    """
    ui.label(content).style(f'font-size: {size}px; font-weight: {weight}; color: {color}')

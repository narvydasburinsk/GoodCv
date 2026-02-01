from nicegui import ui

# Button that executes string safely
def Button(text: str, code: str = None):
    def run_code():
        if code:
            try:
                exec(code)
            except Exception as e:
                ui.notify(f"Error: {e}")  # show error instead of crashing
        else:
            ui.notify(f"You clicked {text}!")  # default
    
    ui.button(
        text,
        on_click=run_code,
        style="""
            color: #FFFFFF;
            background-color: rgba(255,165,0,0.2);
            border-radius: 12px;
            border: 1px solid #888888;
            padding: 8px 16px;
            font-size: 16px;
        """
    )


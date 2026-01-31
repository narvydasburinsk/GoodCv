
def Button(text: str, on_click=None):
    """Create a styled button with white text, 20% faded background, smooth edges."""
    ui.button(
        text,
        on_click=on_click or (lambda: ui.notify(f"You clicked {text}!")),
        style="""
            color: #FFFFFF;                 /* white text */
            background-color: rgba(255,165,0,0.2); /* orange faded 20% */
            border-radius: 12px;            /* smooth edges */
            border: 1px solid #888888;      /* subtle gray border */
            padding: 8px 16px;
            font-size: 16px;
        """
    )

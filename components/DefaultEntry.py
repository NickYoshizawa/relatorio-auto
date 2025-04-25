import customtkinter as ctk
from config.theme import (
    ENTRY_WIDTH,
    ENTRY_HEIGHT,
    ENTRY_FONT,
    ENTRY_TEXT_COLOR,
    ENTRY_BG_COLOR,
    ENTRY_BORDER_COLOR,
    ENTRY_BORDER_WIDTH,
    ENTRY_CORNER_RADIUS
)

class DefaultEntry(ctk.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(
            master=master,
            width=ENTRY_WIDTH,
            height=ENTRY_HEIGHT,
            font=ENTRY_FONT,
            text_color=ENTRY_TEXT_COLOR,
            fg_color=ENTRY_BG_COLOR,
            border_color=ENTRY_BORDER_COLOR,
            border_width=ENTRY_BORDER_WIDTH,
            corner_radius=ENTRY_CORNER_RADIUS,
            **kwargs
        )
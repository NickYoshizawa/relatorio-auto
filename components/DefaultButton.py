import customtkinter as ctk
from config.theme import (
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_CORNER_RADIUS,
    BUTTON_BORDER_WIDTH,
    BUTTON_PRIMARY_COLOR,
    BUTTON_PRIMARY_HOVER,
    BUTTON_PRIMARY_TEXT_COLOR,
    BUTTON_FONT
)

class DefaultButton(ctk.CTkButton):
    def __init__(self, 
            master=None,
            text="", 
            command=None,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            border_width=BUTTON_BORDER_WIDTH,
            fg_color=BUTTON_PRIMARY_COLOR,
            hover_color=BUTTON_PRIMARY_HOVER,
            text_color=BUTTON_PRIMARY_TEXT_COLOR,
            font=BUTTON_FONT,
            **kwargs
        ):
        super().__init__(
            master=master,
            text=text,
            command=command,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            font=font,
            **kwargs
        )
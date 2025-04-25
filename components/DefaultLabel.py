import customtkinter as ctk
from config.theme import (
    LABEL_TEXT_FONT,
    LABEL_TEXT_COLOR
)

class DefaultLabel(ctk.CTkLabel):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(
            master=master,
            text=text,
            font=LABEL_TEXT_FONT,
            text_color=LABEL_TEXT_COLOR,
            **kwargs
        )
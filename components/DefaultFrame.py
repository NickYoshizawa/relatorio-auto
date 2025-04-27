import customtkinter as ctk
from config.theme import (
    FRAME_WIDTH,
    FRAME_HEIGHT,
    FRAME_CORNER_RADIUS,
    FRAME_BORDER_WIDTH,
    FRAME_BG_COLOR,
    FRAME_BORDER_COLOR
)

class DefaultFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(
            master=master,
            width=FRAME_WIDTH,
            height=FRAME_HEIGHT,
            corner_radius=FRAME_CORNER_RADIUS,
            border_width=FRAME_BORDER_WIDTH,
            fg_color=FRAME_BG_COLOR,
            border_color=FRAME_BORDER_COLOR,
            **kwargs
        )

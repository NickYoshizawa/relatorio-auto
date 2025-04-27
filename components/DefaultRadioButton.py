import customtkinter as ctk
from config.theme import (
    RADIOBUTTON_WIDTH,
    RADIOBUTTON_HEIGHT,
    RADIOBUTTON_FONT,
    RADIOBUTTON_TEXT_COLOR,
    RADIOBUTTON_SELECTED_COLOR,
    RADIOBUTTON_HOVER_COLOR,
    RADIOBUTTON_BORDER_COLOR,
    RADIOBUTTON_BORDER_WIDTH,
    RADIOBUTTON_CORNER_RADIUS
)

class DefaultRadioButton(ctk.CTkRadioButton):
    def __init__(self, 
        master, 
        width=100,
        height=22, 
        radiobutton_width = RADIOBUTTON_WIDTH, 
        radiobutton_height = RADIOBUTTON_HEIGHT, 
        corner_radius=RADIOBUTTON_CORNER_RADIUS,
        border_width_unchecked = RADIOBUTTON_BORDER_WIDTH,
        border_width_checked = RADIOBUTTON_BORDER_WIDTH,
        bg_color = "transparent", 
        fg_color=RADIOBUTTON_SELECTED_COLOR,
        hover_color=RADIOBUTTON_HOVER_COLOR,
        border_color=RADIOBUTTON_BORDER_COLOR,
        text_color=RADIOBUTTON_TEXT_COLOR,
        text_color_disabled = None, 
        text = "CTkRadioButton", 
        font=RADIOBUTTON_FONT, 
        textvariable = None, 
        variable = None, 
        value = 0, 
        state = 'normal',
        hover = True, 
        command = None, 
        **kwargs
    ):
        
        super().__init__(master, width, height, radiobutton_width, radiobutton_height, corner_radius, border_width_unchecked, border_width_checked, bg_color, fg_color, hover_color, border_color, text_color, text_color_disabled, text, font, textvariable, variable, value, state, hover, command, **kwargs)

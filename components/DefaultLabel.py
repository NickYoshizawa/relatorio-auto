import customtkinter as ctk
from config.theme import (
    LABEL_TITLE_FONT,
    LABEL_SECTION_FONT,
    LABEL_SUBTITLE_FONT,


    LABEL_TEXT_FONT,


    LABEL_TEXT_COLOR,
    LABEL_TEXT_MUTED_COLOR,
    LABEL_TITLE_COLOR,
    LABEL_SECTION_COLOR,
    LABEL_ERROR_COLOR,
    LABEL_SUCCESS_COLOR,
)

class DefaultLabel(ctk.CTkLabel):
    def __init__(self, 
        master, 
        width = 0, 
        height = 28, 
        corner_radius = None, 
        bg_color = "transparent", 
        fg_color = None, 
        text_color=LABEL_TEXT_COLOR, 
        text_color_disabled = LABEL_TEXT_MUTED_COLOR, 
        text = "Default Text", 
        font=LABEL_TEXT_FONT, 
        image = None, 
        compound = "center", 
        anchor = "center", 
        wraplength = 0,
        font_type: str = None,
        text_type: str = None,
        **kwargs
    ):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)
    
        if font_type == "title":
            self.configure(font=LABEL_TITLE_FONT)
        if font_type == "section":
            self.configure(font=LABEL_SECTION_FONT)
        if font_type == "subtitle":
            self.configure(font=LABEL_SUBTITLE_FONT)
            
        if text_type == "title":
            self.configure(text_color=LABEL_TITLE_COLOR)
        if text_type == "section":
            self.configure(text_color=LABEL_SECTION_COLOR)
        if text_type == "error":
            self.configure(text_color=LABEL_ERROR_COLOR)
        if text_type == "sucess":
            self.configure(text_color=LABEL_SUCCESS_COLOR)

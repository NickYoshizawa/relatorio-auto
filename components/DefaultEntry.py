import customtkinter as ctk
from config.theme import (
    ENTRY_WIDTH,
    ENTRY_HEIGHT,
    ENTRY_FONT,
    ENTRY_TEXT_COLOR,
    ENTRY_BG_COLOR,
    ENTRY_BORDER_COLOR,
    ENTRY_BORDER_WIDTH,
    ENTRY_CORNER_RADIUS,
    ENTRY_PLACEHOLDER_COLOR,
    ENTRY_FOCUS_BORDER_COLOR
)

class DefaultEntry(ctk.CTkEntry):
    def __init__(self, 
            master, 
            width=ENTRY_WIDTH,
            height=ENTRY_HEIGHT,
            corner_radius=ENTRY_CORNER_RADIUS,
            border_width=ENTRY_BORDER_WIDTH,
            bg_color = "transparent", 
            fg_color=ENTRY_BG_COLOR, 
            border_color=ENTRY_BORDER_COLOR, 
            text_color=ENTRY_TEXT_COLOR, 
            placeholder_text_color = ENTRY_PLACEHOLDER_COLOR, 
            textvariable = None, 
            placeholder_text = None, 
            font=ENTRY_FONT,
            state = 'normal',
            **kwargs
        ):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, text_color, placeholder_text_color, textvariable, placeholder_text, font, state, **kwargs)
        
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event=None):
        self.configure(border_color=ENTRY_FOCUS_BORDER_COLOR)

    def on_focus_out(self, event=None):
        self.configure(border_color=ENTRY_BORDER_COLOR)
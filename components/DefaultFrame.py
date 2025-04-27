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
    
    def __init__(self, 
        master, 
        width = FRAME_WIDTH, 
        height = FRAME_HEIGHT, 
        corner_radius = FRAME_CORNER_RADIUS, 
        border_width = FRAME_BORDER_WIDTH, 
        bg_color = "transparent", 
        fg_color = FRAME_BG_COLOR, 
        border_color = FRAME_BORDER_COLOR, 
        background_corner_colors = None, 
        overwrite_preferred_drawing_method = None, 
        **kwargs
    ):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    
    def configure(self, require_redraw=False, **kwargs):
        return super().configure(require_redraw, **kwargs)

    
    

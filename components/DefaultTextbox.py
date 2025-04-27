import customtkinter as ctk
from config.theme import (
    TEXTBOX_WIDTH,
    TEXTBOX_HEIGHT,
    TEXTBOX_FONT,
    TEXTBOX_TEXT_COLOR,
    TEXTBOX_BG_COLOR,
    TEXTBOX_BORDER_COLOR,
    TEXTBOX_BORDER_WIDTH,
    TEXTBOX_CORNER_RADIUS,
    TEXTBOX_VARIAVEL_TAG_COLOR,
    TEXTBOX_FOCUS_BORDER_COLOR,
    SCROLLBAR_BUTTON_COLOR,     
    SCROLLBAR_BUTTON_HOVER_COLOR
)

class DefaultTextbox(ctk.CTkTextbox):
    def __init__(self, 
        master, 
        width=TEXTBOX_WIDTH,
        height=TEXTBOX_HEIGHT, 
        corner_radius=TEXTBOX_CORNER_RADIUS,
        border_width=TEXTBOX_BORDER_WIDTH, 
        border_spacing = 3, 
        bg_color = "transparent", 
        fg_color=TEXTBOX_BG_COLOR,
        border_color=TEXTBOX_BORDER_COLOR,
        text_color=TEXTBOX_TEXT_COLOR,
        scrollbar_button_color = SCROLLBAR_BUTTON_COLOR, 
        scrollbar_button_hover_color = SCROLLBAR_BUTTON_HOVER_COLOR, 
        font=TEXTBOX_FONT,
        activate_scrollbars = True, 
        **kwargs
    ):
        
        super().__init__(master, width, height, corner_radius, border_width, border_spacing, bg_color, fg_color, border_color, text_color, scrollbar_button_color, scrollbar_button_hover_color, font, activate_scrollbars, **kwargs)

        self._textbox.tag_configure("highlight", foreground=TEXTBOX_VARIAVEL_TAG_COLOR)

        self.bind("<KeyRelease>", self.highlight_text)
        
        if self._textbox.cget("state") != "disabled":
            self.bind("<FocusIn>", self.on_focus_in)
            self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event=None):
        self.configure(border_color=TEXTBOX_FOCUS_BORDER_COLOR)

    def on_focus_out(self, event=None):
        self.configure(border_color=TEXTBOX_BORDER_COLOR)
        
    def highlight_text(self, event=None):
        content = self.get("1.0", "end-1c")
        self.tag_remove("highlight", "1.0", "end")

        start = 0
        while True:
            start = content.find('[', start)
            end = content.find(']', start)

            if start == -1 or end == -1:
                break

            
            start_index = self.index(f"1.0+{start}c")
            end_index = self.index(f"1.0+{end+1}c")

            
            self.tag_add("highlight", start_index, end_index)

            start = end + 1  

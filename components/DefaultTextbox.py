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
    TEXTBOX_VARIAVEL_TAG_COLOR
)

class DefaultTextbox(ctk.CTkTextbox):
    def __init__(self, master=None, **kwargs):
        super().__init__(
            master=master,
            width=TEXTBOX_WIDTH,
            height=TEXTBOX_HEIGHT,
            font=TEXTBOX_FONT,
            text_color=TEXTBOX_TEXT_COLOR,
            fg_color=TEXTBOX_BG_COLOR,
            border_color=TEXTBOX_BORDER_COLOR,
            border_width=TEXTBOX_BORDER_WIDTH,
            corner_radius=TEXTBOX_CORNER_RADIUS,
            **kwargs
        )
        self._textbox.tag_configure("highlight", foreground=TEXTBOX_VARIAVEL_TAG_COLOR)

        self.bind("<KeyRelease>", self.highlight_text)
        
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

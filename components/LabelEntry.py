import customtkinter as ctk
from components.DefaultEntry import DefaultEntry
from components.DefaultLabel import DefaultLabel



class LabelEntry(ctk.CTkFrame):
    def __init__(self,
        master,
        label_text="Text",
        show=None,
        corner_radius=10,
        border_width=0,
        bg_color="transparent",
        fg_color="transparent",
        placeholder_text=None,
        border_color=None,
        background_corner_colors=None,
        overwrite_preferred_drawing_method=None,
        **kwargs
    ):

        super().__init__(master,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            background_corner_colors=background_corner_colors,
            overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
            **kwargs
        )


        self.label = DefaultLabel(self, text=label_text)
        self.label.pack(anchor='w', padx=(5, 0), pady=(5, 0))

        self.entry = DefaultEntry(self, show=show, placeholder_text=placeholder_text)
        self.entry.pack(expand=True, fill="x", padx=5, pady=(0, 5))
        
    def insert(self, index: any, string: any):
        self.entry.insert(index, string)
    
    def get(self) -> str:
        return self.entry.get()
        
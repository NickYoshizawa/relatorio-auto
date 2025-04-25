from typing import Any
from components.DefaultLabel import DefaultLabel
from components.DefaultTextbox import DefaultTextbox
from customtkinter import *

class LabelTextbox(CTkFrame):
    def __init__(self, 
        master: Any, 
        text: str = 'Text Label',
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.label = DefaultLabel(self, text=text)
        self.textbox = DefaultTextbox(self)
        
        self.label.pack(anchor='w', padx=10)
        self.textbox.pack(expand=True, fill=BOTH)
    
    def get(self, index1, index2):
        return self.textbox.get(index1, index2)
    
    def insert(self, index, text):
        self.textbox.insert(index, text)
        
    def delete(self, start, end):
        self.textbox.delete(start, end)
        
    def highlight_text(self):
        self.textbox.highlight_text()
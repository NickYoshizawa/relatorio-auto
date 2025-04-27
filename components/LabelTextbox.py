from typing import Any
from components.DefaultLabel import DefaultLabel
from components.DefaultTextbox import DefaultTextbox
from components.DefaultFrame import DefaultFrame

class LabelTextbox(DefaultFrame):
    def __init__(self, 
        master: Any, 
        text: str = 'Text Label',
        state: str = 'normal',
        font_type: str = None,
        text_type: str = None,
        **kwargs
    ):
        super().__init__(master, **kwargs)

        self.label = DefaultLabel(self, text=text, font_type=font_type, text_type=text_type)
        self.textbox = DefaultTextbox(self, state=state)
        
        self.label.pack(anchor='w', padx=10, pady=(2, 0))
        self.textbox.pack(expand=True, fill='both')
    
    def get(self, index1, index2):
        return self.textbox.get(index1, index2)
    
    def insert(self, index, text):
        self.textbox.insert(index, text)
        
    def delete(self, start, end):
        self.textbox.delete(start, end)
        
    def highlight_text(self):
        self.textbox.highlight_text()
        
    def configure(self, require_redraw=False, **kwargs):
        return self.textbox.configure(require_redraw, **kwargs)
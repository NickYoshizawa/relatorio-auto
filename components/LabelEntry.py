from components.DefaultEntry import DefaultEntry
from components.DefaultLabel import DefaultLabel
from components.DefaultFrame import DefaultFrame



class LabelEntry(DefaultFrame):
    def __init__(self,
        master,
        label_text="Text",
        show=None,
        placeholder_text=None,
        font_type: str = None,
        text_type: str = None,
        **kwargs
    ):

        super().__init__(master, **kwargs)


        self.label = DefaultLabel(self, text=label_text, font_type=font_type, text_type=text_type)
        self.label.pack(anchor='w')

        self.entry = DefaultEntry(self, show=show, placeholder_text=placeholder_text)
        self.entry.pack(expand=True, fill="x")
        
    def insert(self, index: any, string: any):
        self.entry.insert(index, string)
    
    def get(self) -> str:
        return self.entry.get()
        
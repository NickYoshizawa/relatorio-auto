from components.DefaultEntry import DefaultEntry
from components.DefaultLabel import DefaultLabel
from components.DefaultFrame import DefaultFrame



class LabelEntry(DefaultFrame):
    def __init__(self,
        master,
        label_text="Text",
        show=None,
        placeholder_text=None,
        **kwargs
    ):

        super().__init__(master, **kwargs)


        self.label = DefaultLabel(self, text=label_text)
        self.label.pack(anchor='w', padx=(5, 0), pady=(5, 0))

        self.entry = DefaultEntry(self, show=show, placeholder_text=placeholder_text)
        self.entry.pack(expand=True, fill="x", padx=5, pady=(0, 5))
        
    def insert(self, index: any, string: any):
        self.entry.insert(index, string)
    
    def get(self) -> str:
        return self.entry.get()
        
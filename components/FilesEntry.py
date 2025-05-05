from typing import Any, Iterable
from tkinter import filedialog

from components.DefaultFrame import DefaultFrame
from components.DefaultLabel import DefaultLabel
from components.DefaultButton import DefaultButton

from config.theme import (
    BUTTON_WIDTH,
    BUTTON_HEIGHT
)

class FilesEntry(DefaultFrame):
    def __init__(self, 
        master: Any, 
        wrap_lenth: int = 690,
        height: int = None,
        button_height: int = BUTTON_HEIGHT,
        button_width: int = BUTTON_WIDTH,
        label_text: str = "Escolha um arquivo",
        button_text: str = "Browse",
        filetypes: Iterable[tuple[str, str | list[str] | tuple[str, ...]]] | None = [("Todos os arquivos", "*.*")],
        **kwargs
    ):
        
        
        super().__init__(master, **kwargs)
        
        if height:
            self.pack_propagate(False)
            self.configure(height=height)
        
        self.label_text = label_text
        self.filetypes = filetypes
    
        self.label = DefaultLabel(self, text=self.label_text, wraplength=wrap_lenth)
        self.button= DefaultButton(self, text=button_text, command=self.__browsefile, height=button_height, width=button_width)
        
        self.label.pack(side="left", padx=10, pady=10, fill="both")
        self.button.pack(side="right", padx=10, pady=10)
        
        self.filepath = []
    
    def __browsefile(self):
        self.filepath = filedialog.askopenfilename(filetypes=self.filetypes)
        if self.filepath:
            self.label.configure(text=self.filepath)
        else:
            self.label.configure(text=self.label_text)
        
    def insert(self, string):
        self.label.configure(text=string)
    
    def get(self):
        file = self.label.cget("text")
        if file == '' or file == self.label_text:
            return ''
        else:
            return file
    
    def insert_file(self, file: str):
        self.label.configure(text=file)
from typing import Any, Tuple
import customtkinter as ctk
from tkinter import filedialog


class FileEntry(ctk.CTkFrame):
    def __init__(self, master: Any, wrap_lenth: int = 690, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = 1, bg_color: str | Tuple[str] = "transparent", fg_color: str | Tuple[str] | None = None, border_color: str | Tuple[str] | None = 'white', background_corner_colors: Tuple[str | Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        
    
        self.label = CTkLabel(self, text="Selecione um Arquivo Excel", wraplength=wrap_lenth)
        self.button= CTkButton(self, text='Browse', command=self.__browsefile, height=40, width=100)
        
        self.label.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.BOTH)
        self.button.pack(side=ctk.RIGHT, padx=10, pady=10)
        
        self.filepath = []
    
    def __browsefile(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        if self.filepath:
            self.label.configure(text=self.filepath)
        else:
            self.label.configure(text='Selecione um Arquivo Excel')
        
    def insert(self, string):
        self.label.configure(text=string)
    
    def get(self):
        file = self.label.cget("text")
        if file == '' or file == "Selecione um Arquivo Excel":
            return ''
        else:
            return file
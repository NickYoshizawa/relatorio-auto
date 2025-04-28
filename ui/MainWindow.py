import os
import customtkinter as ctk
import json

from threading import Thread

from utils.layout import *
from utils.jsonUtils import update_json

from components.DefaultButton import DefaultButton
from components.LabelTextbox import LabelTextbox
from components.LabelEntry import LabelEntry
from components.FilesEntry import FilesEntry
from components.DefaultFrame import DefaultFrame
from components.DefaultRadioButton import DefaultRadioButton

from models.DataFrame import DataFrame

from config.theme import WINDOW_ICON, EXCEL_FILETYPES

class MainWindow(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.file_type_option = ctk.StringVar(value="sheets") 
        self.field_type_option = ctk.StringVar(value="row") 
        
        if os.path.exists('data/token.json'):
            os.remove('data/token.json')
            
        ctk.set_appearance_mode('dark-blue')
        self.geometry('800x550')
        self.minsize(800, 550)
        self.iconbitmap(WINDOW_ICON)
        self.title('Integração GoogleSheets')
        
        self.file_radio_frame = DefaultFrame(self, border_width=0)
        self.entrys_frame = DefaultFrame(self, border_width=0)
        self.textboxs_frame = DefaultFrame(self, border_width=0)
        self.field_type_radio_frame = DefaultFrame(self, border_width=0)
        
        
        self.sheets_radio_entry = DefaultRadioButton(self.file_radio_frame, text="Planilha Google Sheets", value="sheets", variable=self.file_type_option)
        self.excel_radio_entry = DefaultRadioButton(self.file_radio_frame, text="Arquivo Excel", value="excel", variable=self.file_type_option)
        self.excel_radio_entry.bind("<Button-1>", self.radio_callback)
        self.sheets_radio_entry.bind("<Button-1>", self.radio_callback)
        
        self.excel_entry = FilesEntry(self.entrys_frame, filetypes=EXCEL_FILETYPES, height=63, wrap_lenth=400)
        self.sheets_entry = LabelEntry(self.entrys_frame, label_text='Link da planilha (.CSV):', border_width=0)
        
        self.field_entry = LabelEntry(self.entrys_frame, label_text="Campo:",border_width=0)
        
        self.row_radio_entry = DefaultRadioButton(self.field_type_radio_frame, text="Buscar por linha", value="row", variable=self.field_type_option)
        self.column_radio_entry = DefaultRadioButton(self.field_type_radio_frame, text="Buscar por coluna", value="column", variable=self.field_type_option)
        
        self.input_textbox = LabelTextbox(self.textboxs_frame, text='Input:', fg_color='transparent')
        self.output_textbox = LabelTextbox(self.textboxs_frame, text='Output:', fg_color='transparent', state='disabled')
        
        
        
        self.submit_button = DefaultButton(self, text='Submit', command=self.start_thread)
        
        
        
        try:
            with open('data/msg.txt', 'r', encoding="utf-8") as file:
                self.input_textbox.insert(1.0, file.read())
                self.input_textbox.highlight_text()
            with open('data/inputs.json', 'r', encoding="utf-8") as file:
                json_data = json.loads(file.read())
                
                if json_data[0]['file'] != '' and json_data[0]['file_type'] != '' and json_data[0]['field'] != '' and json_data[0]['axis'] != '':
                    if json_data[0]['file_type'] == "sheets":
                        self.sheets_entry.insert(0, json_data[0]['file'])
                    else:
                        self.excel_entry.insert_file(json_data[0]['file'])
                    self.file_type_option.set(json_data[0]['file_type'])
                    self.field_entry.insert(0, json_data[0]['field'])
                    self.field_type_option.set(json_data[0]['axis'])
        except Exception as e:
            print(e)
        finally:
            self.after(100, self.radio_callback)
    
        self.file_radio_frame.pack(fill='x', pady=(20, 10))
        self.entrys_frame.pack(fill='x')
        self.field_type_radio_frame.pack(fill='x', pady=10)
        self.textboxs_frame.pack(fill='both', expand=True, pady=(10, 0))
        
        
        self.sheets_radio_entry.pack(anchor="w", side="left", padx=(100, 20))
        self.excel_radio_entry.pack(anchor="w")
        
        self.field_entry.pack(expand=True, fill='x', padx=100)
        
        self.row_radio_entry.pack(anchor="w", side="left", padx=(100, 20))
        self.column_radio_entry.pack(anchor="w")
        
        self.input_textbox.pack(expand=True, fill='both', side='left', padx=20)
        self.output_textbox.pack(expand=True, fill='both', side='right', padx=(0,20))
        
        self.submit_button.pack(pady=30)
    
    def radio_callback(self, event=None):
        if self.file_type_option.get() == "sheets":
            self.excel_entry.pack_forget()
            self.sheets_entry.pack(expand=True, fill='x', padx=100 ,before=self.field_entry)
        else:
            self.sheets_entry.pack_forget()
            self.excel_entry.pack(expand=True, fill='x', padx=100, before=self.field_entry)
            
        
    def submit(self):
        
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="disabled")
        
        open('data/msg.txt', 'w').close()
        open('data/inputs.json', 'w').close()
        
        file_type = self.file_type_option.get()
        
        if file_type == "sheets":
            file = self.sheets_entry.get()
        else:
            file = self.excel_entry.get()
        
        field = self.field_entry.get()
        axis = self.field_type_option.get()
        msg = self.input_textbox.get(1.0, "end-1c")
        
        x = 0
        
        for widget in self.entrys_frame.winfo_children():
            if widget.get() == "" and widget.winfo_ismapped():
                widget.configure(border_color = 'red')
                x+=1
        if x > 0:
            return
        
        df = DataFrame(file, file_type)
        
        data = {
            'file': file,
            'file_type': file_type,
            'field': field,
            'axis': axis
        }
        
        with open('data/msg.txt', 'a', encoding="utf-8") as file:
            file.write(msg)
            
        update_json('data/inputs.json', data, 2, False)
        
        self.output_textbox.configure(state="normal")
        self.output_textbox.insert(1.0, df.format_text(msg, field, axis))
        self.output_textbox.configure(state="disabled")
        
    
    def start_thread(self):
        thread = Thread(target=self.submit)
        thread.start()
        
    def run(self):
        self.mainloop()

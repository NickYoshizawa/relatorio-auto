from customtkinter import *
import json
import datetime

from utils.layout import *
from utils.jsonUtils import update_json

from components.DefaultButton import DefaultButton
from components.DefaultEntry import DefaultEntry
from components.LabelTextbox import LabelTextbox
from components.LabelEntry import LabelEntry

from config.theme import WINDOW_ICON

class MainWindow(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if os.path.exists('data/token.json'):
            os.remove('data/token.json')
            
        set_appearance_mode('dark-blue')
        self.geometry('800x500')
        self.minsize(600, 550)
        self.iconbitmap(WINDOW_ICON)
        self.title('Integração GoogleSheets')
        
        self.entrys_frame = CTkFrame(self, fg_color='transparent')
        self.textboxs_frame = CTkFrame(self, fg_color='transparent')
        
        self.id_entry = LabelEntry(self.entrys_frame, label_text='Id da Planilha')
        self.range_entry = LabelEntry(self.entrys_frame, label_text='Intervalo da Planilha')
        self.date_entry = LabelEntry(self.entrys_frame, placeholder_text='ex: dd/mm/yyyy')
        
        self.input_textbox = LabelTextbox(self.textboxs_frame, text='Input:', fg_color='transparent')
        self.output_textbox = LabelTextbox(self.textboxs_frame, text='Output:', fg_color='transparent')
        
        self.submit_button = DefaultButton(self, text='Submit', command=self.__submit)
        
        self.date_entry.insert(0, datetime.date.today().strftime('%d/%m/%Y'))
        
        try:
            with open('data/msg.txt', 'r', encoding="utf-8") as file:
                self.input_textbox.insert(1.0, file.read())
                self.input_textbox.highlight_text()
            with open('data/inputs.json', 'r', encoding="utf-8") as file:
                json_data = json.loads(file.read())
                
                if json_data[0]['id'] != '' and json_data[0]['range'] != '':
                    self.id_entry.insert(0, json_data[0]['id'])
                    self.range_entry.insert(0, json_data[0]['range'])
                
        except:
            pass
    
        self.entrys_frame.pack(fill=X)
        self.textboxs_frame.pack(fill=BOTH, expand=True, pady=(20, 0))
        
        
        self.id_entry.pack(expand=True, fill=X, padx=100)
        self.range_entry.pack(expand=True, fill=X, padx=100)
        self.date_entry.pack(expand=True, fill=X, padx=100)
        
        self.input_textbox.pack(expand=True, fill=BOTH, side='left', padx=20)
        self.output_textbox.pack(expand=True, fill=BOTH, side='right', padx=(0,20))
        
        self.submit_button.pack(pady=30)
        
    def __submit(self):
        
        self.output_textbox.delete("1.0", "end")
        
        open('data/msg.txt', 'w').close()
        open('data/inputs.json', 'w').close()
        
        self.id = self.id_entry.get()
        self.range = self.range_entry.get()
        self.msg = self.input_textbox.get(1.0, "end-1c")
        self.date = self.date_entry.get()
        
        data = {
            'id': self.id,
            'range': self.range 
        }
        
        with open('data/msg.txt', 'a', encoding="utf-8") as file:
            file.write(self.msg)
            
        update_json('data/inputs.json', data, 2, False)
        
        self.output_textbox.insert(1.0, integracao(self.msg, self.id, self.range, self.date))
        
    def run(self):
        self.mainloop()

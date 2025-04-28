import pandas as pd

class DataFrame():
    def __init__(self, file: str, type: str) -> None:

        self.message = None

        try:
            if type == "excel":
                self.df = pd.read_excel(file)
            else:
                self.df = pd.read_csv(file)
        except Exception as e:
            self.message = f"""
Erro na importação da planilha!

{str(e)}
"""
    
    def convert_timeStamp(self, value):
        try:
            dt = pd.to_datetime(value)
            # Se conseguir, formata só como dia/mês/ano
            return dt.strftime("%d/%m/%Y")
        except (ValueError, TypeError):
            return value
            
    def format_text(self, text: str, field: str, axis: str,) -> str:
        if self.message:
            return self.message
        
        if axis == 'column':
            
            df = self.df.transpose()
            df.columns = df.iloc[0]
            df = df.drop(df.index[0])
            df.columns = df.columns.infer_objects()
            print(df.index)
            print(df.index.tolist())
            
            try:
                
                row = df.loc[field]
                row = row.to_dict()  
                
                for item in row.items():
                    text = text.replace('['+str(item[0])+']', str(item[1]))
        
            except KeyError:
                return f"Campo '{field}' não encontrada na planilha!"
            
        else:
            try:
                df = self.df
                first_column = df.columns[0]
                values = df[self.df[first_column] == field]

                for header in values:
                    text = text.replace('['+str(header)+']', str(values[header][0]))
            except KeyError:
                return f"Campo '{field}' não encontrada na planilha!"
            
        return text
        
import pandas as pd
import time

class DataFrame():
    def __init__(self, file: str, type: str) -> None:

        self.message = None
        self.df = None
        
        timestamp = int(time.time())
        file = f"{file}&cachebuster={timestamp}"

        try:
            if type == "excel":
                self.df = pd.read_excel(file, index_col=0)
            else:
                self.df = pd.read_csv(file, index_col=0)
        except Exception as e:
            self.message = self.format_import_error(e)
            return
        
        self.df = self.format_index_columns(self.df)
    
    def format_import_error(self, e: Exception) -> str:
        """Formata uma mensagem de erro de importação de planilha."""
        
        user_message = "⚠️ Erro na importação!\n\n"

        if isinstance(e, PermissionError):
            user_message += "Arquivo está aberto em outro programa ou sem permissão de acesso.\nFeche o arquivo e tente novamente.\n\n"
        elif isinstance(e, FileNotFoundError):
            user_message += "Arquivo não encontrado. Verifique o caminho informado.\n\n"
        else:
            user_message += "Erro inesperado ao tentar ler o arquivo.\n\n"

        user_message += f"Detalhes técnicos: {type(e).__name__}: {e}"

        return user_message


    def format_index_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Padroniza index e colunas:
        - Se for Timestamp, converte para 'dd/mm/yyyy'
        - Se não for, transforma em string
        """

        # Padronizar index
        df.index = pd.Index([self.format_date(item) for item in df.index]).infer_objects()

        # Padronizar columns
        df.columns = pd.Index([self.format_date(col) for col in df.columns]).infer_objects()

        return df
    
    def format_date(self, valor):
            try:
                if isinstance(valor, pd.Timestamp):
                    return valor.strftime('%d/%m/%Y')
                else:
                    valor_convertido = pd.to_datetime(valor, errors='raise', dayfirst=True)
                    return valor_convertido.strftime('%d/%m/%Y')
            except (ValueError, TypeError):
                return str(valor)
    
    def format_number(self, value):
        if pd.isna(value):
            return "Vazio"
        
        if isinstance(value, float):
            if value.is_integer():
                return int(value)
            else:
                value = str(value).replace(".", '_')
                value = value.replace(",", '.')
                value = value.replace("_", ',')
                return value
        
        return value
        
    def format_text(self, text: str, field: str, axis: str,) -> str:
        if self.message:
            return self.message
        
        headers = None
        row_values = None
        
        try:
            if axis == 'column':
                
                headers = self.df.index.to_list()
                row_values = self.df[field].tolist()
                
                for header, value in zip(headers, row_values):
                    header = str(header)
                    value = str(self.format_number(value))
                    
                    text = text.replace('['+header+']', value)
            
            else:
                
                headers = self.df.columns.to_list()
                row_values = self.df.loc[field].tolist()
                
                for header, value in zip(headers, row_values):
                    
                    header = str(header)
                    value = str(self.format_number(value))
                    
                    text = text.replace('['+header+']', value)
                
                
        except KeyError:
            return f"Campo '{field}' não encontrada na planilha!"
        
        except Exception as e:
            return f"Erro : {e}"

            
        return text
        
import customtkinter as ctk

class UpdateProgressWindow(ctk.CTkToplevel):
    def __init__(self, master=None, total_size=100, title="Baixando Atualização"):
        super().__init__(master)
        self.title(title)
        self.geometry("400x180")
        self.resizable(False, False)
        self.configure(fg_color="#1E1E1E")

        # Label principal
        self.label = ctk.CTkLabel(self, text="Iniciando download...", font=("Arial", 16, "bold"), text_color="#EAEAEA")
        self.label.pack(pady=(20, 10))

        # ProgressBar estilizada
        self.progress_bar = ctk.CTkProgressBar(self, width=300, height=20, corner_radius=10, progress_color="#3B82F6")
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        # Label percentual
        self.percent_label = ctk.CTkLabel(self, text="0%", font=("Arial", 13), text_color="#A1A1AA")
        self.percent_label.pack(pady=(5, 20))

        self.total_size = total_size
        self.downloaded_size = 0

        self.update_idletasks()

    def update_progress(self, chunk_size):
        self.downloaded_size += chunk_size
        progress = self.downloaded_size / self.total_size
        self.progress_bar.set(progress)

        percentual = progress * 100
        self.percent_label.configure(text=f"{percentual:.2f}%")

        if percentual < 100:
            self.label.configure(text="Baixando atualização...")
        else:
            self.label.configure(text="Finalizando...")

        self.update_idletasks()

    def download_complete(self):
        self.label.configure(text="Download concluído!")
        self.percent_label.configure(text="100%")
        self.update_idletasks()


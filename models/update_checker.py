import requests
import os
import sys
import zipfile
import shutil
import tkinter.messagebox as messagebox
import customtkinter as ctk
from models.UpdateProgressWindow import UpdateProgressWindow
from config.theme import ATUAL_VERSAO

URL_JSON_VERSAO = "https://raw.githubusercontent.com/NickYoshizawa/relatorio-auto/main/versao.json"

def check_update():
    try:
        response = requests.get(URL_JSON_VERSAO)
        if response.status_code == 200:
            data = response.json()
            nova_versao = data["version"]
            para = data["for"]
            download_url = data["download_url"]
            changelog = data.get("changelog", "Sem informações.")

            if para == "all" and nova_versao != ATUAL_VERSAO:
                resposta = messagebox.askyesno(
                    "Atualização disponível!",
                    f"Nova versão {nova_versao} disponível!\n\n{changelog}\n\nDeseja atualizar agora?"
                )
                if resposta:
                    baixar_e_instalar(download_url)
            else:
                print("Você já está na última versão.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao verificar atualização: {e}")

def baixar_e_instalar(url):
    try:
        nome_arquivo = "update.zip"
        caminho_zip = os.path.join(os.getcwd(), nome_arquivo)

        # Janela de progresso própria, já que MainWindow não existe ainda
        root = ctk.CTk()
        root.withdraw()  # Esconde a janela principal (não queremos que ela apareça)
        progress_window = UpdateProgressWindow(master=root)
        progress_window.grab_set()

        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        progress_window.total_size = total_size

        with open(caminho_zip, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    progress_window.update_progress(len(chunk))

        progress_window.download_complete()
        progress_window.grab_release()
        progress_window.after(2000, progress_window.destroy)
        root.mainloop()

        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            for member in zip_ref.namelist():
                zip_ref.extract(member, os.getcwd())

        os.remove(caminho_zip)

        messagebox.showinfo(
            "Atualização concluída!",
            "O aplicativo foi atualizado com sucesso!\nReinicie o programa para usar a nova versão."
        )

        sys.exit()

    except Exception as e:
        messagebox.showerror("Erro", f"Falha na atualização: {e}")
        sys.exit()

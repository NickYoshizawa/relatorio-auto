import requests
import os
import sys
import zipfile
import tkinter.messagebox as messagebox

ATUAL_VERSAO = "1.0.0"
URL_JSON_VERSAO = "https://NickYoshizawa.github.io/relatorio-auto/versao.json"

def check_update():
    try:
        response = requests.get(URL_JSON_VERSAO)
        if response.status_code == 200:
            data = response.json()
            nova_versao = data["version"]
            para = data["for"]
            download_url = data["download_url"]
            changelog = data.get("changelog", "Sem informações.")
            
            if para == "all":
                if nova_versao != ATUAL_VERSAO:
                    resposta = messagebox.askyesno(
                        "Atualização disponível!",
                        f"Nova versão {nova_versao} disponível!\n\n{changelog}\n\nDeseja atualizar agora?"
                    )
                    if resposta:
                        baixar_e_instalar(download_url)
                else:
                    print("Você já está na última versão.")
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")

def baixar_e_instalar(url):
    try:
        # Nome do arquivo zip
        nome_arquivo = "update.zip"
        caminho_zip = os.path.join(os.getcwd(), nome_arquivo)

        # Baixar o zip
        r = requests.get(url, stream=True)
        with open(caminho_zip, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        # Descompactar
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())

        # Remover o zip após descompactar
        os.remove(caminho_zip)

        messagebox.showinfo(
            "Atualização concluída!",
            "O aplicativo foi atualizado com sucesso!\nReinicie o programa para usar a nova versão."
        )

        sys.exit()

    except Exception as e:
        messagebox.showerror("Erro!", f"Falha na atualização: {e}")

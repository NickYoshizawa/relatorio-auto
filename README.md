
# Relatório Automático - Integração Google Sheets / Excel

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

---

## 📄 Descrição Curta

Aplicativo de desktop para integração e geração automática de relatórios a partir de planilhas Google Sheets ou arquivos Excel locais (.xlsx/.csv), com substituição dinâmica de dados.

---

## 💡 Objetivo do Projeto

Facilitar a criação de relatórios automáticos e personalizados, usando dados extraídos de planilhas em poucos cliques, de forma rápida e sem necessidade de codificação manual.

---

## 🛠️ Tecnologias Usadas

- [Python 3.10+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) (para leitura de Excel)
- [Tkinter (GUI base)](https://docs.python.org/3/library/tkinter.html)

---

## 🏗️ Como Instalar e Rodar o Projeto

### 1. Clone o repositório
```bash
https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```

### 2. Navegue até a pasta do projeto
```bash
cd relatorio-auto
```

### 3. Crie um ambiente virtual (opcional, recomendado)
```bash
python -m venv venv
```

### 4. Ative o ambiente virtual
- **Windows**:
```bash
venv\Scripts\activate
```
- **Linux / MacOS**:
```bash
source venv/bin/activate
```

### 5. Instale as dependências
```bash
pip install -r requirements.txt
```

### 6. Execute o programa
```bash
python main.py
```

---

## 📥 Download do Executável (.exe)

Este projeto possui uma versão executável para Windows, que permite rodar o programa sem a necessidade de instalar o Python.

### 🔗 Última versão:

👉 [Baixar Executável (.exe) - Versão mais recente](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/releases/latest)

> **Nota**: Certifique-se de fazer o download do arquivo `.exe` correspondente à última release publicada.

---

## 🛠️ Como Gerar seu próprio Executável

Caso deseje gerar sua própria versão do `.exe`, siga as instruções:

1. Instale o PyInstaller:
```bash
pip install pyinstaller
```

2. Gere o arquivo:
```bash
pyinstaller --noconsole --onefile --icon=assets/icon/icon.ico main.py
```

O arquivo gerado estará localizado na pasta:
```
/dist/main.exe
```

---

## 🔧 Funcionalidades Principais

- 👁️ Interface moderna e responsiva usando CustomTkinter
- 📅 Leitura de planilhas Google Sheets (formato CSV) e arquivos Excel (.xlsx, .csv)
- 🔄 Atualização dinâmica de textos substituindo placeholders com dados da planilha
- 🔢 Busca de dados por **linha** ou **coluna**
- 📥 Suporte a seleção de arquivos pelo sistema
- 📤 Armazena inputs e arquivos usados para reuso rápido
- 📚 Trata erros de forma amigável (ex: arquivo aberto, ausente ou corrompido)

---

## 🧾 Licença

Este projeto está licenciado sob a Licença MIT.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Desenvolvedor

Feito com ❤️ por **[Seu Nome ou GitHub]**.  
Se gostou do projeto, deixe uma estrela! ⭐

---

# ✨ Exemplo Visual

> "Insira aqui uma imagem/gif de demonstração se desejar futuramente."

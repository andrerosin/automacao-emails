import pyperclip
import pyautogui
import pandas
import time
import os

pyautogui.PAUSE = 1

# Passo 1: Acessar o sistema de vendas
os.system("start chrome")
time.sleep(3)
pyautogui.click(x=955, y=601)

time.sleep(3)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
time.sleep(1)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login no sistema
pyautogui.press("tab")
pyautogui.write("meu login")

pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Baixar a base de dados

pyautogui.press("tab")
pyautogui.press("right")
pyautogui.press("enter")

time.sleep(3)

# Passo 4: Calculcar os indicadores

# importar a base de dados

tabela = pandas.read_csv(r"C:\Users\andre\Downloads\Compras.csv", sep=";")

# calculo dos indicadores
# total gasto
total_gasto = tabela["ValorFinal"].sum()

# quantidade
quantidade = tabela["Quantidade"].sum()

# preço médio
preco_medio = total_gasto / quantidade

# Passo 5: Enviar o e-mail para a diretoria

# entrar no meu email
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox?compose=new")
pyautogui.press("enter")

time.sleep(5)

# preencher o email
pyautogui.write("pyautogui@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab")
pyperclip.copy("Relatório de Compras")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto = f"""
Prezados,

Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida é só falar.
Att.,
Python Gui
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar
pyautogui.hotkey("ctrl", "enter")
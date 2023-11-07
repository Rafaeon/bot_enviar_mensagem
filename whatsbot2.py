import time
import pyautogui as py
import pandas as pd


tabela = pd.read_csv("botwhats/Pasta1.csv", sep=';')
print(tabela.head())

time.sleep(5)

def enviar_mensagem_e_retornar(numero, mensagem):

    py.click(x=154, y=188)
    time.sleep(3)

    
    py.write(numero)
    py.press("tab")
    py.press("enter")
    time.sleep(3)

    
    py.click(x=1037, y=996)
    time.sleep(3)

    
    py.write(mensagem)
    time.sleep(1)

    
    py.press("enter")

    
    py.click(x=154, y=188)


for linha in tabela.index:
    numero_contato = tabela.loc[linha, 'numero']
    mensagem = tabela.loc[linha, 'mensagem']

    enviar_mensagem_e_retornar(numero_contato, mensagem)


#py.hotkey("ctrl", "w") fechar navegador


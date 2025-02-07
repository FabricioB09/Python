import pyautogui
import pyperclip
import pandas
import time
pyautogui.PAUSE= 2
tabela = pandas.read_excel(r'C:\Users\inove\Downloads\Vendas - Dez.xlsx')
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=56, y=187)
pyperclip.copy('inovetech9@gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f''' Prezados, Boa tarde
O faturamento desse mês foi de {faturamento:,.2f}R$
E a quantidade de produtos vendidos foi {quantidade:,}

Atenciosamente
Fabricio Barbosa'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')




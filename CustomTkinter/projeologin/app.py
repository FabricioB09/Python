# NUNCA ESQUECER DE IMPORTAR AS BIBLIOTECAS QUE SERÃO USADAS NO CODIGO
# O as NA LINHA SERVE PARA DAR UM NOVO NOME AQUELA BIBLIOTECA
import customtkinter as ctk

#CRIAÇÃO DAS FUNCTIONS
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #verificar se o usuario é Fabricio, e a senha é 000000
    if usuario == 'Fabricio' and senha == '000000':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    elif usuario == 'Fabricio' and senha != '000000':
       resultado_login.configure(text='Senha Incorreta, Digite novamente!', text_color='red') 
    elif senha == '000000' and usuario != 'Fabricio':
        resultado_login.configure(text='Usuario Incorreto, Digite novamente!', text_color='red')
    else:
        resultado_login.configure(text='Usuario e Senha incorretos, digite novamente!', text_color='red')

#CONFIGURAÇÃO DE APARENCIA
ctk.set_appearance_mode('dark')

#CRIAÇÃO DA JANELA PRINCIPAL
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')
#CRIAÇÃO DE CAMPOS
#label
label_usuario = ctk.CTkLabel(app,text='Usuario:')
label_usuario.pack(pady=5)
#entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu Usuario')
campo_usuario.pack(pady=5)
#label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack(pady=5)
#entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=5)
#button
button_login = ctk.CTkButton(app, text='Login', command=validar_login)
button_login.pack(pady=5)
#CAMPO FEEDBACK DE LOGIN
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=5)

#INICIALIZAR APLICAÇÃO
app.mainloop()